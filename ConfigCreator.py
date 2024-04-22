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

def createOccasionalDataProvision(driver) :
    
    driver.get(os.getenv("CONFIG_CREATOR_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Adatszolgáltatások']")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, "//span[text()=' Adatszolgáltatás létrehozása ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Adatszolgáltatás létrehozása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    
    driver.find_element(By.XPATH, '(//input)[1]').send_keys('SMOKE')
    driver.find_element(By.XPATH, '(//input)[2]').send_keys('SMOKE01')
    driver.find_element(By.XPATH, '(//mat-select)[1]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[1]').click()
    driver.find_element(By.XPATH, '(//mat-select)[2]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[1]').click()
    driver.find_element(By.XPATH, '(//input)[3]').send_keys('SMOKE igénylő')
    driver.find_element(By.XPATH, '(//input)[4]').send_keys('SMOKE fogadó')
    driver.find_element(By.XPATH, "//span[contains(text(),'Eseti')]").click()

    createOfflineEMSZ(driver)
    createOnlineEMSZ(driver)

    driver.find_element(By.XPATH, "//span[text()=' Mentés ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Információ')]")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, "//span[text()=' Rendben ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Adatszolgáltatások']")) )
    except NoSuchElementException:
        print("Error in page loading")

def createOfflineEMSZ(driver) :

    driver.find_element(By.XPATH, "//span[text()=' EMSZ létrehozása ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[text()='EMSZ létrehozása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[1]').send_keys('SMOKE eseti offline')
    driver.find_element(By.XPATH, "//mat-dialog-container//span[contains(text(), 'Offline')]").click()
    driver.find_element(By.XPATH, "//span[text()=' Hozzáad ']").click()

    createListConfig(driver, "SMOKE eseti offline")

def createOnlineEMSZ(driver) :

    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()=' EMSZ létrehozása ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[text()='EMSZ létrehozása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[1]').send_keys('SMOKE eseti online')
    driver.find_element(By.XPATH, "//mat-dialog-container//span[contains(text(), 'Online')]").click()
    driver.find_element(By.XPATH, "//span[text()=' Hozzáad ']").click()

    createListConfig(driver, "SMOKE eseti online")

def createListConfig(driver, EMSZname) :

    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'" + EMSZname + "')]")) )
    except NoSuchElementException:
        print("Error in page loading")

    trs = driver.find_elements(By.XPATH, "//tr")
    emszCount = len(trs) / 2
    emszCount = int(emszCount)

    driver.find_element(By.XPATH, "//td[contains(text(),'" + EMSZname + "')]").click()
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 200)","")
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "(//span[text()=' Listakonfiguráció létrehozása '])[" + str(emszCount) + "]")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, "(//span[text()=' Listakonfiguráció létrehozása '])[" + str(emszCount) + "]").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[text()=' " + EMSZname + " - Listakonfiguráció létrehozása ']")) )
    except NoSuchElementException:
        print("Error in page loading")
    
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[3]').send_keys('5')
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[1]').send_keys('SMOKE lista')
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[2]').send_keys('1000')

    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[6]').send_keys('SMOKE1_INT')
    driver.find_element(By.XPATH, '(//mat-slide-toggle)[2]').click()
    driver.find_element(By.XPATH, '(//mat-select)[3]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[2]').click()
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[9]').send_keys('10')

    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[12]').send_keys('SMOKE2_DATE')
    driver.find_element(By.XPATH, '(//mat-slide-toggle)[4]').click()
    driver.find_element(By.XPATH, '(//mat-select)[4]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[3]').click()
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[15]').send_keys('20')

    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[18]').send_keys('SMOKE3_STRING')
    driver.find_element(By.XPATH, '(//mat-slide-toggle)[6]').click()
    driver.find_element(By.XPATH, '(//mat-select)[5]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[1]').click()
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[21]').send_keys('20')

    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[24]').send_keys('SMOKE4_STRING')
    driver.find_element(By.XPATH, '(//mat-slide-toggle)[8]').click()
    driver.find_element(By.XPATH, '(//mat-select)[6]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[1]').click()
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[27]').send_keys('20')

    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[30]').send_keys('SMOKE5_STRING')
    driver.find_element(By.XPATH, '(//mat-slide-toggle)[10]').click()
    driver.find_element(By.XPATH, '(//mat-select)[7]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '(//mat-option)[1]').click()
    driver.find_element(By.XPATH, '(//mat-dialog-container//input)[33]').send_keys('20')

    driver.find_element(By.XPATH, "//span[text()=' Hozzáad ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//span[text()=' Bezárás ']")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, "//span[text()=' Bezárás ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'" + EMSZname + "')]")) )
    except NoSuchElementException:
        print("Error in page loading")

    driver.find_element(By.XPATH, "//td[contains(text(),'" + EMSZname + "')]").click()
    time.sleep(0.5)

