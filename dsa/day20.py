# - Set matrix zeros (row_col_track) (leet code 73).

def set_to_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    row_track = [0 for _ in range(rows)]
    col_track = [0 for _ in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                row_track[r] = -1
                col_track[c] = -1
            
    for r in range(rows):
        for c in range(cols):
            if row_track[r] == -1 or col_track[c] == -1:
                matrix[r][c] = 0
                
    return matrix

arr = [[1,2,3,4],
       [5,6,0,8],
       [9,0,1,3],
       [5,2,8,4]]
print(set_to_zero(arr))

# Time Complexity (TC): O(n x m)  # Total: O(2(N x M)), which simplifies to O(N x M).
# Space Complexity (SC): O(n + m)