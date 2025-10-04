def insert_underscore(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0
    count = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            if (i + 1 < len(txt)) and (txt[i + 1] in vowels or txt[i + 1] == "_"):
                # shift the underscore forward
                if i + 2 < len(txt):
                    result.append(txt[i + 1])
                    result.append("_")
                    i += 1
            else:
                if i + 1 < len(txt):  # Don't add at end
                    result.append("_")
            count = 0
        i += 1

    return "".join(result)

# ✅ Examples
print(insert_underscore("hello"))              # hel_lo
print(insert_underscore("assalom"))            # ass_alom
print(insert_underscore("abcabcabcdeabcdefabcdefg"))  # abc_abcab_cdeabcd_efabcdef_g
🔹 2. Integer Squares Exercise

n = int(input("Enter n: "))
for i in range(n):
    print(i ** 2)
🔹 3. Loop-Based Exercises
Exercise 1: First 10 Natural Numbers using while

i = 1
while i <= 10:
    print(i)
    i += 1
Exercise 2: Print Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
Exercise 3: Sum from 1 to n
n = int(input("Enter number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum is:", total)
Exercise 4: Multiplication Table

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)
Exercise 5: Display Specific Numbers from List

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 > num > 70:
        print(num)
Exercise 6: Count Digits in a Number

num = input("Enter a number: ")
print("Number of digits:", len(num))
Exercise 7: Reverse Number Pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
Exercise 8: Reverse a List Using Loop

list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)
Exercise 9: Display -10 to -1

for i in range(-10, 0):
    print(i)
Exercise 10: Display “Done” after Loop

for i in range(5):
    print(i)
else:
    print("Done!")
Exercise 11: Print All Primes Between Two Numbers

start, end = 25, 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
Exercise 12: Fibonacci Series (10 Terms)

a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
Exercise 13: Factorial of a Number

n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")
🔹 4. Return Uncommon Elements of Lists
✅ Supports duplicates:

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
    return result

# ✅ Examples
print(uncommon_elements([1, 1, 2], [2, 3, 4]))           # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))           # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
