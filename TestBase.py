from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from DataReceiver import *
from ConfigCreator import *
from dotenv import load_dotenv, dotenv_values 
import time
import os

load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#SMOKE SET
createOccasionalDataProvision(driver)
getCertForDataProvision(driver)
time.sleep(0.5)
#dataReceiverLogin(driver)
