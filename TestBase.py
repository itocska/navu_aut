from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from DataReceiver import *
from ConfigCreator import *
from dotenv import load_dotenv, dotenv_values 
import time
import os

load_dotenv()

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\projects\navu_aut\downloads\\"}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-features=InsecureDownloadWarnings")
driver = webdriver.Chrome(options=options)

#SMOKE SET
#createOccasionalDataProvision(driver)
#getCertForDataProvision(driver)
#checkCertForDataProvision(driver)
downloadAndUnzipConfigs(driver)
time.sleep(0.5)
#dataReceiverLogin(driver)
