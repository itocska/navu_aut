from DataReceiver import *
from ConfigCreator import *
from DataSender import *
from Helpers import *

def smokeSet(driver) :
##CC
    createOccasionalDataProvision(driver)
    getCertForDataProvision(driver)
    checkCertForDataProvision(driver)
    downloadAndUnzipConfigs(driver)
    #unzipConfig(driver)
##Receiver
    dataReceiverLogin(driver)
    loadConfigurationToDataReceiver(driver)
##Sender
    loadConfigurationToDataSender(driver)
    uploadFileToEncrypt(driver)
##Receiver
    checkMappedFile(driver)