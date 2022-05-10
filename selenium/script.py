'''antes de rodar:

abra o terminal
rode:

pip install selenium
pip install time
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time

class Login:
    def __init__(self):
        #open page
        Login.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com')
        Login.res = ''
        self.login_opts()

    def login_opts(self):
        #insert login strings
        self.login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME ,'username')))
        #seu login no instagram
        self.login_btn.send_keys('tucokk')

        #insert psw strings
        self.psw_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME ,'password')))
        #sua senha no instagram
        self.psw_btn.send_keys('arthur05')

        #login button
        self.submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME ,'form'))).click()
        Login.res = True
            
class User(Login):
    def __init__(self):
        self.res = Login.res
        User.driver = Login.driver
        User.res = ''
        if self.res == True:
            self.user_page()
    
    def user_page(self):
        #open user page
        self.search = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
        #user @ 
        self.search.send_keys('mateus.agnol')
        self.search_result = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a'))).click()
        User.res = True

class SendMessage(User):
    def __init__(self):
        self.res = User.res
        self.driver = User.driver
        if self.res == True:
            self.send_message()
    
    def send_message(self):
        #opening dm page
        self.msg_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button'))).click()

        #verifying if notifications modal is show and closing it
        self.modal = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'/html/body/div[6]/div')))
        self.modal_is_displayed = self.modal.is_displayed()
        if self.modal_is_displayed == True:
            self.not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'/html/body/div[6]/div/div/div/div[3]/button[2]'))).click()

        #sending message
        self.msg = 'teste mateus'
        self.qntmsg = 30

        for i in range(self.qntmsg):
            self.msgarea = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
            self.msgarea.send_keys(f'{self.msg} {i}')
            self.msgarea.send_keys(Keys.ENTER)
            #speed message
            time.sleep(0.5)

login = Login()
user = User()
send_msg = SendMessage()

