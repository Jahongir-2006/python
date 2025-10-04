try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
2. Raise ValueError for invalid integer
python
Копировать код
try:
    x = input("Enter an integer: ")
    if not x.isdigit():
        raise ValueError("Not a valid integer")
    print("You entered:", int(x))
except ValueError as e:
    print("Error:", e)
3. Handle FileNotFoundError
python
Копировать код
try:
    with open("testfile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")
4. Raise TypeError if inputs are not numerical
python
Копировать код
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numerical.")

    print("Sum =", float(a) + float(b))
except TypeError as e:
    print("Error:", e)
5. Handle PermissionError
python
Копировать код
try:
    with open("/etc/shadow", "r") as f:   # Example restricted file
        print(f.read())
except PermissionError:
    print("Error: Permission denied.")
6. Handle IndexError
python
Копировать код
try:
    lst = [10, 20, 30]
    print(lst[5])  # Out of range
except IndexError:
    print("Error: Index out of range.")
7. Handle KeyboardInterrupt
python
Копировать код
try:
    num = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nError: Input cancelled by user.")
8. Handle ArithmeticError
python
Копировать код
try:
    x = 10 / 0   # will raise ZeroDivisionError (a subclass of ArithmeticError)
except ArithmeticError as e:
    print("Arithmetic error occurred:", e)
9. Handle UnicodeDecodeError
python
Копировать код
try:
    with open("testfile.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Encoding issue while reading file.")
10. Handle AttributeError
python
Копировать код
try:
    lst = [1, 2, 3]
    lst.push(4)   # Wrong method
except AttributeError:
    print("Error: List object has no such attribute.")
📂 File Input/Output Programs
1. Read entire text file
python
Копировать код
with open("sample.txt", "r") as f:
    print(f.read())
2. Read first n lines
python
Копировать код
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")
3. Append text to a file
python
Копировать код
with open("sample.txt", "a") as f:
    f.write("\nNew line added.")
with open("sample.txt", "r") as f:
    print(f.read())
4. Read last n lines
python
Копировать код
n = 3
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))
5. Read file line by line into list
python
Копировать код
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)
6. Read file line by line into variable
python
Копировать код
text = ""
with open("sample.txt", "r") as f:
    for line in f:
        text += line
print(text)
7. Read file into array
python
Копировать код
arr = []
with open("sample.txt", "r") as f:
    for line in f:
        arr.append(line.strip())
print(arr)
8. Find longest words
python
Копировать код
with open("sample.txt", "r") as f:
    words = f.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
9. Count lines in a file
python
Копировать код
with open("sample.txt", "r") as f:
    print("Number of lines:", len(f.readlines()))
10. Count frequency of words
python
Копировать код
from collections import Counter

with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
count = Counter(words)
print(count)
11. Get file size
python
Копировать код
import os
print("File size:", os.path.getsize("sample.txt"), "bytes")
12. Write list to file
python
Копировать код
lst = ["Apple", "Banana", "Cherry"]
with open("list.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")
13. Copy contents of a file
python
Копировать код
with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
14. Combine lines from two files
python
Копировать код
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())
15. Read random line
python
Копировать код
import random
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(random.choice(lines))
16. Check if file is closed
python
Копировать код
f = open("sample.txt", "r")
print("Closed?", f.closed)
f.close()
print("Closed?", f.closed)
17. Remove newline characters
python
Копировать код
with open("sample.txt", "r") as f:
    lines = f.read().splitlines()
print(lines)
18. Count words in file
python
Копировать код
with open("sample.txt", "r") as f:
    text = f.read().replace(",", " ")
words = text.split()
print("Word count:", len(words))
19. Extract characters into list

chars = []
with open("sample.txt", "r") as f:
    for line in f:
        chars.extend(list(line.strip()))
print(chars)
20. Generate 26 text files (A.txt–Z.txt)

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")
21. File with alphabet letters

import string

n = 5  # letters per line
letters = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")
