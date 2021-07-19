from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class Creatina(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(r"C:\chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()


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


    def cautare(self):
        bara_cautare = self.driver.find_element(By.NAME, "q")
        bara_cautare.send_keys("creatina" + Keys.ENTER)


    def selectare(self):
        selectare_produs = self.driver.find_element(By.XPATH, "//a[@href='https://gymbeam.ro/creatina-dna-216-g-bsn.html']")
        selectare_produs.click()


    def adauga_in_cos(self):
        buton_adauga = self.driver.find_element(By.XPATH, "//button[@id='product-addtocart-button']")
        self.driver.execute_script("arguments[0].click()", buton_adauga)

    def vizualizare_cos(self):
        cos = self.driver.find_element(By.XPATH, "//a[@class='action showcart']")
        self.driver.execute_script("arguments[0].click()", cos)

    def finalizarea_comenzii(self):
        finalizare_comanda = self.driver.find_element(By.XPATH, "//button[@class='action primary checkout']")
        self.driver.execute_script("arguments[0].click()", finalizare_comanda)


    def continua(self):
        buton_continua = self.driver.find_element(By.XPATH, "//button[@class='button action continue primary']")
        self.driver.execute_script("arguments[0].click()", buton_continua)

    def selectare_plata(self):
        ramburs =self.driver.find_element(By.XPATH, "//input[@id='cashondelivery']")
        self.driver.execute_script("arguments[0].click()", ramburs)


    def close_session(self):
        self.driver.close()



supliment = Creatina("https://www.gymbeam.ro/")
supliment.autentificare()
supliment.input_username_password('denisgabriel9705@gmail.com','Testing999')
time.sleep(2)
supliment.conectare()
time.sleep(5)
supliment.cautare()
time.sleep(5)
supliment.selectare()
time.sleep(5)
supliment.adauga_in_cos()
time.sleep(5)
supliment.vizualizare_cos()
time.sleep(5)
supliment.finalizarea_comenzii()
time.sleep(5)
supliment.continua()
time.sleep(5)
supliment.selectare_plata()
time.sleep(5)
supliment.close_session()


