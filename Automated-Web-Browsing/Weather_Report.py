import time
from selenium import webdriver

#Initial Setup
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://weather.com/weather/today/l/c3c69cfc9248e306c9c54533c6b25eca5c36122f5ebebc50c48908877ccfcb97')

time.sleep(3600)
