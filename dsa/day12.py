# - Find all missing's in sorted array and fill them in-place (Optimized to O(N)).

def fill_missing_optimized(arr):
    if not arr:
        return []
    
    return list(range(arr[-1] + 1))

arr = [1,3,5,7]
print(fill_missing_optimized(arr))

# Time Complexity (TC): O(N)
# Space Complexity (SC): O(N)