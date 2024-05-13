import shutil
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from DataReceiver import *
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

def clickXP(driver, xpath) :
    driver.find_element(By.XPATH, xpath).click()
    
def printGreen(string) :
    print("\x1b[6;30;42m" + string + "\x1b[0m")
    
def printRed(string) :
    print("\x1b[6;31;41m" + string + "\x1b[0m") 
    

def cleanUp(driver) : 
    dataReceiverLogin(driver)
    selectKeyNetwork(driver, "TestNetwork")
    deleteConfigRS(driver)
    
    driver.get(os.getenv("KM_RESET"))
    now = datetime.now()
    nowPlus7 = now + timedelta(minutes = 7)
    now_time = now.strftime("%H:%M:%S")
    nowPlus7_time = nowPlus7.strftime("%H:%M:%S")
    print("KM reset start: " + str(now_time) +"\nExpected finish: " + str(nowPlus7_time))
    time.sleep(2)
    driver.get(os.getenv("CC_RESET"))
    time.sleep(2)
    driver.get(os.getenv("SS_API_RESET"))
    time.sleep(2)
    
    try:
        shutil.rmtree(os.getcwd() + "/downloads/configurations")
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))