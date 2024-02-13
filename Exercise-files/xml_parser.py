import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1818137.xml'

# Read the XML data from the URL
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse the XML data
tree = ET.fromstring(data)

# Find all <count> elements
counts = tree.findall('.//count')

# Sum up the numbers
sum_counts = sum(int(count.text) for count in counts)

# Output the sum
print('Sum:', sum_counts)
