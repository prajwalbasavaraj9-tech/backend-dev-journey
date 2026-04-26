# - Two sum problems (leet code 1).

def two_sum(arr, target):
    n = len(arr)
    freq = {}
    
    for i in range(n):
        remaining = target - arr[i]
        if remaining in freq:
            return [freq[remaining], i]
        freq[arr[i]] = i
    
    
arr = [2,4,5,5,9]
print(two_sum(arr, 13))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)  # Storing elements in a dictionary to find them later.