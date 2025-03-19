[11,2,2,3,4,555,6,7,88,9,19]
arr.sort(reverse=False)
print(arr)
# [555, 88, 19, 11, 9, 7, 6, 4, 3, 2, 2]
minv=arr[0]
print(minv)
sminv=arr[arr.count(minv)]
print(sminv)