# =======================================
#      Regular Expression Extraction
# =======================================

# Python Fundamentals for Data Engineering
# regex_extraction.py: Utilizes regular expressions for string manipulation.

# Importing necessary libraries
import re

# Function to extract data using regex
def extract_data_with_regex(pattern, text):
    """
    Extracts data from a text using a specified regular expression pattern.

    Parameters:
    - pattern (str): The regular expression pattern to match.
    - text (str): The input text from which to extract data.

    Returns:
    - str or None: The extracted data if a match is found, or None otherwise.
    """
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None
    
# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("Regular Expression Extraction - regex_extraction.py execution complete.")

# End of regex_extraction.py file
