# import requests
# from bs4 import BeautifulSoup

# def simple_scraper(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         return soup.prettify()
#     else:
#         return f"Failed to retrieve page. Status code: {response.status_code}"

# url = "https://cybernautblogs.medium.com/"
# html_content = simple_scraper(url)
# print(html_content)

import requests
from bs4 import BeautifulSoup

response = requests.get("https://cybernautblogs.medium.com/")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())