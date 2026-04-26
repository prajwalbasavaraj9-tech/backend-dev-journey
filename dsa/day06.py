# - Move zeroes to the end (in-place) (leet code 283).

def move_zeors_end(arr):
    n = len(arr)
    i = 0 
    
    while i < n:
        if arr[i] == 0:
            break
        i += 1
        
    if i == n:
        return arr
        
    j = i + 1
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    
    return arr

arr = [1,0,2,0,3,0]
print(move_zeors_end(arr))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)