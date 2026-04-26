# - Merge two sorted array without duplicates.

def merge_two_sorteds(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    res = []
    
    i = j = 0
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
                
    while i < n:
        if len(res) == 0 or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1
        
    while j < m:
        if len(res) == 0 or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1
            
    return res
            
arr1 = [1,1,2,2,3,3,4]
arr2 = [3,4,5,6,7,9,10]
print(merge_two_sorteds(arr1, arr2))

# Time Complexity (TC): O(n + m)
# Space Complexity (SC): O(n + m)