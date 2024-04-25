from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import os

def waitUntilSeenXpath(driver, xpath) :
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, xpath)) )
    except NoSuchElementException:
        print("Error in page loading")

def searchFileIn(path, startsWith) : 
    configs_path = os.listdir(path)
    result = []
    for file in configs_path:
        if file.startswith(startsWith):
            result.append(file)
    return result[0]