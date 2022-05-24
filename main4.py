from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")

username = os.getenv("in_user")
password = os.getenv("in_pass")
chrome_driver_path = Service("C:/Users/conno/chrome_driver/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

f = open("insta_accounts.txt", "r")
y = [x for x in f]

class InstaFollower:

    def __init__(self):
        f = open("insta_accounts.txt", "r")
        self.accts = [x for x in f]
        #print(self.accts)

    def login(self, username, password):
        self.user = username
        self.pass_ = password
        driver.get('https://www.instagram.com/')
        time.sleep(4)
        self.log = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.pas = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.log_btn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

    def follow(self):
        self.search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')


b = InstaFollower()

b.login(username, password)
b.log.send_keys(username)
b.pas.send_keys(password)
b.log_btn.click()
time.sleep(4)
ex1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
ex1.click()
ex2 = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
ex2.click()
time.sleep(4)

b.follow()
for x in range(len(b.accts)):
    b.search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    b.search_bar.send_keys(Keys.CONTROL + "a")
    b.search_bar.send_keys(Keys.BACK_SPACE)
    time.sleep(3)
    b.search_bar.send_keys(b.accts[x])
    #e.search_bar=driver
    time.sleep(4)
    profile = driver.find_element(By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
    profile.click()
    time.sleep(4)
    follow_btn = driver.find_element(By.CLASS_NAME, '_5f5mN')
    follow_btn.click()
    time.sleep(2)

driver.quit()