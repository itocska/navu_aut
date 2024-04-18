from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def waitUntilSeenXpath(driver, xpath) :
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, xpath)) )
    except NoSuchElementException:
        print("Error in page loading")