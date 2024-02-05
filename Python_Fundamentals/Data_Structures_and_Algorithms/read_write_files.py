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


# Creating a JSON file 
import json

json_file_path = 'example.json'
data = {
    "people": [
        {"name": "John Doe", "age": 25, "city": "New York"},
        {"name": "Jane Smith", "age": 30, "city": "Los Angeles"},
        {"name": "Bob Johnson", "age": 22, "city": "Chicago"},
        {"name": "Alice Brown", "age": 28, "city": "San Francisco"},
        {"name": "Charlie White", "age": 35, "city": "Seattle"},
        {"name": "Eva Black", "age": 29, "city": "Miami"},
        {"name": "David Green", "age": 32, "city": "Dallas"},
        {"name": "Grace Taylor", "age": 27, "city": "Boston"},
        {"name": "Frank Miller", "age": 40, "city": "Denver"}
    ]
}

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Content has been written to {json_file_path}")


# Reading from a JSON file
import json

json_file_path = 'example.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    print("JSON Data:", json_data)


# Creating the binary file
# Generating and Writing Data into a binary file
binary_generated_data = b'\x48\x65\x6C\x6C\x6F\x2C\x20\x74\x68\x69\x73\x20\x69\x73\x20\x61\x20\x62\x69\x6E\x61\x72\x79\x20\x66\x69\x6C\x65\x2E'

with open('generated_data.bin', 'wb') as binary_generated_file:
    binary_generated_file.write(binary_generated_data)

# Reading from the binary file
with open('generated_data.bin', 'rb') as binary_generated_file:
    binary_generated_content = binary_generated_file.read()
    print("Binary File Content:", binary_generated_content)


# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Read/Write Operations - read_write_files.py execution complete.")

# End of read_write_files.py file
