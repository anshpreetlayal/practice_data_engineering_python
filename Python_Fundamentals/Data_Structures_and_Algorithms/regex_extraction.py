'''
todo:
Write scripts using regular expressions to extract specific patterns from strings.
Practice matching, searching, and replacing with regular expressions.
'''

# =======================================
#      Regular Expression Extraction
# =======================================

# Python Fundamentals for Data Engineering
# regex_extraction.py: Utilizes regular expressions for string manipulation.

# Importing necessary libraries
import re

# Function to extract data using regex
def extract_data_with_regex(pattern, text):
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

# Example usage
text_data = "Sample text with 123 and ABC"
pattern = r'\d+'
result = extract_data_with_regex(pattern, text_data)
print("Extracted Data:", result)

# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Regular Expression Extraction - regex_extraction.py execution complete.")

# End of regex_extraction.py file
