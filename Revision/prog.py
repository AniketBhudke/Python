
// Gas Tracker Simulator - Next.js + Zustand + Ethers + Lightweight Charts with Simulation Mode

// 1. Zustand Store (store/gasStore.js)
import create from 'zustand';
import { ethers } from 'ethers';

export const useGasStore = create((set) => ({
  mode: 'live',
  transactionValue: 0.5, // Default simulation value in ETH
  chains: {
    ethereum: { baseFee: 0, priorityFee: 0, history: [] },
    polygon: { baseFee: 0, priorityFee: 0, history: [] },
    arbitrum: { baseFee: 0, priorityFee: 0, history: [] },
  },
  usdPrice: 0,
  setMode: (mode) => set({ mode }),
  setTransactionValue: (value) => set({ transactionValue: value }),
  updateChain: (chain, data) =>
    set((state) => ({
      chains: { ...state.chains, [chain]: { ...state.chains[chain], ...data } },
    })),
  setUsdPrice: (price) => set({ usdPrice: price }),
}));

// 2. WebSocket Providers + Data Fetcher (utils/providers.js)
import { useGasStore } from '../store/gasStore';

export const setupProviders = () => {
  const ethProvider = new ethers.providers.WebSocketProvider('wss://mainnet.infura.io/ws/v3/YOUR_PROJECT_ID');
  const polygonProvider = new ethers.providers.WebSocketProvider('wss://polygon-mainnet.g.alchemy.com/v2/YOUR_API_KEY');
  const arbitrumProvider = new ethers.providers.WebSocketProvider('wss://arb-mainnet.g.alchemy.com/v2/YOUR_API_KEY');

  const store = useGasStore.getState();

  ethProvider.on('block', async (blockNumber) => {
    const block = await ethProvider.getBlock(blockNumber);
    store.updateChain('ethereum', {
      baseFee: block.baseFeePerGas?.toNumber() || 0,
      priorityFee: ethers.utils.parseUnits('2', 'gwei').toNumber(),
    });
  });

  polygonProvider.on('block', async (blockNumber) => {
    const block = await polygonProvider.getBlock(blockNumber);
    store.updateChain('polygon', {
      baseFee: block.baseFeePerGas?.toNumber() || 0,
      priorityFee: ethers.utils.parseUnits('30', 'gwei').toNumber(),
    });
  });

  arbitrumProvider.on('block', async (blockNumber) => {
    const block = await arbitrumProvider.getBlock(blockNumber);
    store.updateChain('arbitrum', {
      baseFee: block.baseFeePerGas?.toNumber() || 0,
      priorityFee: ethers.utils.parseUnits('1', 'gwei').toNumber(),
    });
  });
};

// 3. ETH/USD Price Fetcher (utils/usdPrice.js)
import UNISWAP_ABI from '../abis/uniswap.json';

export const fetchEthUsdPrice = async () => {
  const provider = new ethers.providers.WebSocketProvider('wss://mainnet.infura.io/ws/v3/YOUR_PROJECT_ID');
  const pool = new ethers.Contract(
    '0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640',
    UNISWAP_ABI,
    provider
  );

  pool.on('Swap', (sender, recipient, amount0, amount1, sqrtPriceX96) => {
    const price = (sqrtPriceX96 ** 2 * 10 ** 12) / 2 ** 192;
    useGasStore.getState().setUsdPrice(price);
  });
};

// 4. Lightweight Charts Component (components/GasChart.js)
import React, { useEffect, useRef } from 'react';
import { createChart } from 'lightweight-charts';
import { useGasStore } from '../store/gasStore';

export default function GasChart({ chain }) {
  const chartRef = useRef();
  const { chains } = useGasStore();

  useEffect(() => {
    const chart = createChart(chartRef.current, { width: 600, height: 300 });
    const series = chart.addCandlestickSeries();

    const interval = setInterval(() => {
      const history = chains[chain].history;
      series.setData(history);
    }, 6000);

    return () => clearInterval(interval);
  }, [chains, chain]);

  return <div ref={chartRef}></div>;
}

// 5. Simulation Mode Form (components/SimulationForm.js)
import { useGasStore } from '../store/gasStore';

export default function SimulationForm() {
  const { transactionValue, setTransactionValue, chains, usdPrice } = useGasStore();

  const handleChange = (e) => {
    setTransactionValue(parseFloat(e.target.value));
  };

  const gasLimit = 21000;

  const calculateCost = (baseFee, priorityFee) => {
    return ((baseFee + priorityFee) * gasLimit * usdPrice) / 1e9;
  };

  return (
    <div>
      <input
        type="number"
        value={transactionValue}
        onChange={handleChange}
        placeholder="Enter ETH value"
      />
      <table>
        <thead>
          <tr>
            <th>Chain</th>
            <th>Base Fee (Gwei)</th>
            <th>Priority Fee (Gwei)</th>
            <th>USD Cost</th>
          </tr>
        </thead>
        <tbody>
          {Object.keys(chains).map((chain) => (
            <tr key={chain}>
              <td>{chain}</td>
              <td>{chains[chain].baseFee}</td>
              <td>{chains[chain].priorityFee}</td>
              <td>{calculateCost(chains[chain].baseFee, chains[chain].priorityFee).toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// 6. Main Page (pages/index.js)
import React, { useEffect } from 'react';
import { setupProviders } from '../utils/providers';
import { fetchEthUsdPrice } from '../utils/usdPrice';
import GasChart from '../components/GasChart';
import SimulationForm from '../components/SimulationForm';
import { useGasStore } from '../store/gasStore';

export default function Home() {
  const { mode, setMode } = useGasStore();

  useEffect(() => {
    setupProviders();
    fetchEthUsdPrice();
  }, []);

  return (
    <div>
      <h1>Real-Time Cross-Chain Gas Tracker</h1>
      <button onClick={() => setMode(mode === 'live' ? 'simulation' : 'live')}>
        Switch to {mode === 'live' ? 'Simulation' : 'Live'} Mode
      </button>
      {mode === 'live' ? (
        <div>
          <GasChart chain="ethereum" />
          <GasChart chain="polygon" />
          <GasChart chain="arbitrum" />
        </div>
      ) : (
        <SimulationForm />
      )}
    </div>
  );
}

// 7. Basic CSS Layout (styles/globals.css)
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background: #121212;
  color: white;
}

input, button {
  padding: 0.5rem;
  margin: 0.5rem;
  border-radius: 5px;
}

// 8. ABI File (abis/uniswap.json)
[
  {
    "anonymous": false,
    "inputs": [
      { "indexed": true, "name": "sender", "type": "address" },
      { "indexed": true, "name": "recipient", "type": "address" },
      { "indexed": false, "name": "amount0", "type": "int256" },
      { "indexed": false, "name": "amount1", "type": "int256" },
      { "indexed": false, "name": "sqrtPriceX96", "type": "uint160" }
    ],
    "name": "Swap",
    "type": "event"
  }
]










