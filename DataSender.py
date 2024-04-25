from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

load_dotenv()

def loadConfigurationToDataSender(driver) :
    
    driver.get(os.getenv("DATA_SENDER_URL" + "/configuration"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()='NKR - Adatküldő alkalmazás']")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, "(//mat-card//mat-icon)[1]").click()
    time.sleep(1)
    configs_path = os.listdir(os.getcwd() + "/downloads/configurations")
    result = []
    for file in configs_path:
        if file.startswith("SMOKE eseti online"):
            result.append(file)
    pyautogui.write(os.getcwd() + "\downloads\configurations\\" + result[0])
    pyautogui.press("enter")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Konfiguráció kezelése')]")) )
    except NoSuchElementException:
        print("Error in page loading")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button/span[contains(text(),'Mentés')]").click()
    try:
        WebDriverWait(driver, 40).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Információ')]")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//span[text()=' Rendben ']").click()
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Konfiguráció kezelése']")) )
    except NoSuchElementException:
        print("Error in page loading")

def uploadFileToEncrypt(driver) :
    driver.get(os.getenv("DATA_SENDER_URL" + "/data-submission"))
    