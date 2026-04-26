# - Search target in 2D array / matrix (linear search).

def search_in_matrix(matrix, target):
    
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == target:
                return (r, c)
            
    return (-1, -1)

grid = [[1,2,3],
        [5,6,7]]
print(search_in_matrix(grid, 7))

# Time Complexity (TC): O(n ^ m)
# Space Complexity (SC): O(1)