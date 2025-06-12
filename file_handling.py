# import os


# print(os.getcwd())  # Prints the current working directory


# # file = open('example.txt', 'r')

# # content = file.read()
# # file.close()

# # print(content)

# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# # The above code opens a file named 'example.txt' in read mode, reads its content line by line,
# # and prints each line after stripping any leading or trailing whitespace characters.
# # The 'with' statement ensures that the file is properly closed after its suite finishes, even if an error is raised.
# # This is a more efficient way to handle files in Python, as it automatically manages file closing.
# # The 'strip()' method is used to remove any leading or trailing whitespace characters from each line.
# # This code snippet demonstrates how to read a file line by line and print each line without leading or trailing whitespace.



# # file = open('example2.txt', 'a')

# # file.write('car\n')
# # file.close()


# with open('example2.txt', 'a') as file:
#     file.write('car\n')
#     # The 'a' mode opens the file for appending, meaning new data will be added to the end of the file.
#     # If the file does not exist, it will be created.
#     # The 'write' method writes a string to the file.
#     # After writing, the file is automatically closed when exiting the 'with' block.

# A = ['SAI \n', 'BMW \n', 'AUDI \n']

# with open('example2.txt', 'a') as file:
#     file.writelines(A)


# data = b'\x00\x01\x02'

# with open('example.bin', 'wb') as file:

#     file.write(data)


# with open('example.bin', 'rb') as file:

#     content = file.read()

#     print(content)

# The above code writes binary data to a file named 'example.bin' in write-binary mode ('wb').
# It then reads the content of the file in read-binary mode ('rb') and prints it.
# The 'wb' mode is used for writing binary files, while 'rb' is used for reading binary files.
# The 'b' in the mode stands for binary, indicating that the file will be treated as a binary file.
# The 'write' method writes the binary data to the file, and the 'read' method reads the entire content of the file.
# The 'print' function outputs the content read from the file, which will be in bytes format.
# The code demonstrates how to handle binary files in Python.





'''
with open("example.txt", "r") as source_file:
    content = source_file.read()

with open("destination.txt", 'w') as destination_file:
    destination_file.write(content)
    '''


# The above code copies the content of 'example.txt' to 'destination.txt'.
# It opens 'example.txt' in read mode and reads its entire content into the variable 'content'.
# Then, it opens 'destination.txt' in write mode and writes the content to it.
# This effectively creates a copy of the original file.




def count_text_files(file_path):

    with open(file_path, 'r') as file:

        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

    return line_count, word_count, char_count


file_path = 'example.txt'
lines , words, characters = count_text_files(file_path)
print(f"Lines: {lines}, Words: {words}, Characters: {characters}") 
