from asyncio import wait_for
from xml.dom.minidom import Element
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Selenium Setup
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.amazon.com/?tag=amazusnavi-20&hvadid=381891677693&hvpos=&hvnetw=g&hvrand=12793925684753999037&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9031162&hvtargid=kwd-49491430&ref=pd_sl_67w2s0guum_e&hydadcr=28882_11845412&gclid=Cj0KCQiAwJWdBhCYARIsAJc4idCn6lvaH6_qYovLmXdDFzSpKX9adqiMBUssezNFtVtzKjkKYfTOUw4aAr0FEALw_wcB')
wait = WebDriverWait(driver, 0)
original_window = driver.current_window_handle
actions = ActionChains(driver)


# Searching for the keyword within the Search Bar after signin in
search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search_bar.send_keys()