def getCertForDataProvision(driver) :

    driver.find_element(By.XPATH, "(//mat-icon[contains(@class,'mat-icon notranslate')])[3]").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Adatszolgáltatás módosítása']")) )
    except NoSuchElementException:
        print("Error in page loading")

    # Requester Cert Login
    driver.find_element(By.XPATH, "(//span[text()=' Tanúsítvány igénylése '])[1]").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[text()='Tanúsítvány igényléshez szükséges belépési adatok megadása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys(os.getenv("RA_NICK"))
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(os.getenv("RA_PASS"))
    driver.find_element(By.XPATH, "//span[text()=' Bejelentkezés ']").click()
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Információ')]")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//span[text()=' Rendben ']").click()
    time.sleep(0.5)


    # Receiver Cert Login
    driver.find_element(By.XPATH, "(//span[text()=' Tanúsítvány igénylése '])[2]").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[text()='Tanúsítvány igényléshez szükséges belépési adatok megadása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys(os.getenv("RA_NICK"))
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(os.getenv("RA_PASS"))
    driver.find_element(By.XPATH, "//span[text()=' Bejelentkezés ']").click()
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Információ')]")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//span[text()=' Rendben ']").click()
    time.sleep(0.5)

    # Scrolling and open to EMSZ Cert Login
    driver.find_element(By.XPATH, "//td[contains(text(),'SMOKE eseti online')]").click()
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 200)","")
    time.sleep(0.5)


    # EMSZ Cert Login
    driver.find_element(By.XPATH, "(//span[text()=' Tanúsítvány igénylése '])[3]").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h2[text()='Tanúsítvány igényléshez szükséges belépési adatok megadása']")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys(os.getenv("RA_NICK"))
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(os.getenv("RA_PASS"))
    driver.find_element(By.XPATH, "//span[text()=' Bejelentkezés ']").click()
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Információ')]")) )
    except NoSuchElementException:
        print("Error in page loading")
    driver.find_element(By.XPATH, "//span[text()=' Rendben ']").click()
    time.sleep(0.5)

def checkCertForDataProvision(driver) :

    while driver.find_element(By.XPATH, "(//mat-icon)[3]").text != "check_circle_outline" :
        #TODO if the answer was error during cert request
        print("Waiting for Certification")
        time.sleep(30)
        driver.refresh()
        time.sleep(0.5)
        try:
            WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Adatszolgáltatás módosítása']")) )
        except NoSuchElementException:
            print("Error in page loading")

    driver.get(os.getenv("CONFIG_CREATOR_URL"))
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//h1[text()='Adatszolgáltatások']")) )
    except NoSuchElementException:
        print("Error in page loading")

def downloadAndUnzipConfigs(driver) : 
    try:
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//mat-icon[text()='download_for_offline']")) )
    except NoSuchElementException:
        print("Data provision error")
    driver.find_element(By.XPATH, "//mat-icon[text()='download_for_offline']").click()

    time.sleep(2)
    
    #impovement idea - wait until downloaded
    files = glob.glob(os.getenv("DLOAD_PATH") + "/*")
    latest_file_full_path = max(files, key = os.path.getctime)
    print("Name of the downloaded file: ", latest_file_full_path)

    with ZipFile(latest_file_full_path, 'r') as zObject :
        zObject.extractall(path = os.getenv("DLOAD_PATH") + "/extracted") 
    


#def createDataProvision(driver, dataServiceMode) :
#def createEMSZ(driver, dataServiceMode, dataServiceType) :
