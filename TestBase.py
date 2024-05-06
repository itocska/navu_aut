from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from DataReceiver import *
from ConfigCreator import *
from DataSender import *
from Helpers import *
from MultiModule import *
from KeyManagement import *
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

##KM
##TR:9188
changeParameters(driver)
##TR:9184
##TR:9182
##TR:9186
##TR:9185
##TR:9183
##TR:9187
##TR:9181
##TR:9179
##TR:9180
##TR:9178
