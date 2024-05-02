from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from DataReceiver import *
from ConfigCreator import *
from DataSender import *
from Helpers import *
from MultiModule import *
from dotenv import load_dotenv, dotenv_values 
import time
import os

load_dotenv()

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd() + "\downloads"} 
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-features=InsecureDownloadWarnings")
driver = webdriver.Chrome(options=options)

#SMOKE SET
#smokeSet(driver)

##CleanUp
#cleanUp(driver)
