// Dark Mode Toggle
const darkModeToggle = document.getElementById('darkModeToggle');
darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    darkModeToggle.textContent = document.body.classList.contains('dark-mode') ? '☀️ Light Mode' : '🌙 Dark Mode';
});

// Menu Filtering
const menuItems = [
    { name: 'Garlic Bread', category: 'starters', price: '$5.00', image: 'https://via.placeholder.com/150', description: 'Freshly baked garlic bread with herbs.' },
    { name: 'Caesar Salad', category: 'starters', price: '$7.00', image: 'https://via.placeholder.com/150', description: 'Classic Caesar salad with croutons and parmesan.' },
    { name: 'Grilled Salmon', category: 'main-course', price: '$15.00', image: 'https://via.placeholder.com/150', description: 'Grilled salmon served with vegetables.' },
    { name: 'Beef Steak', category: 'main-course', price: '$20.00', image: 'https://via.placeholder.com/150', description: 'Juicy beef steak with mashed potatoes.' },
    { name: 'Chocolate Cake', category: 'desserts', price: '$8.00', image: 'https://via.placeholder.com/150', description: 'Rich chocolate cake with a creamy filling.' },
    { name: 'Cheesecake', category: 'desserts', price: '$9.00', image: 'https://via.placeholder.com/150', description: 'Classic New York-style cheesecake.' },
];

const filterButtons = document.querySelectorAll('.filter-btn');
const menuContainer = document.querySelector('.menu-items');

function displayMenuItems(filter = 'all') {
    menuContainer.innerHTML = menuItems
        .filter(item => filter === 'all' || item.category === filter)
        .map(item => `
            <div class="item" onclick="openModal('${item.name}', '${item.image}', '${item.description}', '${item.price}')">
                <img src="${item.image}" alt="${item.name}">
                <h3>${item.name}</h3>
                <p>${item.price}</p>
            </div>
        `)
        .join('');
}

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        displayMenuItems(button.dataset.filter);
    });
});

displayMenuItems(); // Initialize menu

// Modal Functionality
function openModal(name, image, description, price) {
    const modal = document.getElementById('dishModal');
    document.getElementById('modalTitle').textContent = name;
    document.getElementById('modalImage').src = image;
    document.getElementById('modalDescription').textContent = description;
    document.getElementById('modalPrice').textContent = price;
    modal.style.display = 'flex';
}

function closeModal() {
    document.getElementById('dishModal').style.display = 'none';
}

// Image Slider
let currentSlide = 0;
const slides = document.querySelectorAll('.slider img');

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${100 * (i - index)}%)`;
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

showSlide(currentSlide);

// Smooth Scrolling
function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
}

// Form Validation
document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    this.reset();
});