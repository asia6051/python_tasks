
# ------------ TASK READ WRITE -----------------------------
"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import os
from python_3.taski import read_write


def test_read_write():
    directory = 'test_folder'

    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w') as f2:
        f2.write('cd')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f1:
        f1.write('ab')

    result = ""
    result_file = 'result.txt'
    read_write(directory, result_file)

    with open(result_file, 'r') as file:
        result = file.read()

    assert result == 'ab, cd, '

# --------------- TASK READ WRITE 2 -------------------------
"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
from python_3.taski import read_write_2

def test_f():
    words = ('abc', 'def', 'xyz')
    read_write_2(words)
    with open("utf8.txt", 'r', encoding = "UTF-8") as file1:
        f1 = file1.read()

    with open("CP1252.txt", 'r', encoding = "CP1252") as file2:
        f2 = file2.read()

    assert f1 == 'abc\ndef\nxyz', "UTF-8 File works wrong"
    assert f2 == 'xyz, def, abc', "CP1252 File works wrong"

# --------------- TASK CLASSES -------------------------------
"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import pytest
from python_3.taski import Teacher, Student, Homework
from datetime import timedelta


@pytest.fixture
def teacher():
    return Teacher("Albus", "Dumbledore")


@pytest.fixture
def student():
    return Student("Harry", "Potter")


@pytest.fixture
def homework_active():
    return Homework("abc", 3)


@pytest.fixture
def homework_inactive():
    return Homework("xyz", 0)


def test_create_homework(teacher):
    text = "Test"
    deadline = 4

    test_homework = teacher.create_homework(text, deadline)

    assert isinstance(test_homework, Homework), "Homework object was not created"
    assert test_homework.text == text, "Homework text not assigned properly"
    assert test_homework.deadline == timedelta(days=deadline), "Homework deadline not assigned properly"


def test_create_expired_homework(teacher):
    text = "Test2"
    deadline = -1

    test_homework = teacher.create_homework(text, deadline)

    assert not isinstance(test_homework, Homework), "Overdue homework creation"


def test_is_active(homework_active):
    assert homework_active.is_active(), "Active homework recognized as overdue"


def test_is_inactive(homework_inactive):
    assert not homework_inactive.is_active(), "Overdue homework recognized as active"


def test_do_active_homework(student, homework_active):
    assert student.do_homework(homework_active) == str(homework_active), "Active homework wasn't done"


def test_do_inactive_homework(student, homework_inactive):
    assert student.do_homework(homework_inactive) is None, "Inactive homework was done"


def test_create_homework_bad_type(teacher):
    text = 12.7
    deadline = 5

    with pytest.raises(TypeError, match="Task must be a string"):
        teacher.create_homework(text, deadline)


# ----------------------- TASK EXCEPTIONS --------------------------
"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest
from python_3.taski import MyYException, division

divisions = [
    (2, 2, 1),
    (10, 5, 2),
    (5, 2, 2.5),
    (-10, 4, -2.5),
    (20, -8, -2.5)
]


@pytest.mark.parametrize('x, y, result', divisions)
def test_division_ok(x, y, result):
    assert x / y == result


def test_division_by_zero(capfd):
    division(1, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\nDivision finished\n", "Wrong communicates after 0 division"
    assert division(1,0) is None, "Division by 0 didn't return None"


def test_division_by_one():
    with pytest.raises(MyYException, match="Deletion on 1 get the same result"):
        division(1,1)


# --------------------- TASK INPUT OUTPUT -----------------------------
"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch
from python_3.taski import read_numbers


def test_read_numbers_only():
    inputs = ['1', '2', '3', '4', '5']
    with patch('builtins.input', side_effect=inputs):
        answer = read_numbers(5)
        assert answer == 'Avg: 3.00'


def test_read_numbers_and_words():
    inputs = ['1', '2', 'hello', '2', 'world']
    with patch('builtins.input', side_effect=inputs):
        answer = read_numbers(5)
        assert answer == 'Avg: 1.67'


def test_read_words_only():
    inputs = ['hello', 'world', 'foo', 'bar', 'baz']
    with patch('builtins.input', side_effect=inputs):
        answer = read_numbers(5)
        assert answer == "No numbers entered"


# -------------------- TASK PARAMETRIZE -----------------------------
"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""
import pytest

fib_numbers = [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
]
# Functions


def fibonacci_1(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_2(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]

# TESTS


@pytest.mark.parametrize('n, fib', fib_numbers)
def test_fibonacci_1(n, fib):
    assert fibonacci_1(n) == fib


@pytest.mark.parametrize('n, fib', fib_numbers)
def test_fibonacci_2(n, fib):
    assert fibonacci_2(n) == fib









