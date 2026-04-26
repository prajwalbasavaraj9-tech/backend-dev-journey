# - Max sub array sum (Kadane's algorithm) (leet code 53).

def maxsub_arrsum(arr):
    n = len(arr)
    maxi = float('-inf')
    total = 0
    
    for i in range(n):
        total = total + arr[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
            
    return maxi

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsub_arrsum(arr))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)