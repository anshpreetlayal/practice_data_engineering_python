
'''
todo
-Write programs that read data from files (e.g., text, CSV, JSON) and manipulate it.
- Reading binary files using urllib
- Create scripts that generate and write data into files.'''

# =======================================
#      Read/Write Operations on Files
# =======================================
# Python Fundamentals for Data Engineering

# read_write_files.py: Covers reading from and writing to files.

# Writing to a text file
with open('example.txt', 'w') as file:
    file.write("Hello, this is an example file.")

# Reading from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:", content)



# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Read/Write Operations - read_write_files.py execution complete.")

# End of read_write_files.py file
