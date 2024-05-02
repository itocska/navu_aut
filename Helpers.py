from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from DataReceiver import dataReceiverLogin
import os
import time

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

def cleanUp(driver) : 
    dataReceiverLogin(driver)
    driver.get(os.getenv("CC_RESET"))
    time.sleep(2)
    driver.get(os.getenv("RS_RESET"))
    time.sleep(2)
    driver.get(os.getenv("SS_RESET"))
    time.sleep(2)

    #Delete Conf from RS
    #Delete download folder