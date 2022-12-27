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

#Select employee:
employee=driver.find_element(By.CSS_SELECTOR,'#MenusDashboard > li:nth-child(2) > a')
employee.click()
time.sleep(1)

#Select Create:
create=driver.find_element(By.CSS_SELECTOR,'#MenusDashboard > li.treeview.menu-open > ul > li:nth-child(1) > a').click()
time.sleep(1)
#fill&save info in create:
fullName=driver.find_element(By.ID,"FirstName").send_keys("Geetha")
lastName=driver.find_element(By.ID,"LastName").send_keys("Vemula")
email=driver.find_element(By.NAME,"EmailId").send_keys("geethavemula@gmail.com")
mobileNumber=driver.find_element(By.NAME,"MobileNo").send_keys('7013267527')
dob=driver.find_element(By.ID,"DOB").send_keys('25/05/2000')
#radio Button:
genderFemale=driver.find_element(By.ID,"rdbFemale").click()
Address=driver.find_element(By.ID,"Address").send_keys('5-23/1,sircilla')
#drop Down:
country=driver.find_element(By.ID,"CountryId").send_keys('India')
city=driver.find_element(By.ID,"CityId").send_keys('Hyderabad')
#check Box:
skills=driver.find_element(By.ID,"chkSkill_1").click()
save=driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(1)

#If we can search the previous employees list then select the select option like given below
search=driver.find_element(By.CSS_SELECTOR,'#MenusDashboard > li.treeview.menu-open > ul > li:nth-child(2) > a').click()

#Search employee info in search:
time.sleep(1)

searchName=driver.find_element(By.ID,"Name").send_keys("Geetha")
mobileNo=driver.find_element(By.ID,"MobileNo").send_keys('7013267527')
search=driver.find_element(By.ID,"btnSearch")
search.click()
time.sleep(1)
driver.refresh()
driver.close()