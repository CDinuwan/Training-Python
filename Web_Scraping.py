#beautifulSoup
#Request
#Pandas

import pandas as pd
import requests
from bs4 import BeautifulSoup

page=requests.get('https://forecast.weather.gov/MapClick.php?lat=40.6036&lon=-73.9544#.XqR4NkBuLDd')
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.find_all('a'))
week=soup.find(id='seven-day-forecast-body')
#print(week)

items=week.find_all(class_='tombstone-container')
print(items[0])

items[0].find(class_='period-name').get_text()
items[0].find(class_='short-desc').get_text()
items[0].find(class_='temp').get_text()

period_names=[item.find(class_='period-name').get_text() for item in items]
short_desc=[item.find(class_='short-desc').get_text() for item in items]
temp=[item.find(class_='temp').get_text() for item in items]
print(period_names)
print(short_desc)
print(temp)

weather_stuff=pd.DataFrame(
    {
        'period':period_names,
        'short-desc':short_desc,
        'temp':temp
    }
)
print(weather_stuff)
weather_stuff.to_csv('weather.csv')