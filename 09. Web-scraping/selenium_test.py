import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.amazon.in/s?k=books&crid=CHGNHB0RJ67M&sprefix=books%2Caps%2C100&ref=nb_sb_noss_1"
pth = "chromedriver.exe"
driver = webdriver.Chrome(pth)
driver.get(url)