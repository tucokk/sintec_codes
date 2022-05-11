from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time

class Login:
    def __init__(self):
        #open page
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        Login.driver = webdriver.Chrome(options=options)
        self.driver.get('https://web.whatsapp.com')

class User(Login):
    def __init__(self):
        self.driver = Login.driver
        #msg infos
        # -------------------
        self.msgtext = '' #msg to be sended
        self.counter = 1 #number of times the msg will be sended
        self.group_or_contact = '' #who it will be sended
        # -------------------

        input('Press any key after scanning QR Code ')
        self.user_page()

    def user_page(self):
        #open contact who will be messaged
        self.user = self.driver.find_element(By.XPATH, f'//span[@title = "{self.group_or_contact}"]').click()
        self.msg()
    
    def msg(self):
        #send message to the contact
        for counter in range(self.counter):
            self.msgbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//div[@title = "Mensagem"]')))
            self.msgbox.send_keys(f'{self.msgtext} \n\nby wpptucobot')
            self.msgbox.send_keys(Keys.ENTER)
            time.sleep(0.5)
        

        time.sleep(10)
        self.driver.quit()

Login()
User()