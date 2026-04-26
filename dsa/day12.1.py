# - Find all missing's in sorted array and fill them in-place.

def finding_them(arr):                # 🧧 12.1.py
    last_digit = arr[-1]
    res = []
    
    for i in range(last_digit + 1):
        if i not in arr:
            res.append(i)
            
    return res

# Time Complexity (TC): O(L x N)  # loop and The "in" Operator
# Space Complexity (SC): O(M)  # missing numbers

def filling_them(arr, res):
    i = j = 0
    
    while i < len(arr) and j < len(res):
        if arr[i] > res[j]:
            arr.insert(i, res[j])
            i += 1
            j += 1
        else:
            i += 1
            
    return arr

# Time Complexity (TC): O(N x (N + M))  # insert oper^
# Space Complexity (SC): O(1)

arr = [1,3,5,7]
found_here = finding_them(arr)
filled_here = filling_them(arr, found_here)
print(filled_here)

# Time Complexity (TC): O(N^2)
# Space Complexity (SC): O(M)