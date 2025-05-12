# practiced problems in gfg

# data structures in python 

# list
# A list is a collection of items that are ordered and changeable. Lists are written with square brackets
# Example:
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# # Accessing items in a list
# print(fruits[0]) # Output: apple
# print(fruits[1]) # Output: banana
# print(fruits[2]) # Output: cherry
# # Changing items in a list
# fruits[0] = "orange"
# print(fruits) # Output: ['orange', 'banana', 'cherry']
# # Adding items to a list
# fruits.append("grape")
# print(fruits) # Output: ['orange', 'banana', 'cherry', 'grape']
# # Removing items from a list
# fruits.remove("banana")
# print(fruits) # Output: ['orange', 'cherry', 'grape']
# # Looping through a list
# for fruit in fruits:
#     print(fruit)
# # Output: orange
# #         cherry
# #         grape


# # List methods
# fruits = ["apple", "banana", "cherry"]
# print(fruits) # Output: ['apple', 'banana', 'cherry']

# # Adding items to a list
# fruits.append("orange")
# print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']
# fruits.insert(1, "kiwi")
# print(fruits) # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']
# fruits.extend(["mango", "grape"])
# print(fruits) # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange', 'mango', 'grape']

# # Removing items from a list
# fruits.remove("banana")
# print(fruits) # Output: ['apple', 'kiwi', 'cherry', 'orange', 'mango', 'grape']
# fruits.pop()  
# print(fruits) # Output: ['apple', 'kiwi', 'cherry', 'orange', 'mango']
# fruits.clear()
# print(fruits) # Output: []
# fruits = ["apple", "banana", "cherry"]
# fruits.pop(1)
# print(fruits) # Output: ['apple', 'cherry']
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits) # Output: ['apple', 'cherry']

# # Sorting a list
# fruits = ["banana", "cherry", "apple"]
# fruits.sort()
# print(fruits) # Output: ['apple', 'banana', 'cherry']
# fruits.sort(reverse=True)
# print(fruits) # Output: ['cherry', 'banana', 'apple']
# fruits = ["banana", "cherry", "apple"]
# fruits.sort(key=len)
# print(fruits) # Output: ['banana', 'apple', 'cherry']
# fruits = ["banana", "cherry", "apple"]
# fruits.sort(key=len, reverse=True)
# print(fruits) # Output: ['banana', 'cherry', 'apple']
# fruits = ["banana", "cherry", "apple"]
# fruits.sort(key=str.lower)
# print(fruits) # Output: ['apple', 'banana', 'cherry']
# fruits = ["banana", "cherry", "apple"]
# fruits.sort(key=str.lower, reverse=True)
# print(fruits) # Output: ['cherry', 'banana', 'apple']
# fruits = ["banana", "cherry", "apple"]




# List comprehension
# List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses
# Example:
# squares = [x**2 for x in range(10)]
# print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# # List comprehension with if statement
# squares = [x**2 for x in range(10) if x % 2 == 0]
# print(squares) # Output: [0, 4, 16, 36, 64]


# # List comprehension with nested for loops
# squares = [x**2 for x in range(3) for y in range(3)]
# print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0]
# print(squares) # Output: [0, 4, 16]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
# print(squares) # Output: [0, 4, 16]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0 and x != y]
# print(squares) # Output: [0, 4, 16]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0 and x != y and x < y]
# print(squares) # Output: [0, 4, 16]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0 and x != y and x < y and x + y < 5]
# print(squares) # Output: [0, 4, 16]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0 and x != y and x < y and x + y < 5 and x - y > 0]
# print(squares) # Output: [0, 4, 16]

# # List comprehension with nested for loops and if statement
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0 and x != y and x < y and x + y < 5 and x - y > 0]
# print(squares) # Output: [0, 4, 16]
# squares = [x**2 for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0 and x != y and x < y and x + y < 5 and x - y > 0]
# print(squares) # Output: [0, 4, 16]


# Sets
# A set is a collection of items that are unordered and unindexed. Sets are written with curly brackets
# Example:
# fruits = {"apple", "banana", "cherry"}
# print(fruits)

# # Accessing items in a set
# print(fruits[0]) # Output: TypeError: 'set' object is not subscriptable

# # Adding items to a set
# fruits.add("orange")
# print(fruits) # Output: {'banana', 'cherry', 'orange', 'apple'}

# # Removing items from a set
# fruits.remove("banana")
# print(fruits) # Output: {'cherry', 'orange', 'apple'}

# # Looping through a set
# for fruit in fruits:
#     print(fruit)
# # Output: apple
# #         cherry
# #         orange

# # Set methods
# fruits = {"apple", "banana", "cherry"}
# print(fruits) # Output: {'banana', 'cherry', 'apple'}

# # Adding items to a set
# fruits.add("orange")
# print(fruits) # Output: {'banana', 'cherry', 'orange', 'apple'}
# fruits.update({"kiwi", "mango"})
# print(fruits) # Output: {'banana', 'cherry', 'orange', 'kiwi', 'mango', 'apple'}
# fruits.update(["grape", "pear"])
# print(fruits) # Output: {'banana', 'cherry', 'orange', 'kiwi', 'mango', 'apple', 'grape', 'pear'}

# # Removing items from a set
# fruits.remove("banana")
# print(fruits) # Output: {'cherry', 'orange', 'kiwi', 'mango', 'apple', 'grape', 'pear'}
# fruits.discard("banana")
# print(fruits) # Output: {'cherry', 'orange', 'kiwi', 'mango', 'apple', 'grape', 'pear'}
# fruits.pop()
# print(fruits) # Output: {'cherry', 'orange', 'kiwi', 'mango', 'apple', 'grape'}
# fruits.clear()
# print(fruits) # Output: set()
# fruits = {"apple", "banana", "cherry"}


# # Set operations
# fruits1 = {"apple", "banana", "cherry"}
# fruits2 = {"banana", "cherry", "orange"}

# # Union
# fruits3 = fruits1.union(fruits2)
# print(fruits3) # Output: {'banana', 'cherry', 'orange', 'apple'}

# # Intersection
# fruits3 = fruits1.intersection(fruits2)
# print(fruits3) # Output: {'banana', 'cherry'}

# # Difference
# fruits3 = fruits1.difference(fruits2)
# print(fruits3) # Output: {'apple'}
# fruits3 = fruits2.difference(fruits1)
# print(fruits3) # Output: {'orange'}

# # Symmetric difference
# fruits3 = fruits1.symmetric_difference(fruits2)
# print(fruits3) # Output: {'orange', 'apple'}
# fruits3 = fruits2.symmetric_difference(fruits1)
# print(fruits3) # Output: {'orange', 'apple'}

# # Set comprehension
# fruits = {x**2 for x in range(10)}
# print(fruits) # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# fruits = {x**2 for x in range(10) if x % 2 == 0}
# print(fruits) # Output: {0, 4, 16, 36, 64}
# fruits = {x**2 for x in range(10) if x % 2 == 0 and x > 5}
# print(fruits) # Output: {64, 36, 16, 4, 0}
# fruits = {x**2 for x in range(10) if x % 2 == 0 and x > 5 and x < 8}
# print(fruits) # Output: {64, 36, 16, 4, 0}
# fruits = {x**2 for x in range(10) if x % 2 == 0 and x > 5 and x < 8 and x != 6}
# print(fruits) # Output: {64, 36, 16, 4, 0}
# fruits = {x**2 for x in range(10) if x % 2 == 0 and x > 5 and x < 8 and x != 6 and x != 7}
# print(fruits) # Output: {64, 36, 16, 4, 0}


