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
time.sleep(2)

#Css Properties:
driver.find_element(By.XPATH,"//a[normalize-space()='CSS Properties']").click()
#Links
driver.find_element(By.XPATH,"//li[@class='active']//a[contains(text(),'Links')]").click()
link7=driver.find_element(By.XPATH,"//a[normalize-space()='Link 1']").click()
time.sleep(2)
link8=driver.find_element(By.XPATH,"//a[normalize-space()='Link 2']").click()
time.sleep(2)
link9=driver.find_element(By.XPATH,"//a[normalize-space()='Link 3']").click()
time.sleep(2)
link10=driver.find_element(By.XPATH,"//a[normalize-space()='Link 4']").click()
time.sleep(2)
link11=driver.find_element(By.XPATH,"//a[normalize-space()='Link 5']").click()
time.sleep(2)
#Labels;
driver.find_element(By.XPATH,"//a[normalize-space()='Labels']").click()
time.sleep(2)
#Buttons:
driver.find_element(By.XPATH,"//a[normalize-space()='Buttons']").click()
time.sleep(2)
#Alert:
driver.find_element(By.XPATH,"//a[normalize-space()='Alerts']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='alert alert-success']//button[@type='button'][normalize-space()='×']").click()
time.sleep(2)
#Progress bar:
driver.find_element(By.XPATH,"//a[normalize-space()='Progress Bars']").click()
time.sleep(2)
driver.quit()