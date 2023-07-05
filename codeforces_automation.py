from selenium import webdriver
import getpass
import time
from selenium.webdriver.common.by import By


#codeforces credentials for login
email="sagar.programming.2664@gmail.com"
password=getpass.getpass("Password: ")

#problem code
problem="https://codeforces.com/contest/1792/submit"

#submission code
with open('OurCode.cpp','r') as f:
    code=f.read()

#starting browser session
browser=webdriver.Chrome("")

#opening link in browser
browser.get("https://codeforces.com/enter?back=%2F")

#login
emailElm=browser.find_element(By.ID,"handleOrEmail")
emailElm.send_keys(email)

passElm=browser.find_element(By.ID,'password')
passElm.send_keys(password)

browser.find_element(By.CLASS_NAME,"submit").click()

#In case of slow internet
time.sleep(10)

#getting submit page of a contest
browser.get(problem)

#choosing problem
browser.find_element(By.XPATH,'/html/body/div[6]/div[4]/div[2]/form/table/tbody/tr[1]/td[2]/label/select/option[2]').click()

#choosing language
browser.find_element(By.XPATH,'/html/body/div[6]/div[4]/div[2]/form/table/tbody/tr[3]/td[2]/select/option[8]')

#making editor as text editor
browser.find_element(By.ID,'toggleEditorCheckbox').click()

#pasting our code
textElem=browser.find_element(By.ID,'sourceCodeTextarea')
textElem.send_keys(code)

#submmitting code
browser.find_element(By.CLASS_NAME,'submit').click()

time.sleep(30)