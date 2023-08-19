from time import sleep
from selenium import webdriver
import datetime

USERNAME = ""
PASSWORD = ""

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com")
login_path = "/html/body/header/div/nav/ol/li[3]/a[1]"
login_button = driver.find_element("xpath", login_path)
login_button.click()
sleep(3)
username = driver.find_element("xpath", '//*[@id="email"]')
username.send_keys(USERNAME)
password = driver.find_element("xpath", '//*[@id="password"]')
password.send_keys(PASSWORD)
driver.find_element("xpath", '//*[@id="submit-button"]').click()
sleep(5)

with open('access-log.txt', 'a') as out:
    out.write('\n' + str(datetime.datetime.now()))