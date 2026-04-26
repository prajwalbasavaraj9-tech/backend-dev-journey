# - Find the second largest element in an array.

def second_largest(arr):
    n = len(arr)
    
    if n < 2:
        return "array must contain more than 2 items..!"
    
    largest = sec_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            sec_largest = largest
            largest = num
            
        if num > sec_largest and num != largest:
            sec_largest = num
            
    if sec_largest == float('-inf'):
        return "something is fishy..!(all items must be equal)"
    
    return sec_largest

arr1 = [11,34,5,66,83,101]
arr2 = [100]
arr3 = [1,1,1,1,1,1,1]
print(second_largest(arr1))
print(second_largest(arr2))
print(second_largest(arr3))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)