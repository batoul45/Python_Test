def find_minimuim(arr):
    # Assume the first row has the minimum sum initially
    min_row_index = 0
    min_row_sum = sum(arr[0])
    
    # we use the loop to find the row with the minimum sum
    for i in range(1, len(arr)):
        row_sum = sum(arr[i])
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i
    
    # Assume the first column has the minimum sum initially
    min_col_index = 0
    min_col_sum = sum(row[0] for row in arr)
    
    # Loop each column to find the minimum sum and its column
    for j in range(1, len(arr[0])):
        col_sum = sum(row[j] for row in arr)
        if col_sum < min_col_sum:
            min_col_sum = col_sum
            min_col_index = j

    # Return the row and column indices with the minimum sums
    return [min_row_index, min_col_index]

# Example 
array = [
    [3, 5, 1],
    [7, 2, 6],
    [4, 8, 0]
]
print(find_minimuim(array))  
