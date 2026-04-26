# - Find the ceil and floor value of num.

def binary_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    floor = -1
    ceil = -1   
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return [arr[mid], arr[mid]]
        
        elif arr[mid] < target:
            floor = arr[mid]
            low = mid + 1
            
        else:
            ceil = arr[mid]
            high = mid - 1
            
    return [floor, ceil]

arr = [1,2,3,6,8,10]
target = 9
print(binary_search(arr, target))

# Time Complexity (TC): O(log2n)
# Space Complexity (SC): O(1)