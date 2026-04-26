# - Rotate matrix by 90 degree (leet code 48).
'''
1st - transpose the matrix
2nd - reverse each row 
3rd - matrix style present^
'''

def rotate_matrix(arr):
    n = len(arr)
        
    for r in range(n):
        for c in range(r + 1, n):
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]
            
    for i in range(len(arr)):
        arr[i].reverse()
        
    return arr

grid = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
result = rotate_matrix(grid)

for row in result:
    print(row)
    
# Time Complexity (TC): O(n^2)
# Space Complexity (SC): O(1)