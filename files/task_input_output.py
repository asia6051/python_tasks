"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
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
        print(f"Avg: {(sum(numbers) / len(numbers)):.2f}")
    else:
        print("No numbers entered")

read_numbers(5)