# Task 2 - Python Basics
from typing import Dict

def set_to_dict(dict_to_update: Dict[str, int], **items_to_set):
    for key, value in items_to_set.items():
        if key not in dict_to_update.keys():  # new key occurred
            dict_to_update[key] = value       # create new key : value pair

        elif(dict_to_update[key] < value):  # key already exists
            dict_to_update[key] = value     # update value

    return dict_to_update

# TESTS
print(set_to_dict({'a' : 1, 'b' : 2, 'c' : 3}, a = 0, b=4))
print(set_to_dict({}, a = 0))
print(set_to_dict({'a' : 5}))