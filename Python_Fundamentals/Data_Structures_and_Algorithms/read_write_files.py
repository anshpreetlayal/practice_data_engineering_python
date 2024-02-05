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


#creating a csv file
import csv

csv_file_path = 'example.csv'
data = [
    ['Name', 'Age', 'City'],
    ['John Doe', 25, 'New York'],
    ['Jane Smith', 30, 'Los Angeles'],
    ['Bob Johnson', 22, 'Chicago'],
    ['Alice Brown', 28, 'San Francisco'],
    ['Charlie White', 35, 'Seattle'],
    ['Eva Black', 29, 'Miami'],
]

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f"Content has been written to {csv_file_path}")

# Reading from a CSV file
import csv

csv_file_path = 'example.csv'
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_data = [row for row in csv_reader]
    print("CSV Data:", csv_data)










# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Read/Write Operations - read_write_files.py execution complete.")

# End of read_write_files.py file
