def matrix_shape(matrix):
    if not len(matrix) == 0 and not len(matrix[0]) == 0:
        return [len(matrix), len(matrix[0])]
    else:
        raise ValueError  # Raising error for empty matrix


def isnum(x):
    if (
        not (type(x) is int) and not (type(x) is float) and not (type(x) is complex)
    ):  # Explore the possibility of extending to complex number matrices
        raise TypeError


def check_validity(matrix):
    # Checking if all the rows have equal number of elements(columns)
    for i in range(len(matrix) - 1):
        if not (len(matrix[i]) == len(matrix[i + 1])):
            raise ValueError

    # Checking if all the elements of the matrix are numeric

    for row in matrix:
        for element in row:
            isnum(element)


def test_matrices(matrix1, matrix2):  # Implementing matrix check

    check_validity(
        matrix1
    )  # Checking for uniform rows and columns, non_numeric elements
    check_validity(matrix2)

    if not matrix_shape(matrix1)[1] == matrix_shape(matrix2)[0]:
        # Checking for shape compatibility and empty matrices
        raise ValueError


def init_result(rows, cols):
    res = []
    for i in range(rows):
        row = [0 for j in range(cols)]
        res.append(row)

    return res


def multiply(matrix1, matrix2):

    result = init_result(matrix_shape(matrix1)[0], matrix_shape(matrix2)[1])

    for i in range(len(result)):
        for j in range(len(result[0])):
            tmp = 0
            for k in range(len(matrix1[0])):
                tmp += matrix1[i][k] * matrix2[k][j]
            result[i][j] = tmp

    return result


def matrix_multiply(matrix1, matrix2):
    # The assumption is that each of the matrices are represented in the 2-D nested list form

    test_matrices(
        matrix1, matrix2
    )  # Running the test function to check for compatibility and validity of the input matrices

    # result = init_result(matrix_shape(matrix1)[0], matrix_shape(matrix2)[1]) # Creating a result matrix to store the multiplication result

    return multiply(matrix1, matrix2)
