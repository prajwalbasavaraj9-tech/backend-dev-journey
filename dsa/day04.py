# - Remove duplicates from sorted array (leet code 26).

def remove_duplicates(arr):   # (Optimal Sol^ x1)
    n = len(arr)
    i = 0
    j = i + 1
    
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
        
    return i + 1

def removeduplicates(arr):      # (Optimal Sol^ x2)
    n = len(arr)
    k = 1
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[k] = arr[i]
            k += 1
            
    return k

arr0 = [1,1,2,2,3,3,4,5,6,6]
arr1 = [1,2,2,2,3,3,4]
print(remove_duplicates(arr0))
print(removeduplicates(arr1))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)
# for both Sol^'s