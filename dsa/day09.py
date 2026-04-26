# - Find elements with even number of digits (linear search).

def even_numbered_nums(arr):
    evens = []
    count = 0
    
    for i in range(len(arr)):
        if len(str(arr[i])) % 2 == 0:
            count += 1
            evens.append(arr[i])
            
    return count, evens

arr = [12,234,5346,876,125683]
res_count, res_list = even_numbered_nums(arr)
print(res_count)
print(res_list)

# Time Complexity (TC): O(n x d)  
''' 
Inside the Loop: The operation str(arr[i]) converts an integer to a string.
The time it takes to convert an integer to a string is proportional to the number of digits, d, in that integer.
'''
# Space Complexity (SC): O(1)