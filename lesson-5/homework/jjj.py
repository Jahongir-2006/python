def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
✅ Example usage:

print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True
🔹 2. Conditional Statements Exercise
✅ Code:

n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:  # n > 20 and even
    print("Not Weird")
✅ Sample Run:
Input: 3
Output: Weird

🔹 3. Even Numbers Between Two Numbers (a and b inclusive)
We want two solutions without using a loop:

✅ Solution 1: Using if-else

def even_numbers_if_else(a, b):
    if a > b:
        a, b = b, a  # ensure a <= b
    # Use list comprehension to get even numbers
    return [x for x in range(a, b + 1) if x % 2 == 0]

# Example usage:
print(even_numbers_if_else(2, 10))  # [2, 4, 6, 8, 10]
✅ Solution 2: No if-else, using Python built-ins only

def even_numbers_no_if(a, b):
    a, b = min(a, b), max(a, b)
    # start from first even number, step by 2
    start = a if a % 2 == 0 else a + 1
    return list(range(start, b + 1, 2))

# Example usage:
print(even_numbers_no_if(2, 10))  # [2, 4, 6, 8, 10]
