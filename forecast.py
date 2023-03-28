#This will not run on online IDE
from pyclbr import Class
import requests
from bs4 import BeautifulSoup
# Pandas
import pandas as pd  
URL = "https://forecast.weather.gov/MapClick.php?lat=44.9055&lon=-122.8107&lg=english&FcstType=text#.ZCMF63ZBy5d"
# sample_url='https://forecast.weather.gov/MapClick.php?lat=41.7875&lon=-87.7416'
req = requests.get(URL) 
soup = BeautifulSoup(req.content, 'html.parser')

week = soup.find(id ='seven-day-forecast-body')
# print(week)
items = soup.find_all(class_ ='tombstone-container')
# print(items[0])
# print(items[0].find(class_ ='period-name').get_text())
# print(items[0].find(class_ ='short-desc').get_text())
# print(items[0].find(class_ ='temp temp-high').get_text())
# All items should  print:
# for item in items:
#     print(item.get_text())

# List of items comprehension
period_names = [item.find(class_ ='period-name').get_text() for item in items]
short_desc = [item.find(class_ ='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
# print(f" {period_names} \n {short_desc} \n {temp}")

weather_stuff = pd.DataFrame({
    'period-name': period_names,
    'short-desc': short_desc,
    'temp': temp
})
print(weather_stuff)
weather_stuff.to_csv('weather.csv')