import numpy as np
# Matrix A
A = np.array([
    [ 1 , 2],
    [ 3 , 4]
])
# Matrix B
B = np.array([
    [ 5 , 6],
    [ 7  , 8]
])

# Showing Matrix A
print("\nMatrix A: ", A)

# Showing Matrix B 
print("\nMatrix B: " , B)

# Addition of Matrix A and B
print( "\nAddition of A and B: ", A+B)

# Subtraction of Matrix B from A
print("\nSubtraction of A and B: ", A - B)

# Subtraction of Matrix A from B
print("\nSubtraction of B and A: ", B - A)

# Multiplication of Matrix A and B

print("\nMultiplication of A and B:", A  @  B)

# Transpose of Matrix A
print("\nTranspose of Matrix A: " , A.T)

# Transpose of Matrix B
print("\nTranspose of Matrix B: ", B.T)

# Determinant of Matrix A 
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Determinant of Matrix B 
print("\nDeterminant of B:")
print(np.linalg.det(B))

# Inverse of Matrix A
print("\nInverse of A:")
print(np.linalg.inv(A))

# Inverse of Matrix B
print("\nInverse of B:")
print(np.linalg.inv(B))