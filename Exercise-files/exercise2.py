import urllib.request, urllib.parse, urllib.error
import json

# Prompt
url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1818138.json'

# Read the JSON data from the URL
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Parse the JSON data
info = json.loads(data)
comments = info['comments']
sum_counts = sum(int(comment['count']) for comment in comments)

# Output
print('Sum:', sum_counts)
