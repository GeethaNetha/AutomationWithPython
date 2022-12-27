import time

import requests as requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://magnus.jalatechnologies.com/Home/Index")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='UserName']").send_keys("training@jalaacademy.com")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("jobprogram")
driver.find_element(By.ID,"btnLogin").click()

time.sleep(1)

more=driver.find_element(By.CSS_SELECTOR,'#MenusDashboard > li:nth-child(3) > a').click()
time.sleep(1)

#Popups:
popups=driver.find_element(By.XPATH,"//a[normalize-space()='Popups']").click()

inwindowPopup=driver.find_element(By.XPATH,'//*[@id="btn-six"]').click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Close']").click()

alertBox=driver.find_element(By.XPATH,"//input[@id='alertBox']").click()
driver.switch_to.alert.accept()

time.sleep(2)

confirmBox=driver.find_element(By.XPATH,"//input[@id='confirmBox']").click()
if confirmBox =='yes':
    print(driver.switch_to.alert.accept())
else:
    print(driver.switch_to.alert.dismiss())
time.sleep(2)


promptBox=driver.find_element(By.XPATH,'//*[@id="promptBtn"]').click()
if promptBox =='JALA Academy- A Place to find your Dream Job':
    print(driver.switch_to.alert.accept())
else:
    print(driver.switch_to.alert.dismiss())
time.sleep(2)
driver.close()

