"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
import typing
"""
import typing
class MyYException(Exception):
    def __init__(self, message):
        self.message = message

def division(x: int, y: int):
    if y == 0:
        print("Division by 0")
        print("Division finished")
        return None
    elif y == 1:
        raise MyYException("Deletion on 1 get the same result")
    else:
        print("Division finished")
        return x/y

try:
    division(1, 0)
except MyYException as e:
    print(f"{e.message}\nDivision finished\n")

try:
    division(1, 1)
except MyYException as e:
    print(f"{e.message}\nDivision finished\n")

try:
    division(2, 2)
except MyYException as e:
    print(f"{e.message}\nDivision finished\n")