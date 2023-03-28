#This will not run on online IDE
from pyclbr import Class
import requests
from bs4 import BeautifulSoup
  
URL = "https://www.geeksforgeeks.org/"
req = requests.get(URL)
  
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())
# data 
data = soup.find(id ='home-page')

items = soup.find_all(class_='gfg_home_page_search_card_title_anchor')
# print(soup.find_all('a')) # href attribute
print(data)
print('Items:',items)