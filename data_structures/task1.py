# Task 1 - Python Basics
from typing import List, Any

def delete_from_list(list_to_clean: List, item_to_delete: Any):
    while item_to_delete in list_to_clean:          # while element still occurrs in list
        index = list_to_clean.index(item_to_delete) # find its index (first occurrence)
        list_to_clean.pop(index)                    # delete
    return list_to_clean

#TESTS
print(delete_from_list([1, 2, 3, 4, 3], 3))
print(delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b'))
print(delete_from_list([1, 2, 3], 'b'))
print(delete_from_list([], 'b'))