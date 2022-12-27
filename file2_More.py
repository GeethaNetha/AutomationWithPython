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

multipleTabs=driver.find_element(By.CSS_SELECTOR,'#MenusDashboard > li.treeview.menu-open > ul > li:nth-child(1) > a').click()
planToSucceed=driver.find_element(By.XPATH,'//*[@id="frmTabs"]/div/div/div/div/ul/li[1]/a').click()
textBox1=driver.find_element(By.ID,"textbox1").send_keys('Thanks')
textBox2=driver.find_element(By.ID,"textbox2").send_keys('Thankyou')
time.sleep(2)

unLearn=driver.find_element(By.XPATH,"//a[normalize-space()='UnLearning']").click()
textBox3=driver.find_element(By.ID,"textbox3").send_keys('Thanks')
textBox4=driver.find_element(By.ID,"textbox4").send_keys('Thankyou')
time.sleep(2)

wayOfLearning=driver.find_element(By.XPATH,"//a[normalize-space()='Ways of Unlearning']").click()
textBox5=driver.find_element(By.ID,"textbox5").send_keys('Thanks')
textBox6=driver.find_element(By.ID,"textbox6").send_keys('Thankyou')
time.sleep(2)

menu=driver.find_element(By.XPATH,"//a[normalize-space()='Menu']").click()
time.sleep(2)

singleMenu=driver.find_element(By.XPATH,"//a[normalize-space()='Single Menus']").click()
time.sleep(2)
testing=driver.find_element(By.ID,"b1").click()
time.sleep(2)
java=driver.find_element(By.ID,"b2").click()
time.sleep(2)
net=driver.find_element(By.ID,"b3").click()
time.sleep(2)
dataBase=driver.find_element(By.ID,"b4").click()
time.sleep(2)

subMenu=driver.find_element(By.XPATH,"//a[normalize-space()='Sub Menus']").click()
time.sleep(2)
testing1=driver.find_element(By.XPATH,"//a[@class='dropbtn'][normalize-space()='Testing']").click()
time.sleep(2)
selenium=driver.find_element(By.XPATH,"//a[@id='selbtn']").click()
time.sleep(2)
manualTesing=driver.find_element(By.XPATH,"//a[@id='manualbtn']").click()
time.sleep(2)
dbtestimg=driver.find_element(By.XPATH,"//a[@id='dbbtn']").click()
time.sleep(2)
unitTesting=driver.find_element(By.XPATH,"//a[@id='unitbtn']").click()
time.sleep(2)

Java1=driver.find_element(By.XPATH,"//a[@class='dropbtn'][normalize-space()='JAVA']").click()
time.sleep(2)
advJava=driver.find_element(By.XPATH,"//a[@id='advjavabtn']").click()
time.sleep(2)
corejava=driver.find_element(By.ID,"corejavabtn").click()
time.sleep(2)
spring=driver.find_element(By.ID,"springbtn").click()
time.sleep(2)
hibernate=driver.find_element(By.ID,"hibernatebtn").click()
time.sleep(2)

net1=driver.find_element(By.XPATH,"//a[@class='dropbtn'][normalize-space()='.Net']").click()
time.sleep(2)
c=driver.find_element(By.ID,"cbtn").click()
time.sleep(2)
asp=driver.find_element(By.ID,"aspbtn").click()
time.sleep(2)
ado=driver.find_element(By.ID,"adobtn").click()
time.sleep(2)
mvc=driver.find_element(By.ID,"mvcbtn").click()
time.sleep(2)

dataBase1=driver.find_element(By.XPATH,"//a[normalize-space()='Database']").click()
time.sleep(2)
sql=driver.find_element(By.ID,"sqlbtn").click()
time.sleep(2)
mysql=driver.find_element(By.ID,"mysqlbtn").click()
time.sleep(2)
oracle=driver.find_element(By.ID,"oraclebtn").click()
time.sleep(2)
h2=driver.find_element(By.ID,"h2btn").click()
time.sleep(2)

#Auto Complete:
driver.find_element(By.XPATH,"//a[normalize-space()='Autocomplete']").click()
singleValues=driver.find_element(By.XPATH,"//a[normalize-space()='Single Values']").click()
time.sleep(2)
tag=driver.find_element(By.XPATH,"//input[@id='txtSingleAutoComplete']").send_keys('comment')
time.sleep(2)

multipleValues=driver.find_element(By.XPATH,"//a[normalize-space()='Multiple Values']").click()
time.sleep(2)
tag2=driver.find_element(By.XPATH,"//input[@id='txtMultipleAutoComplete']").send_keys('comment1 comment2 comment3')
time.sleep(2)

#Collapsible Content:
driver.find_element(By.XPATH,"//a[normalize-space()='Collapsible Content']").click()
time.sleep(2)
singleCollapse=driver.find_element(By.XPATH,"//a[normalize-space()='Single Collapse']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Know your goals and Prioritize Wisely']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Be focused and Eliminate Distractions']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Chose the right mentor to Succeed in career']").click()
time.sleep(2)

multipleCollapse=driver.find_element(By.XPATH,"//a[normalize-space()='Multiple Collapse']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Collaborate with Colleagues']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Learn Anything Quickly']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Reasons People Give Up on Their Goals Too Early']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Signs of Settling For Less In Life']").click()
time.sleep(2)

#Images:
image=driver.find_element(By.XPATH,"//a[normalize-space()='Images']").click()
time.sleep(2)
chooseFile=driver.find_element(By.ID,"file").send_keys('C:/Users/geeth/OneDrive/Pictures/Screenshots/Shiva.png')
time.sleep(2)
fileName=driver.find_element(By.XPATH,"//input[@id='fileName']").send_keys('Lord Shiva')
upload=driver.find_element(By.XPATH,"//button[normalize-space()='Upload']").click()
time.sleep(2)
popup=driver.find_element(By.XPATH,'//*[@id="toast-container"]/div/button').click()
time.sleep(2)

#slider:
slider=driver.find_element(By.XPATH,"//a[@href='/Home/Slider']").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="blue"]/div[1]/div[3]').click()
time.sleep(2)

#Tooltip:
toolTip=driver.find_element(By.XPATH,"//a[@href='/Home/Tooltip']").click()
driver.find_element(By.XPATH,"//ul[@class='nav nav-tabs']//a[contains(text(),'Tooltips')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='btnTooltip']").click()
time.sleep(2)

driver.close()