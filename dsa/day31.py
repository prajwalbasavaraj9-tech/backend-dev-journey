# - Find minimum in rotated sorted array (leet code 153).

def rotated_minimum(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mini = float('inf')
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] <= arr[high]:
            mini = min(mini, arr[mid])
            high = mid - 1
        else:
            mini = min(mini, arr[low])
            low = mid + 1
    
    return mini

arr = [7,8,1,2,3,5,6]
print(rotated_minimum(arr))

# Time Complexity (TC): O(logn)
# Space Complexity (SC): O(1)