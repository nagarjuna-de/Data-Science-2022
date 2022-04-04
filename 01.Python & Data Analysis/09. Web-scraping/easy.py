import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YgE8prrMKUk')

print(page)

soup = BeautifulSoup(page.content, 'html.parser')

day = soup.find('div', class_="col-sm-2 forecast-label")
print(day)