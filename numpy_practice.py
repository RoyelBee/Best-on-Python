# Create 2 new lists height and weight
height = [1, 2, 3]
weight = [4, 5, 6]

# print(type(height))
# print(type(weight))

# Import the numpy package as np
import numpy as np

# Convert array yo Numpy array
np_height = np.array(height)
np_weight = np.array(weight)
# print(type(np_height))
# print(np_weight)

# Marge two numpy array
all = np.concatenate((np_height, np_weight), axis=None)
# print(all)
# print(all.shape)
# print(all.dtype)
#

# Create random size array

data = np.arange((50000))
# print(data)

# Checks how much it will take to compute
import timeit as t

# a = t.timeit(str(range(1)), number=1000)
# print(a)

# Create random dataset

# Data Start from 2 emd in 9 . and increase by 1
data = np.arange(2, 10, 1)
# print(data)

# Create 3*3 zero dataset
# print(np.zeros((3, 3)))

# Create 3*2 dataset with value = 1
# print(np.ones((3, 2)))

# Create diagonal array with value = 1, except = 0
# print(np.eye(10))

# Diagonal array with different values
# print(np.diag([1, 2, 3, 4, 5]))

# Create full 3*3 dataset with values = 5
# print(np.full((3, 3), 5))

# create 5*4 random array with random value
random_data = np.random.random([5, 4])
# print(random_data)

# Random value with fixed range
# 100 Numbers between 10 to 20
print(np.linspace(10, 20, 100))


