# - Right rotate an array by k place (leet code 189).

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
def right_rotate(arr, k):
    n = len(arr)
    k = k % n
    
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - k - 1)
    reverse(arr, 0, n - 1)
    
    return arr

arr = [4,5,6,1,2,3]
print(right_rotate(arr, 3))


# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)