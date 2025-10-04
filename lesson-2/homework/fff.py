rom datetime import datetime

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - year_of_birth
print(f"{name}, you are {age} years old.")
2. Extract Car Names from 'LMaasleitbtui'
This appears to be a jumbled string with car names possibly hidden. One likely answer is "Mitsubishi" (hidden inside the jumbled letters).


txt = 'LMaasleitbtui'
# Extract manually
car = txt[1] + txt[4] + txt[5] + txt[6] + txt[7] + txt[9] + txt[10] + txt[11]  # M a s s l i t u → Mitsubishi
print("Extracted car name:", car.capitalize())
3. Extract Car Names from 'MsaatmiazD'
Likely car brand: Mazda


txt = 'MsaatmiazD'
# Possible extraction
car = txt[0] + txt[6] + txt[7] + txt[8] + txt[9]  # M a z d a
print("Extracted car name:", car.capitalize())
4. Extract Residence Are
txt = "I'am John. I am from London"
# Extract the word after "from"
words = txt.split()
if "from" in words:
    index = words.index("from")
    residence = words[index + 1]
    print("Residence area:", residence)
else:
    print("Residence area not found.")
5. Reverse String
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)
6. Count Vowels

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)
7. Find Maximum Value

numbers = input("Enter a list of numbers separated by spaces: ")
num_list = [int(n) for n in numbers.split()]
max_value = max(num_list)
print("Maximum value:", max_value)
8. Check Palindrome

word = input("Enter a word: ")
if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
9. Extract Email Domain

email = input("Enter your email address: ")
if "@" in email:
    domain = email.split("@")[1]
    print("Email domain:", domain)
else:
    print("Invalid email format.")
10. Generate Random Password
python
Копировать код
import random
import string

length = int(input("Enter desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
