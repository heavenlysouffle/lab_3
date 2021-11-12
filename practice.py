import os
import random
import string
import timeit

with open("numbers.txt", "w") as input:
    letters = string.ascii_letters
    while os.stat("numbers.txt").st_size < 50000000:
        choice = random.randint(1, 3)
        if choice == 1:
            element = str(random.randint(0, 100))
        elif choice == 2:
            element = ""
            for i in range(1, random.randint(2, 7)):
                element += ''.join(random.choice(letters))
        else:
            element = str(round(random.uniform(1, 2), 3))
        input.write(element + "\n")

test = """
result = 0
with open("numbers.txt", "r") as read_file:
    output = read_file.readlines()
    for line in output:
        if line.strip().isdigit():
            result += int(line.strip())
"""
print(timeit.timeit(test, number=10))

test = """
result = 0
with open("numbers.txt", "r") as read_file:
    for line in read_file:
        if line.strip().isdigit():
            result += int(line.strip())
"""
print(timeit.timeit(test, number=10))

test = """
result = 0
with open("numbers.txt", "r") as read_file:
    numbers = (int(line.strip()) for line in read_file if line.strip().isdigit())
    result = sum(numbers)
"""
print(timeit.timeit(test, number=10))
