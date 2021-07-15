from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class CreareCont(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(r"C:\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)

    def autentificare(self):
        buton_autentificare = self.driver.find_element(By.XPATH, "//div[@class='customer-log-out']")
        buton_autentificare.click()

    def creare_cont(self):
        self.creati_un_cont = self.driver.find_element(By.XPATH, "//a[@class='action create primary']")
        self.creati_un_cont.click()

    def introducere_date(self, prenume, nume_de_familie, email, parola, confirmare_parola):
        first_name= self.driver.find_element(By.ID, "firstname")
        second_name = self.driver.find_element(By.ID, "lastname")
        emailul = self.driver.find_element(By.ID ,"email_address")
        parolaa = self.driver.find_element(By.ID, "password")
        confirmarea_parolei = self.driver.find_element(By.ID ,"password-confirmation")

        first_name.send_keys(prenume)
        second_name.send_keys(nume_de_familie)
        emailul.send_keys(email)
        parolaa.send_keys(parola)
        confirmarea_parolei.send_keys(confirmare_parola)

    def selecteaza_genul(self, gen, tipul_genului = "value" ):
        genul = self.driver.find_element(By.ID, 'gender')
        genul.click()
        selectare = Select(genul)
        if tipul_genului == "value":
            selectare.select_by_value(gen)


    def creaza_cont(self):

        buton_creare_cont = self.driver.find_element(By.XPATH, "//button[@class='action submit primary']")
        buton_creare_cont.click()

    def close_session(self):
        self.driver.close()

cont = CreareCont("https://gymbeam.ro")
cont.autentificare()
cont.creare_cont()
time.sleep(3)
cont.introducere_date('Gabriel', 'Szep', 'denisgabriel9705@gmail.com', 'Testing999', 'Testing999')
cont.selecteaza_genul("1", "value")
cont.creaza_cont()
cont.close_session()


