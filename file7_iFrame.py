import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=s)


#get-commands:title,url,page_source
driver.get("http://magnus.jalatechnologies.com/")

driver.maximize_window()
print(driver.current_url)
print(driver.page_source)
print(driver.title)


#login:
driver.find_element(By.XPATH,"//input[@id='UserName']").send_keys("training@jalaacademy.com")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("jobprogram")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(1)

#Select more option
more=driver.find_element(By.CSS_SELECTOR,'#MenusDashboard > li:nth-child(3) > a').click()
time.sleep(1)

#iFrame
driver.find_element(By.XPATH,"//a[normalize-space()='iFrames']").click()

driver.find_element(By.ID,"iframe1")
driver.switch_to.default_content()
time.sleep(2)

driver.find_element(By.ID,"iframe2").click()
driver.switch_to.default_content()
time.sleep(2)

driver.find_element(By.ID,"iframe3").click()
time.sleep(2)
driver.close()