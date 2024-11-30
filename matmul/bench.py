import time
import numpy as np
import random
from matmul_correct import matrix_multiply

def generate_random_matrix(rows, cols):
    """Generate a random matrix with the given number of rows and columns."""
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def time_function(func, *args, repeats=5):
    """Times a function by running it multiple times and averaging the time taken."""
    total_time = 0.0
    for _ in range(repeats):
        start_time = time.time()
        func(*args)
        total_time += time.time() - start_time
    return total_time / repeats

def calculate_flops(m, n, p, time_taken):
    """Calculate the effective FLOPS for a matrix multiplication."""
    # The number of floating-point operations for m x n * n x p is 2 * m * n * p
    operations = 2 * m * n * p
    flops = operations / time_taken
    return flops

def benchmark_matrix_multiply(sizes, repeats=5):
    """Benchmark the custom matrix_multiply function against NumPy's matrix multiplication."""
    for size in sizes:
        rows, cols = size

        # Generate two random matrices of the given size
        mat1 = generate_random_matrix(rows, cols)
        mat2 = generate_random_matrix(cols, rows)  # Ensure mat2 is of compatible size

        # Benchmark the custom matrix_multiply function
        custom_time = time_function(matrix_multiply, mat1, mat2, repeats=repeats)
        custom_flops = calculate_flops(rows, cols, rows, custom_time)/1e6

        # Convert matrices to numpy arrays
        np_mat1 = np.array(mat1)
        np_mat2 = np.array(mat2)

        # Benchmark NumPy's matrix multiplication
        numpy_time = time_function(np.dot, np_mat1, np_mat2, repeats=repeats)
        numpy_flops = calculate_flops(rows, cols, rows, numpy_time)/1e6

        # Compare the results (sanity check)
        result_custom = matrix_multiply(mat1, mat2)
        result_numpy = np.dot(np_mat1, np_mat2)
        assert np.allclose(result_custom, result_numpy.tolist()), "Results do not match!"

        print(f"Matrix size: {rows}x{cols} multiplied by {cols}x{rows}")
        print(f"Custom function average time: {custom_time:.6f} seconds over {repeats} runs")
        print(f"Custom function FLOPS: {custom_flops:}")
        print(f"NumPy function average time: {numpy_time:.6f} seconds over {repeats} runs")
        print(f"NumPy function FLOPS: {numpy_flops:}")
        print("-" * 40)

if __name__ == "__main__":
    # Define matrix sizes for benchmarking
    matrix_sizes = [
        (10, 10),
        (50, 50),
        (100, 100),
        (200, 200)
    ]
    
    benchmark_matrix_multiply(matrix_sizes, repeats=5)

