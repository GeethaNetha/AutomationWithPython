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

#Links:
links=driver.find_element(By.XPATH,"//a[normalize-space()='Links']").click()
workingLinks=driver.find_element(By.XPATH,"//a[normalize-space()='Working Links']").click
link1=driver.find_element(By.XPATH,"//a[@href='http://www.workinglinks.co.uk/']").click()
time.sleep(2)
link2=driver.find_element(By.XPATH,"//a[@href='https://www.google.co.in/'][normalize-space()='Link 2']").click()
time.sleep(2)
link3=driver.find_element(By.XPATH,"//a[@href='http://jalatechnologies.com/'][normalize-space()='Link 3']").click()
time.sleep(2)

brokenLink=driver.find_element(By.XPATH,"//a[normalize-space()='Broken Links']").click()
link4=driver.find_element(By.XPATH,"//a[@href='www.brokenlinkcheck.com/'][normalize-space()='Link 1']").click()
time.sleep(2)
link5=driver.find_element(By.XPATH,"//a[@href='www.brokenlinkcheck.com/'][normalize-space()='Link 2']").click()
time.sleep(2)
link6=driver.find_element(By.XPATH,"//a[@href='www.brokenlinkcheck.com/'][normalize-space()='Link 3']").click()
time.sleep(2)

#imageLinks:
imageLink=driver.find_element(By.XPATH,"//a[normalize-space()='Image Links']").click()
driver.find_element(By.XPATH,"//img[@alt='Growic Link']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Linkedin Link']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Goggle Link']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Jala Technologies Link']").click()
time.sleep(2)

#Status code:
statusCode=driver.find_element(By.XPATH,"//a[normalize-space()='Status Codes']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='200']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='301']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='404']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='500']").click()
time.sleep(2)
driver.quit()



