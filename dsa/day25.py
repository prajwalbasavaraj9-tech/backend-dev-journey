# - Search insert position (leet code 35).
# - alias find lower bound 

def lower_bound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    idx = n
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] >= target:
            idx = mid
            high = mid - 1
            
        else:
            low = mid + 1
            
    return idx

arr = [1,2,3,5,7,8]
target = 6
print(lower_bound(arr, target))

# Time Complexity (TC): O(log2n)
# Space Complexity (SC): O(1)