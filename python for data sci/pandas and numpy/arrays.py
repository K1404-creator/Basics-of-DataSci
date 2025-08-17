import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)


#matrix: 2d array

matrix = np.array([[1,2,4], [3, 4, 5]])
print(matrix)

# Adding two arrays
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

sum_array = array1 + array2
print(sum_array)
difference_array = array1 - array2
print(difference_array)
product_array = array1 * array2
print(product_array)
div_array = array1 / array2
print(div_array)


#Broadcasting example
scalar = 10
broadcasted_array = array1 + scalar
print(broadcasted_array)