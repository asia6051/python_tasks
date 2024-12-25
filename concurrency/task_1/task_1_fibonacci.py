from concurrent.futures import ProcessPoolExecutor
import os
import csv


def clean_csv_file(filename: str):
    with open(filename, 'w', newline='') as csv_f:
        pass


def first_function(n: int):
    filename = "files/{}.txt"
    f0, f1 = 0, 1
    for _ in range(0, n):
        f0, f1 = f1, (f1 + f0)

    with open(filename.format(n), 'w') as f:
        f.write(str(f0))


def second_function(filename: str):
    filepath = os.getcwd() + '/files/'+filename
    with open(filepath, 'r') as f:
        number = f.read()

    n = filename.replace('.txt', '')
    with open('result.csv', 'a', newline='') as csv_f:
        csvwriter = csv.writer(csv_f)
        csvwriter.writerow([n, number])


if __name__ == '__main__':
    clean_csv_file('result.csv')
    path = os.getcwd() + '/files'
    dirs = os.listdir(path)

    with ProcessPoolExecutor() as executor:
        numbers = [5, 1, 8, 10]
        executor.map(first_function, numbers)
        executor.map(second_function, dirs)
