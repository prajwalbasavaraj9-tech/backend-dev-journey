# - Find the largest element in an array.

def finding_largest(arr):
    n = len(arr)
    largest = arr[0]
    
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
            
    return largest

arr = [1,2,3,15,6,9]
print(finding_largest(arr))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)