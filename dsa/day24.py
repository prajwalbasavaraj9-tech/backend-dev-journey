# - 4 sum problem (leet code 18).

def Four_sum(arr, target):
    n = len(arr)
    arr.sort()
    res = []
    
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            
            k = j + 1
            l = n - 1
            
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                
                if total == target:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    res.append(temp)
                    k += 1
                    l -= 1
                    
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                        
                    while k < l and arr[l] == arr[l + 1]:
                        l -= 1
                    
                elif total < target:
                    k += 1
                    
                else:
                    l -= 1
                     
    return res

arr = [1, 0, -1, 0, -2, 2, 5, 9]
target = 0
print(Four_sum(arr, target))

# Time Complexity (TC): O(n ^ 3)
# Space Complexity (SC): O(1)