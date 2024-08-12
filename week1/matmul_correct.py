from typing import List, Union

def matrix_shape(matrix: List[List]) -> List:
    """Returns the shape of the matrix.

    Parameters:
    matrix(List[List]]): A matrix denoted in the form of a list of lists.

    Returns:
    List: The number of rows and columns in the matrix, in that order.

    This is a function that returns the shape of the matrix in the form of a list when it is validly defined.
    """

    # Check if the matrix has no columns or no rows
    if not len(matrix) == 0 and not len(matrix[0]) == 0:
        # Return the shape of the matrix as a list that can be unpacked
        return [len(matrix), len(matrix[0])]
    else:
        # Raise a ValueError when the matrix is defined invalidly
        raise ValueError


def isnum(x: Union[int, float, complex]) -> None:
    """Checks if the given element is numeric.

    Parameters:
    x(Union[int, float, complex]): The value to be checked.

    Returns: 
    None

    This is a function that raises a TypeError when the data in the matrix is of non-numeric type.
    """

    # Check if the element belongs to one of the numeric classes
    if (
        not ((type(x) is int) or (type(x) is float) or (type(x) is complex))
    ):  
        # Raise an error if the element is of a non-numeric type
        raise TypeError


def check_validity(matrix: List[List[Union[int, float, complex]]]) -> None:
    """Checks the validity of the matrix.

    Parameters:
    matrix(List[List[Union[int, float, complex]]]): The matrix to be validated.

    Returns:
    None

    This function raises a ValueError if all the rows of the matrix do not have 
    an equal number of elements or if the matrix contains non-numeric elements.
    """

    # Checking if all the rows have an equal number of elements (columns)
    for i in range(len(matrix) - 1):
        if not (len(matrix[i]) == len(matrix[i + 1])):
            raise ValueError

    # Checking if all the elements of the matrix are numeric
    for row in matrix:
        for element in row:
            isnum(element)


def test_matrices(matrix1: List[List[Union[int, float, complex]]], 
                  matrix2: List[List[Union[int, float, complex]]]) -> None:
    """Checks compatibility and validity of two matrices for multiplication.

    Parameters:
    matrix1(List[List[Union[int, float, complex]]]): The first matrix.
    matrix2(List[List[Union[int, float, complex]]]): The second matrix.

    Returns:
    None

    This function checks whether the matrices are valid and compatible for multiplication. 
    Raises a ValueError if they are not.
    """

    check_validity(matrix1)  # Checking for uniform rows and columns, non-numeric elements
    check_validity(matrix2)

    if not matrix_shape(matrix1)[1] == matrix_shape(matrix2)[0]:
        # Checking for shape compatibility and empty matrices
        raise ValueError


def init_result(rows: int, cols: int) -> List[List[int]]:
    """Initializes a result matrix with all elements set to zero.

    Parameters:
    rows(int): The number of rows in the result matrix.
    cols(int): The number of columns in the result matrix.

    Returns:
    List[List[int]]: A matrix of size `rows x cols` with all elements initialized to zero.
    """

    res = []
    for i in range(rows):
        row = [0 for j in range(cols)]
        res.append(row)

    return res


def multiply(matrix1: List[List[Union[int, float, complex]]], 
             matrix2: List[List[Union[int, float, complex]]]) -> List[List[Union[int, float, complex]]]:
    """Multiplies two matrices.

    Parameters:
    matrix1(List[List[Union[int, float, complex]]]): The first matrix.
    matrix2(List[List[Union[int, float, complex]]]): The second matrix.

    Returns:
    List[List[Union[int, float, complex]]]: The resulting matrix after multiplication.
    """

    result = init_result(matrix_shape(matrix1)[0], matrix_shape(matrix2)[1])

    for i in range(len(result)):
        for j in range(len(result[0])):
            tmp = 0
            for k in range(len(matrix1[0])):
                tmp += matrix1[i][k] * matrix2[k][j]
            result[i][j] = tmp

    return result


def matrix_multiply(matrix1: List[List[Union[int, float, complex]]], 
                    matrix2: List[List[Union[int, float, complex]]]) -> List[List[Union[int, float, complex]]]:
    """Performs matrix multiplication.

    Parameters:
    matrix1(List[List[Union[int, float, complex]]]): The first matrix.
    matrix2(List[List[Union[int, float, complex]]]): The second matrix.

    Returns:
    List[List[Union[int, float, complex]]]: The resulting matrix after multiplication.
    
    This function multiplies two matrices after validating them and returns the result.
    """

    test_matrices(matrix1, matrix2)  # Running the test function to check for compatibility and validity of the input matrices

    return multiply(matrix1, matrix2)
