# - Count occurrences of a num in sorted array with duplicates.

class solution:
    def lower_bound(arr, target):
        n = len(arr)
        low, high = 0, n - 1
        lb = n
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return lb
    
    def upper_bound(arr, target):
        n = len(arr)
        low, high = 0, n - 1
        ub = n
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ub
    
arr = [1,2,3,3,3,3,3,3,4,7]
target = 3
lower_bound = solution.lower_bound(arr, target)
upper_bound = solution.upper_bound(arr, target)
result = upper_bound - lower_bound
print(result)