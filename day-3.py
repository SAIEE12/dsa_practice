# while loops
# while loops are used to execute a block of code as long as a condition is true
# while condition:
#     # code to be executed
#
# Example:
# a = 0
# while a < 5:
#     print(a)
#     a += 1
#
# for loops
# for loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects
# for variable in sequence:
#     # code to be executed
#
# Example:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# break statement
# The break statement is used to exit a loop prematurely. It can be used in both while and for loops
# Example:
# a = 0
# while a < 5:
#     if a == 3:
#         break
#     print(a)
#     a += 1
#
# continue statement
# The continue statement is used to skip the current iteration of a loop and move to the next iteration. It can be used in both while and for loops
# Example:
# a = 0
# while a < 5:              
#     a += 1
#     if a == 3:
#         continue
#     print(a)
#
# pass statement
# The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in loops, functions, classes, or conditionals where code will eventually go but is not yet implemented
# Example:

# a = 0
# while a < 5:
#     a += 1
#     if a == 3:
#         pass
#     print(a)
#
# # range() function
# The range() function is used to generate a sequence of numbers. It can be used in for loops to iterate over a sequence of numbers
# Example:
# for i in range(5):
#     print(i)
#
# # The range() function can also take a start and end value, as well as a step value
# Example:
# for i in range(1, 10, 2):
#     print(i)
#
# # The range() function can also be used to create a list of numbers
# Example:
# numbers = list(range(1, 10, 2))
# print(numbers)    
