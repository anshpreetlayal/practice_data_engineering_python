import urllib.request
from bs4 import BeautifulSoup

# Get the URL from the user
url = input("Enter URL: ")

# Fetch the HTML content from the URL using urllib
with urllib.request.urlopen(url) as response:
    html_content = response.read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
span_tags = soup.find_all('span', class_='comments')
count = 0
total_sum = 0

# Loop through each <span> tag
for span_tag in span_tags:
    comment_count = int(span_tag.text)
    count += 1
    total_sum += comment_count

# Print the count and sum
print("Count:", count)
print("Sum:", total_sum)
