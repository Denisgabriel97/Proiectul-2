from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(r"C:\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.url)

    def autentificare(self):
        aut = self.driver.find_element(By.XPATH, "//div[@class='customer-log-out']")
        aut.click()

    def input_username_password(self, username, password):
        email = self.driver.find_element(By.XPATH, "//input[@title='E-mail']")
        parola = self.driver.find_element(By.XPATH, "//input[@title='Parola']")

        email.send_keys(username)
        parola.send_keys(password)

    def conectare(self):
        but_conectare = self.driver.find_element(By.XPATH, "//button[@class='action login primary']")
        but_conectare.click()


    def close_session(self):
        self.driver.close()

lgn = Login("https://www.gymbeam.ro/")
lgn.autentificare()
time.sleep(2)
lgn.input_username_password('denisgabriel9705@gmail.com', 'Testing999')
time.sleep(2)
lgn.conectare()
time.sleep(2)
lgn.close_session()

