import requests
from bs4 import BeautifulSoup

# Making a GET request and handling exceptions
try:
    r = requests.get('https://computerlearningcenters.com/')
    r.raise_for_status()  # Check if the request was successful (status code 200)
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
else:
    # Parsing the HTML content
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Display the prettified HTML
    print(soup.prettify())
