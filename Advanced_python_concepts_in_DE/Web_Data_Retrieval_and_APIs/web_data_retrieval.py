# =======================================
#   Web Browsing Protocols and Data Retrieval
# =======================================

# Python Fundamentals for Data Engineering
# web_data_retrieval.py: Demonstrates making HTTP requests and handling responses.

# Importing necessary libraries
import requests

# ----------------------------------------------
# Making HTTP Requests and Handling Responses
# ----------------------------------------------

# Define the URL for the Cat Fact API
cat_fact_api_url = 'https://catfact.ninja/fact'

# Make a GET request to the Cat Fact API
response = requests.get(cat_fact_api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON data
    cat_fact_json = response.json()
    
    # Extract the cat fact from the JSON response
    cat_fact = cat_fact_json.get('fact')
    
    # Print the retrieved cat fact
    if cat_fact:
        print("Random Cat Fact:", cat_fact)
    else:
        print("No cat fact found in the response.")
else:
    print("Failed to retrieve cat fact! HTTP Status Code:", response.status_code)

# ----------------------------------------------
# Conclusion
# ----------------------------------------------

print("HTTP Requests -  web_data_retrieval.py execution complete.")

# End of  web_data_retrieval.py file