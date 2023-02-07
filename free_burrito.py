from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import random

rdm = random.randint(5,99999999999999999999)
mail = "martin+"+str(rdm)+"@mouly.name"
print(mail)


driver = webdriver.Firefox()
driver.get("https://chipotefr.fbmta.com/members/UpdateProfile.aspx?Action=Subscribe&_Theme=30064771402&InputSource=krank")

# prenom
driver.find_element(by=By.ID, value="ctl00_PageContent_MemberProfileControl_CustomField_FirstName_0").send_keys("prenom")
# nom
driver.find_element(by=By.ID, value="ctl00_PageContent_MemberProfileControl_CustomField_LastName_0").send_keys("nom")
# mail
driver.find_element(by=By.ID, value="ctl00_PageContent_MemberProfileControl_CustomField_EmailAddress_0").send_keys(mail)
# confirm mail
driver.find_element(by=By.ID, value="ctl00_PageContent_MemberProfileControl_CustomField_EmailAddress_1").send_keys(mail)
# submit 
driver.find_element(by=By.ID, value="ctl00_PageContent_SubmitText").click()

driver.quit()
