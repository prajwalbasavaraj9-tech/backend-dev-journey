# - Rearrange array elements by sign (+, -)(leet code 2149).

def rearrange_bysign(arr):
    n = len(arr)    
    positive_index = 0
    negative_index = 1
    result = [0] * n
    
    for i in range(n):
        if arr[i] >= 0:
            result[positive_index] = arr[i]
            positive_index += 2
        else:
            result[negative_index] = arr[i]
            negative_index += 2
            
    return result

arr = [1,2,3,-1,4,-2,-4]
print(rearrange_bysign(arr))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n) # result = [0] * n