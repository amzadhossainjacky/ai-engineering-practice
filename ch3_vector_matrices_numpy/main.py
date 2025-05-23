import numpy as np
#matrices
#[] 1d, [[]] 2d, [[[]]] 3d


""" In NumPy, all arrays, including vectors (1D arrays), do have a shape.

    A 1D vector like np.array([2, 4, 5]) has a shape of (3,), meaning it has 1 dimension with 3 elements.

    A 2D matrix like np.array([[2, 4, 5]]) has a shape of (1, 3) — 1 row and 3 columns.

    A 3D array has a shape like (1, 1, 3), and so on.
    meaning:
    [
        [  # 1st block (axis 0)
            [1, 2, 3]  # 1 row (axis 1) with 3 columns (axis 2)
        ]
    ]
 """
#random vector example
""" vector_example = np.array([2,4,5])
print(f"vector example: {vector_example}")
# 1D vector has shape (3,)
print(f"Shape: {vector_example.shape}") """


#random matrices, matrices_example1 
""" matrices_example1 = [
    [2,4,5],
    [2,4,5,1,9],
    [7,1],
    [5,1, 3, 2]
]

matrices_example1_result = np.array(matrices_example1, dtype=object)
#[list([2, 4, 5]) list([2, 4, 5, 1, 9]) list([7, 1]) list([5, 1, 3, 2])] 
# print because dtype=object tells NumPy: "Don't try to convert the data into a uniform type—just store it as-is, as generic Python objects 
print(f"matrices example: {matrices_example1_result}")
#(not equal shape, row column wise)
print(f"matrices shape: {matrices_example1_result.shape}") """

#random matrices, matrices_example2
""" matrices_example2 = [
    [2,4,5],
    [2,4,5],
    [7,1,6],
    [5,1, 3]
]

arr = np.array(matrices_example2, dtype=object)
print(f"matrices example: {arr}")
print(f"matrices shape: {arr.shape}") """



#vector addition
# vector_a = np.array([2,4,6])
# vector_b = np.array([4,7])
# vector_c = np.array([4])
# vector_d = np.array([4,6])
# #not possible, row column not match
# # vector_sum = vector_a + vector_b
# # print(f"Vector sum: {vector_sum}")

# #its possible in nympy but not actual possible in math addition
# #In NumPy, [2, 4, 6] + 4 is valid. beacuse of braodcasting, Imagine writing 4 as [4, 4, 4] implicitly — NumPy does this.
# vector_sum2 = vector_a + vector_c
# print(f"Vector sum: {vector_sum2}")

# vector_sum3 = vector_b + vector_d
# print(f"Vector sum: {vector_sum3}")

#vector multiply
#Element-wise product
""" vector_a = np.array([4,7])
vector_b = np.array([4,9])
vector_c = np.array([4])

#this vector multiplication, not matrics so possible
vector_cross = vector_a * vector_b
print(f"cross: {vector_cross}")

#This also works because of broadcasting again!
vector_cross2 = vector_b * vector_c
print(f"cross2: {vector_cross2}") """


#dot product vector
#result in scaler value not array form
""" v_a = np.array([4,7])
v_b = np.array([4,9])
dot_vector = np.dot(v_a, v_b)

#this not possible in dot product
# v_a = np.array([4,7])
# v_b = np.array([4,9,8])
# dot_vector = np.dot(v_a, v_b)

print(dot_vector) """






#matrices addition
""" matrices_a = np.array([
    [1,2,3],
    [4,5,6]
])

matrices_b = np.array([
    [7,8,9],
    [10,11,12]
])

#should be same matrices otherwise get an error
matrices_sum = matrices_a + matrices_b
print(f"matrices sum: {matrices_sum}") """

#matrices multiplication
""" matrices_a = np.array([
    [1,2],
    [3,4]
])

matrices_b = np.array([
    [5,6],
    [7,8]
])

#should be same matrices otherwise get an error
#Element-wise multiplication
matrices_multiplication = matrices_a * matrices_b
print(f"matrices multiplication: {matrices_multiplication}")

#matrix multiplication and dot product same, actual same as math
matrices_multiplication_dot = np.dot(matrices_a, matrices_b)
print(f"matrices multiplication dot: {matrices_multiplication_dot}") """