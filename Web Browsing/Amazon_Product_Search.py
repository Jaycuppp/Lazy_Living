import selenium, time, pyautogui as PAG

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def webBrowsing ():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.amazon.com/?tag=hymsabk-20&ref=pd_sl_290dlthsvm_e&adgrpid=1341404752168026&hvadid=83838074749799&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=80154&hvtargid=kwd-83838147155260:loc-190&hydadcr=28884_14580403')

    Wait = WebDriverWait(driver, 1)
    OriginalWindow = driver.current_window_handle
    Actions = ActionChains(driver)

    # Function for allowing selenium to mouse scroll for n amount of times
    def Scrolling(XPixels, YPixels, Scrolling_Amount):
        LoopCount = 0
        while LoopCount < int(Scrolling_Amount):
            LoopCount += 1
            Actions.scroll_by_amount(delta_x=int(XPixels), delta_y=int(YPixels)).perform(), time.sleep(1)
        return 0


    # 60 Seconds should be enough time to complete the manual Amazon Human Check
    driver.implicitly_wait(60)


    # Find Product Search Bar And Input Desired Keys
    SearchBarID = 'twotabsearchtextbox'
    Search_Button = driver.find_element(By.ID, SearchBarID)
    Search_Button.send_keys('Computer Gaming Graphics Card')


    # Find and Click On The Search Button
    SearchButID = 'nav-search-submit-button'
    Search_Button_Click = driver.find_element(By.ID, SearchButID)
    Search_Button_Click.click()
    

    driver.implicitly_wait(20)

    
    FilterDrowpDownCLASS = "a-dropdown-prompt"
    FilterDrowpDownButton = driver.find_element(By.CLASS_NAME, FilterDrowpDownCLASS)
    FilterDrowpDownButton.click()
    
    
    SortByChoicesID = {
        'Featured': 's-result-sort-select_0',
        'Price: Low to High Price': 's-result-sort-select_1',
        'Price: High to Low Price': 's-result-sort-select_2',
        'Avg. Customer Review': 's-result-sort-select_3',
        'Newest Arrivals': 's-result-sort-select_4',
        'Best Sellers': 's-result-sort-select_5',
    }
    
    FilterDrowpDownSelectOption = driver.find_element(By.ID, SortByChoicesID['Price: High to Low Price'])
    FilterDrowpDownSelectOption.click()
    
    # Delay until the different product result sorthing has happened
    time.sleep(7)
    
    # Scrolling Down
    Scrolling(0, 500, 7)
    
    # Srolling Back Up
    Scrolling(0.00, -500.00, 7.0)

    # 1-hour time delay to allow manual control over website
    time.sleep(3600)
    
    return 0


if __name__ == "__main__":
    webBrowsing()