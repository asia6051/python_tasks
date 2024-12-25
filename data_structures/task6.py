# TASK 6 - Python Basics
def get_min_max(filename: str):
    mini = float('inf')
    maxi = float('-inf')
    with open(filename) as opened_file:
        for line in opened_file:
            mini = min(mini, int(line))
            maxi = max(maxi, int(line))
    result = (mini, maxi)
    return result

# TESTS
print(get_min_max('../.venv/task6_test.txt'))