# Task 4 - Python
from typing import List
import copy

def calculate_power_with_difference(ints: List[int]):
    copy_ints = copy.deepcopy(ints)         # create deep copy of ints
    copy_ints[0] = ints[0] ** 2             # calculate first element
    for i in range(len(ints)-1):
        copy_ints[i+1] = ints[i+1] ** 2 - copy_ints[i] + ints[i]
    return copy_ints

# TESTS
print(calculate_power_with_difference([1, 2, 3]))
