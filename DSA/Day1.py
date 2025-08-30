#time complexity & space complexity
def print_numbers(n):
    for i in range(n):
        print(i)
#O(n) (loop runs n times).

def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
#O(n²) (nested loop → n × n).

def find_element(arr, x):
    for num in arr:
        if num == x:
            return True
    return False
#O(n) (in worst case, check all elements).

def constant_example(arr):
    print(arr[0])
#O(1) (always takes constant time).

