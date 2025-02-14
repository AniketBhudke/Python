set1 = np.array([1, 2,2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=False)

print(newarr)
