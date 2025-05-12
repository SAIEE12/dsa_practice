# Dictionary
# dicttionary is a collection of key-value pairs
# Example:
# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# print(fruits) # Output: {'apple': 1, 'banana': 2, 'cherry': 3}
# # Accessing items in a dictionary
# print(fruits["apple"]) # Output: 1
# print(fruits["banana"]) # Output: 2
# print(fruits["cherry"]) # Output: 3
# # Changing items in a dictionary
# fruits["apple"] = 4
# print(fruits) # Output: {'apple': 4, 'banana': 2, 'cherry': 3}
# # Adding items to a dictionary
# fruits["orange"] = 5
# print(fruits) # Output: {'apple': 4, 'banana': 2, 'cherry': 3, 'orange': 5}
# # Removing items from a dictionary
# fruits.pop("banana")
# print(fruits) # Output: {'apple': 4, 'cherry': 3, 'orange': 5}
# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# # Looping through a dictionary
# for key in fruits:
#     print(key) # Output: apple
# #         banana
# #         cherry
# # Looping through a dictionary
# for key, value in fruits.items():
#     print(key, value) # Output: apple 1
# #         banana 2
# #         cherry 3

# # Dictionary methods
# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# print(fruits) # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

# # Adding items to a dictionary
# fruits["orange"] = 5
# print(fruits) # Output: {'apple': 1, 'banana': 2, 'cherry': 3, 'orange': 5}
# fruits.update({"kiwi": 6})
# print(fruits) # Output: {'apple': 1, 'banana': 2, 'cherry': 3, 'orange': 5, 'kiwi': 6}
# fruits.update({"banana": 4})
# print(fruits) # Output: {'apple': 1, 'banana': 4, 'cherry': 3, 'orange': 5, 'kiwi': 6}
# fruits.update({"banana": 4, "kiwi": 6})
# print(fruits) # Output: {'apple': 1, 'banana': 4, 'cherry': 3, 'orange': 5, 'kiwi': 6}
# fruits.update({"banana": 4, "kiwi": 6, "mango": 7})
# print(fruits) # Output: {'apple': 1, 'banana': 4, 'cherry': 3, 'orange': 5, 'kiwi': 6, 'mango': 7}
# fruits.update({"banana": 4, "kiwi": 6, "mango": 7, "grape": 8})   
# print(fruits) # Output: {'apple': 1, 'banana': 4, 'cherry': 3, 'orange': 5, 'kiwi': 6, 'mango': 7, 'grape': 8}

# # Removing items from a dictionary
# fruits.pop("banana")
# print(fruits) # Output: {'apple': 1, 'cherry': 3, 'orange': 5, 'kiwi': 6, 'mango': 7, 'grape': 8}
# fruits.popitem()
# print(fruits) # Output: {'apple': 1, 'cherry': 3, 'orange': 5, 'kiwi': 6, 'mango': 7}
# fruits.clear()
# print(fruits) # Output: {}
# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# fruits.pop("banana")
# print(fruits) # Output: {'apple': 1, 'cherry': 3}
# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# fruits.popitem()
# print(fruits) # Output: {'apple': 1, 'banana': 2}
# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# fruits.clear()
# print(fruits) # Output: {}
# fruits = {"apple": 1, "banana": 2, "cherry": 3}

