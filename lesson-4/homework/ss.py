my_dict = {'a': 3, 'b': 1, 'c': 2}

# Ascending
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)

# Descending
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)
2. Add a Key to a Dictionary

d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)
3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print("Merged dictionary:", merged_dict)
4. Generate a Dictionary with Squares (1 to n)

n = 5
squares = {x: x*x for x in range(1, n+1)}
print("Dictionary of squares:", squares)
5. Dictionary of Squares (1 to 15)

squares_15 = {x: x**2 for x in range(1, 16)}
print("1 to 15 squares:", squares_15)
🔹 Set Exercises
1. Create a Set

my_set = {"apple", "banana", "cherry"}
print("Created set:", my_set)
2. Iterate Over a Set

for item in my_set:
    print(item)
3. Add Member(s) to a Set

my_set.add("orange")
# Add multiple items
my_set.update(["grape", "melon"])
print("After adding:", my_set)
4. Remove Item(s) from a Set

my_set.discard("banana")  # No error if item not found
print("After discarding 'banana':", my_set)

# Alternatively use remove (throws error if not found)
# my_set.remove("apple")
5. Remove an Item if Present in the Set

item_to_remove = "apple"
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"Removed '{item_to_remove}':", my_set)
else:
    print(f"'{item_to_remove}' not in set.")
