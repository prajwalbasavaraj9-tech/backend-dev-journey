# - Search in rotated sorted array (leet code 33)

def rotated_sorted(arr, target):
    n = len(arr)
    low, high = 0, n - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] <= arr[high]:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
        else:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1

arr = [6,7,8,1,2,3,4]
target = 1
print(rotated_sorted(arr, target)) 

# Time Complexity (TC): O(log2n)
# Space Complexity (SC): O(1)           