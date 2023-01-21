import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Initial Setup
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://weather.com/weather/today/l/c3c69cfc9248e306c9c54533c6b25eca5c36122f5ebebc50c48908877ccfcb97')

#Providing Variables
Today_Button = driver.find_element(By.ID, "hamburgerMenu" )


#Automated Actios We Want To Do
actions = ActionChains(driver)
actions.move_to_element(Today_Button)
actions.click(Today_Button)
actions.perform()

# Change to any amount of seconds
time.sleep(3600)

# Further Development 
