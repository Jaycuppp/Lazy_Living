import selenium, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initial Setup
GoogleOptions = webdriver.ChromeOptions()
GoogleOptions.page_load_strategy = "normal"

driver = webdriver.Chrome(options=GoogleOptions)
driver.get('https://www.volutone.com/')

# Locating the HTML Elements And Typing Buttons In Input Box
SearchBardID = 'Search_vtuopctu0_input'
search = driver.find_element(By.ID, SearchBardID)
search.send_keys("Samsung")
search.send_keys(Keys.RETURN)

# Accepting The Cookies
CookieAcceptButttonID = 'onetrust-accept-btn-handler'
search = driver.find_element(By.ID, CookieAcceptButttonID)
search.click()

time.sleep(999999)

# Further Development Once More Automated Tasks Are Required