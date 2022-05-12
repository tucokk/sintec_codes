from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import os

class Login:
    def __init__(self):
        #open page
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument(r"user-data-dir={}".format(profile))
        Login.driver = webdriver.Chrome(options=options)
        self.driver.get('https://web.whatsapp.com')

class User(Login):
    def __init__(self):
        self.driver = Login.driver
        #msg infos
        # -------------------
        self.msgtext = 'kkk o tumalaca' #msg to be sent
        self.counter = 50 #number of times the msg will be sent
        self.group_or_contact = 'garga' #who it will be sent
        # -------------------
        self.user_page()

    def user_page(self):
        #open contact who will be messaged
        self.user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,f'//span[@title = "{self.group_or_contact}"]'))).click()
        self.msg()
    
    def msg(self):
        #send message to the contact
        for counter in range(self.counter):
            self.msgbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//div[@title = "Mensagem"]')))
            self.msgbox.send_keys(f'{self.msgtext}')
            self.msgbox.send_keys(Keys.ENTER)
        self.msgbox.send_keys('sent by wpptucobot')
        self.msgbox.send_keys(Keys.ENTER)
Login()
User()