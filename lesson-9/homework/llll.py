import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
✅ 2. Person Class

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):  # dob format: 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, '%Y-%m-%d')

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

# Example
p = Person("Alice", "Uzbekistan", "2000-05-14")
print("Age:", p.age())
✅ 3. Calculator Class

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Cannot divide by zero"

# Example
calc = Calculator()
print("Add:", calc.add(4, 5))
print("Divide:", calc.divide(10, 2))
✅ 4. Shape and Subclasses

import math

class Shape:
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

# Example
sq = Square(4)
print("Square Area:", sq.area())
tr = Triangle(3, 4, 5)
print("Triangle Area:", tr.area())
✅ 5. Binary Search Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node: return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(node, key):
            if not node: return False
            if key == node.key: return True
            return _search(node.left, key) if key < node.key else _search(node.right, key)
        return _search(self.root, key)

# Example
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print("Search 15:", bst.search(15))
✅ 6. Stack Class
python
Копировать код
class Stack:
    def __init__(self): self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def is_empty(self): return len(self.items) == 0

# Example
s = Stack()
s.push(10)
print("Pop:", s.pop())
✅ 7. Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example
ll = LinkedList()
ll.insert(3)
ll.insert(5)
ll.display()
ll.delete(5)
ll.display()
✅ 8. Shopping Cart

class ShoppingCart:
    def __init__(self): self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items: del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# Example
cart = ShoppingCart()
cart.add_item("Book", 12.99)
cart.add_item("Pen", 1.50)
print("Total:", cart.total_price())
cart.remove_item("Pen")
✅ 9. Stack with Display

class Stack:
    def __init__(self): self.stack = []

    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else None
    def display(self): print("Stack:", self.stack)

# Example
s = Stack()
s.push(1)
s.push(2)
s.display()
✅ 10. Queue Data Structure

class Queue:
    def __init__(self): self.queue = []

    def enqueue(self, item): self.queue.append(item)
    def dequeue(self): return self.queue.pop(0) if self.queue else None
    def display(self): print("Queue:", self.queue)

# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.display()
print("Dequeued:", q.dequeue())
✅ 11. Bank Class

class Bank:
    def __init__(self):
        self.accounts = {}  # key: name, value: balance

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            print("Insufficient funds or account not found.")

    def get_balance(self, name):
        return self.accounts.get(name, "Account not found")

# Example
b = Bank()
b.create_account("Ali", 100)
b.deposit("Ali", 50)
b.withdraw("Ali", 30)
print("Balance:", b.get_balance("Ali"))
