from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

load_dotenv()

def dataReceiverLogin(driver) :

    driver.get(os.getenv("DATA_RECEIVER_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()='NKR - Adatfogadó alkalmazás']")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(os.getenv("DATA_RECEIVER_USER"))
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(os.getenv("DATA_RECEIVER_PASS"))
    driver.find_element(By.TAG_NAME, 'button').click()

    time.sleep(1)
    try: 
        driver.find_element(By.XPATH,"//h1[text()='Üdvözöljük a NAVÜ Adatfogadó Alkalmazásban!']") 
        print("Login success") 
    except NoSuchElementException: 
        print("Velcome header not found")

def loadConfigurationToDataReceiver(driver) :
    driver.find_element(By.XPATH, "(//mat-card//mat-icon)[1]").click()
    time.sleep(1)
    configs_path = os.listdir(os.getcwd() + "/downloads/configurations")
    result = []
    for file in configs_path:
        if file.startswith("konf"):
            result.append(file)
    #pyautogui.write(os.getenv("DLOAD_PATH_BSLASH") + "\configurations\\ + result[0])
    pyautogui.write(os.getcwd() + "\downloads\configurations\\" + result[0])
    pyautogui.press("enter")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Konfigurációs fájl betöltése')]")) )
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

def checkMappedFile(driver) :
    # driver.find_element(By.XPATH, "//input").click()
    # time.sleep(0.5)
    # driver.find_element(By.XPATH, "//span[contains(text(), 'TestNetwork')]").click()
    # time.sleep(0.5)
    # driver.find_element(By.XPATH, "//span[text()=' Kiválaszt ']").click()
    # time.sleep(1)
    driver.get(os.getenv("DATA_RECEIVER_URL") + "/status/TestNetwork")
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Státuszok']")) )
    except NoSuchElementException:
        print("Error in page loading")
    try:
        WebDriverWait(driver, 40).until( EC.presence_of_element_located((By.XPATH, "//tr[td[contains(., 'SMOKE eseti online')] and td[contains(., 'Kész')]]")) )
    except NoSuchElementException:
        print("Error in page loading")
    downloadMappedFile(driver)

def downloadMappedFile(driver) : 
    driver.get(os.getenv("DATA_RECEIVER_FILES_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Index of /Q0/succesStore']")) )
    except NoSuchElementException:
        print("Error in page loading")
    try:
        WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'SMOKE_eseti_online')]")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//a[contains(text(), 'SMOKE_eseti_online')]").click()