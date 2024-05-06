from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from zipfile import ZipFile
from Helpers import *
import time
import os
import glob

load_dotenv() 

def keymanagementLogin(driver) :
    pass

def changeParameters(driver) :
    
    driver.get(os.getenv("KEYMANAGEMENT_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()='NKR - Kulcsmenedzsment alkalmazás']")) )
    except NoSuchElementException:
        print("Error in page loading")
    current_url = driver.current_url
    if current_url == os.getenv("KEYMANAGEMENT_URL" + "/log-in") :
        keymanagementLogin(driver)
    