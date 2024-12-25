# ------------ TASK READ WRITE -----------------------------
"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os
directory = "files"
result_file = "result.txt"


def read_write(directory, result_file):
    result = ""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with open(filepath, 'r') as read_file:
                result = result + read_file.read() + ", "

    with open(result_file, 'w') as write_file:
        write_file.write(result)


# --------------- TASK READ WRITE 2 -------------------------
"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""

import string
import random


def generate_words(n=20):
    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


words = generate_words()


def read_write_2(words):
    with open("utf8.txt", 'w', encoding = "UTF-8") as file1:
        file1.write("\n".join(words))

    with open("CP1252.txt", 'w', encoding = "CP1252") as file2:
        file2.write(", ".join(words[::-1]))





# --------------- TASK CLASSES -------------------------------
from datetime import datetime, timedelta

class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text, deadline):
        if deadline < 0:
            print("You can't add expired homework\n")
        else:
            if not isinstance(text, str):
                raise TypeError("Task must be a string")
            else:
                homework = Homework(text, deadline)
                return homework

    def __str__(self):
        return(f"First name: {self.first_name}\n"
               f"Last name: {self.last_name}\n")

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            return str(homework)
        else:
            print("You are late")
            return None

    def __str__(self):
        return (f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n")

class Homework:
    def __init__(self, text, days_to_complete):
        self.text = text
        self.deadline = timedelta(days=days_to_complete)
        self.created = datetime.now()

    def is_active(self):
        """Checks, if homework is still active (not overdue)."""
        current_time = datetime.now()
        deadline_time = self.created + self.deadline
        return current_time <= deadline_time

    def __str__(self):
        return (f"Task: {self.text}\n"
                f"Created: {self.created.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Deadline: {self.deadline}\n")

if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    #teacher.last_name  # Daniil
    #student.first_name  # Petrov

    print(str(teacher))
    print(str(student))

    expired_homework = teacher.create_homework('Learn functions', 0)
    #expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    #expired_homework.deadline  # 0:00:00
    #expired_homework.text  # 'Learn functions'

    print(str(expired_homework))

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    #oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late



# ----------------------- TASK EXCEPTIONS --------------------------
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



# --------------------- TASK INPUT OUTPUT -----------------------------
"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    read_numbers(5)
    No numbers entered

"""
def read_numbers(n: int):
    numbers = list()
    while n:
        x = input()
        if x.isnumeric():
            numbers.append(float(x))
        n-=1
    if len(numbers) > 0:
        return f"Avg: {(sum(numbers) / len(numbers)):.2f}"
    else:
        return "No numbers entered"

print(read_numbers(5))


# -------------------- TASK PARAMETRIZE -----------------------------
# WSZYSTKO W TESTACH








