# line continuation
# In Python, you can use a backslash (\) to continue a statement on the next line.
# This is useful for long lines of code that you want to break up for readability.
# Example:
print("sai \
manish")


# Multiple statements on one line
# In Python, you can put multiple statements on the same line by separating them with a semicolon (;).
# Example:
print("sai"); print("manish")

#understand semantics
# In Python, indentation is used to define the structure of the code.
# For example, in a loop or a conditional statement, the code inside the block must be indented.
# Example:
for i in range(5):
    print(i)
    if i == 2:
        print("i is 2")
    else:
        print("i is not 2")
# In this example, the print statements inside the loop and the if statement are indented to show that they are part of the block.
# In Python, indentation is not just for readability; it is part of the syntax.
# This means that if you don't indent your code correctly, you will get a syntax error.
# Example:
# for i in range(5):
#     print(i)
#     if i == 2:
#         print("i is 2")
#     else:
#     print("i is not 2")  # This will cause a syntax error because the else statement is not indented correctly.
# In this example, the print statement inside the else block is not indented correctly, so it will cause a syntax error.




# data types
# In Python, there are several built-in data types that you can use to store and manipulate data.
# The most common data types are:
# 1. Integers: Whole numbers, positive or negative, without decimals.
# Example:
x = 5
y = -10
# 2. Floats: Numbers with decimal points.
# Example:
x = 5.5
y = -10.0       
# 3. Strings: A sequence of characters enclosed in quotes (single or double).
# Example:
x = "Hello, World!"
y = 'Python is awesome!'
# 4. Lists: An ordered collection of items, which can be of different data types.
# Example:
x = [1, 2, 3, 4, 5]
y = ["apple", "banana", "cherry"]
# 5. Tuples: An ordered collection of items, similar to lists, but immutable (cannot be changed).
# Example:
x = (1, 2, 3, 4, 5)
y = ("apple", "banana", "cherry")
# 6. Dictionaries: A collection of key-value pairs, where each key is unique.
# Example:
x = {"name": "John", "age": 30, "city": "New York"}
y = {"name": "Alice", "age": 25, "city": "Los Angeles"}
# 7. Sets: An unordered collection of unique items.
# Example:
x = {1, 2, 3, 4, 5}
y = {"apple", "banana", "cherry"}
# 8. Booleans: Represents True or False values.
# Example:
x = True
y = False
# 9. None: Represents the absence of a value or a null value.
# Example:
x = None
y = ""
# 10. Complex numbers: Numbers with a real and imaginary part.
# Example:
x = 3 + 4j
y = 2 - 3j




# Variables
# In Python, you can create variables to store data. A variable is a name that refers to a value.
# You can assign a value to a variable using the equals sign (=).
# Example:
x = 5
y = "Hello, World!"
# You can also change the value of a variable by assigning a new value to it.
# Example:
x = 10
y = "Python is awesome!"
# You can also create multiple variables in one line by separating them with commas.
# Example:
x, y, z = 1, 2, 3
# You can also create multiple variables with the same value in one line.
# Example:
x = y = z = 5
# You can also use the type() function to check the data type of a variable.
# Example:
x = 5
y = "Hello, World!"
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
# You can also use the id() function to check the memory address of a variable.
# Example:
x = 5
y = "Hello, World!"
print(id(x))  # Output: Memory address of x
print(id(y))  # Output: Memory address of y
# You can also use the dir() function to check the attributes and methods of a variable.
# Example:
x = 5
y = "Hello, World!"
print(dir(x))  # Output: List of attributes and methods of x
print(dir(y))  # Output: List of attributes and methods of y
# You can also use the help() function to get more information about a variable.
# Example:
x = 5
y = "Hello, World!"
print(help(x))  # Output: Help information about x
print(help(y))  # Output: Help information about y
# You can also use the globals() function to check the global variables in the current module.
# Example:
x = 5
y = "Hello, World!"
print(globals())  # Output: Dictionary of global variables in the current module
# You can also use the locals() function to check the local variables in the current scope.
# Example:
x = 5
y = "Hello, World!"
def my_function():
    z = 10
    print(locals())  # Output: Dictionary of local variables in the current scope
my_function()

# naming conventions
# In Python, there are some naming conventions that you should follow when creating variables and functions.
# 1. Use lowercase letters for variable names and function names.
# Example:
my_variable = 5
def my_function():
    pass
# 2. Use underscores (_) to separate words in variable names and function names.
# Example:
my_variable_name = 5
def my_function_name():
    pass
# 3. Use uppercase letters for class names.
# Example:
class MyClass:
    pass