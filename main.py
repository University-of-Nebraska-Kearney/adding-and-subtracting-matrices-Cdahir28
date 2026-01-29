# Need to be able to get two matrix and their values
# Also need to be able to add the matrix together to make one matrix
# Add a check to make sure the matrix can be added together based on size
# *Last checked does work*

def get_matrix():
    # Get number of rows and columns
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    # Loop through each row
    for r in range(rows):
        row = []
        # Loop through each column
        for c in range(cols):
            value = int(input(f"Enter a value at {r}, {c}: "))
            row.append(value)
        # Add the row to the matrix
        matrix.append(row)

    # Loop for matrix1 and matrix2
    return matrix

def add_matrix(matrix1, matrix2):
    # Error check, just if matrices are the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices cannot be added")
        return None

    result = []
    # Go through rows
    for r in range(len(matrix1)):
        row = []
        # Go through columns
        for c in range(len(matrix1[0])):
            row.append(matrix1[r][c] + matrix2[r][c])
        result.append(row)

    return result


def main():
    print("Build first matrix")
    matrix1 = get_matrix()

    print("Build second matrix")
    matrix2 = get_matrix()

    result = add_matrix(matrix1, matrix2)
    # Print the result if addition worked
    if result is not None:
        print("Result:")
        for row in result:
            print(row)

if __name__ == '__main__':
    main()
