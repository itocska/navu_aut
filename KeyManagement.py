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
    
    driver.get(os.getenv("KEY_MANAGEMENT_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()='NKR - Kulcsmenedzsment alkalmazás']")) )
    except NoSuchElementException:
        print("Error in page loading")
    current_url = driver.current_url
    if current_url == os.getenv("KEY_MANAGEMENT_URL") + "/log-in" :
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
    #-----
    print("TC:9188 TS:1 checking text 'Paraméterek módosítása'")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[text()='Paraméterek módosítása']")) )
        print("TC:9188 TS:1 Passed")
    except NoSuchElementException:
        print("TC:9188 TS:1 Failed")
    clickXP(driver, "//div[text()='Paraméterek módosítása']")
    #-----
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
    #-----
    print("TC:9188 TS:3 checking if generated keys input readonly")
    if driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[3]").get_attribute("readonly") :
        print("TC:9188 TS:3 Passed")
    else :
        print("TC:9188 TS:3 Failed")
    #-----
    print("TC:9188 TS:4 checking if used keys input readonly")
    if driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[2]").get_attribute("readonly") :
        print("TC:9188 TS:4 Passed")
    else :
        print("TC:9188 TS:4 Failed")
    #-----
    print("TC:9188 TS:5 checking if changes can be saved with string")
    driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[1]").send_keys("string")
    button_element = driver.find_element(By.XPATH, "(//button[contains(@class,'mat-focus-indicator mat-tooltip-trigger')])[2]")
    if "mat-button-disabled" in button_element.get_attribute("class"):
        print("TC:9188 TS:5 Passed")
    else:
        print("TC:9188 TS:5 Failed")
    #-----
    print("TC:9188 TS:6 checking available keys input max validator")
    driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[1]").clear()
    driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[1]").send_keys("12345678901")
    if "mat-button-disabled" in driver.find_element(By.XPATH, "(//button[contains(@class,'mat-focus-indicator mat-tooltip-trigger')])[2]").get_attribute("class"):
        print("TC:9188 TS:6 Passed")
    else:
        print("TC:9188 TS:6 Failed")
    #-----
    print("TC:9188 TS:7 checking available keys input max validator")
    driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[1]").clear()
    driver.find_element(By.XPATH, "(//input[contains(@class,'mat-input-element mat-form-field-autofill-control')])[1]").send_keys("2000")
    if "mat-button-disabled" in driver.find_element(By.XPATH, "(//button[contains(@class,'mat-focus-indicator mat-tooltip-trigger')])[2]").get_attribute("class"):
        print("TC:9188 TS:7 Failed")
    else:
        print("TC:9188 TS:7 Passed")
    #-----
    print("TC:9188 TS:8 checking confirmation")
    clickXP(driver, "(//button[contains(@class,'mat-focus-indicator mat-tooltip-trigger')])[2]")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Figyelem')]")) )
    except NoSuchElementException:
        print("TC:9188 TS:8 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[text()[normalize-space()='Biztos, hogy az alábbi paraméter(eke)t szeretné módosítani? Kiadható kulcsok száma - 1000']]")) )
    except NoSuchElementException:
        print("TC:9188 TS:8 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()=' Mégse ']")) )
    except NoSuchElementException:
        print("TC:9188 TS:8 Failed")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()=' Rendben ']")) )
        print("TC:9188 TS:8 Passed")
    except NoSuchElementException:
        print("TC:9188 TS:8 Failed") 
    #-----
    print("TC:9188 TS:9 checking cancel button")
    clickXP("//span[text()=' Mégse ']")
    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, "//div[contains(text(),'Figyelem')]")
        print("TC:9188 TS:9 Failed")
    except NoSuchElementException:
        print("TC:9188 TS:9 Passed")
    #-----
    print("TC:9188 TS:10 checking confirm button")
    clickXP(driver, "(//button[contains(@class,'mat-focus-indicator mat-tooltip-trigger')])[2]")
    clickXP("//span[text()=' Rendben ']")
        
    
    