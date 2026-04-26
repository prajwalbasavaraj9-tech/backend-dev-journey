# - Search in rotated sorted array 2 (leet code 81).

def rotated_sorted(arr, target):
    n = len(arr)
    low, high = 0, n - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return True
        
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        
        for i in range(mid + 1, high):
            if arr[i] == arr[i + 1]:
                arr[mid] = arr[i + 1]
                
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
                
    return False

arr = [7,7,7,7,7,7,7,7,1,2,3,5,7]
target = 1
print(rotated_sorted(arr, target))

# Time Complexity (TC): for avg case --> O(log2n)  worst case -- > O(n)
# Space Complexity (SC): O(1)