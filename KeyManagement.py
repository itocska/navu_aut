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
    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(os.getenv("KEY_MANAGEMENT_USER"))
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(os.getenv("KEY_MANAGEMENT_PASS"))
    driver.find_element(By.TAG_NAME, 'button').click()

    time.sleep(1)
    try: 
        driver.find_element(By.XPATH,"//h1[text()='Kulcshálózat választás']") 
        print("Login success") 
    except NoSuchElementException: 
        print("Velcome header not found")

def changeParameters(driver) :
    
    driver.get(os.getenv("KEYMANAGEMENT_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()='NKR - Kulcsmenedzsment alkalmazás']")) )
    except NoSuchElementException:
        print("Error in page loading")
    current_url = driver.current_url
    if current_url == os.getenv("KEYMANAGEMENT_URL" + "/log-in") :
        keymanagementLogin(driver)
    clickXP(driver, "//mat-select")
    time.sleep(0.5)
    clickXP(driver, "(//mat-option)[1]")
    clickXP(driver, "//span[text()=' Kiválaszt ']")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Kulcshálózat adatai']")) )
    except NoSuchElementException:
        print("Error in page loading")
    clickXP(driver, "(//button)[1]")
    print("TC:9188 TS:1 checking text 'Paraméterek módosítása'")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[text()='Paraméterek módosítása']")) )
        print("TC:9188 TS:1 Passed")
    except NoSuchElementException:
        print("TC:9188 TS:1 Failed")
    clickXP(driver, "//div[text()='Paraméterek módosítása']")
    print("TC:9188 TS:2 checking DOMS, 3 input fields, 2 buttons")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Paraméterek módosítása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//mat-label[text()='Felhasználható titkosító kulcsok száma']")) )
        print("TC:9188 TS:2 Available keys input found")
    except NoSuchElementException:
        print("TC:9188 TS:2 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//mat-label[text()='Felhasznált titkosító kulcsok száma']")) )
        print("TC:9188 TS:2 Used keys input found")
    except NoSuchElementException:
        print("TC:9188 TS:2 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//mat-label[text()='Generált kulcshármasok száma']")) )
        print("TC:9188 TS:2 Generated keys input found")
    except NoSuchElementException:
        print("TC:9188 TS:2 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()=' Visszaállítás ']")) )
        print("TC:9188 TS:2 Rollback button found")
    except NoSuchElementException:
        print("TC:9188 TS:2 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()=' Mentés ']")) )
        print("TC:9188 TS:2 Save button found")
    except NoSuchElementException:
        print("TC:9188 TS:2 Failed")
    print("TC:9188 TS:2 Passed")
    
    