# - Check if the array is sorted or not.

def check_for_sorting(arr):
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return 'Not-sorted..!'
    
    return 'Sorted.'
    
arr1 = [1,2,3,4,4,5]
arr2 = [5,4,3,1,7,8]
print(check_for_sorting(arr1))
print(check_for_sorting(arr2))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)