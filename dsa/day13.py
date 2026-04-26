# - Max consecutive ones (leet code 485).

def max_consecutive_ones(arr):
    count = 0
    maxi = 0
    
    for num in arr:
        if num == 1:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
            
    return maxi

arr = [1,1,0,0,1,1,1,1,1,0]
print(max_consecutive_ones(arr))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)