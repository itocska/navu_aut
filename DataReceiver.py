from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv, dotenv_values
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    driver.find_element(By.XPATH, "//input[contains(@class,'mat-input-element')]").send_keys("C:\projects\navu_aut\downloads\extracted\konf_TestNetwork_adatfogado_2_2024-04-22_1516.zip")