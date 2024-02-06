# =======================================
#      Working with XML Data
# =======================================

# Python Fundamentals for Data Engineering
# xml_processing.py: Demonstrates parsing and manipulating XML data.

# Importing necessary libraries
import xml.etree.ElementTree as ET

# Sample XML data
xml_data = '''
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
    <year>2003</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>
'''

# Parsing XML data
root = ET.fromstring(xml_data)

# Accessing elements and attributes
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    price = book.find('price').text
    category = book.get('category')

    print(f"Title: {title}, Author: {author}, Year: {year}, Price: {price}, Category: {category}")
