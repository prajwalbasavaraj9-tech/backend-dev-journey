# - Finding missing num in an array (leet code 268).

def missing_num(arr):
    n = len(arr)
    
    expected_sum = (n * (n + 1)) // 2
    original_sum = sum(arr)
    
    return expected_sum - original_sum

nums = [0,1,2,3,4,5,7,8]
print(missing_num(nums))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)