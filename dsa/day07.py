# - Find the last occurrence of target (linear search).

def last_index(arr, target):
    n = len(arr)
    last_index = arr[-1]
    
    for i in range(n):
        if arr[i] == target:
            last_index = i
        
    return last_index

def last_idx(arr, target):
    n = len(arr)
    
    for i in range(n - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1

arr = [1,2,3,3,3,4,4,5]
target = 3
print(last_index(arr, target))
print(last_idx(arr, target))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)