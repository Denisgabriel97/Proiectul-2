from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
time.sleep(2)


search = driver.find_element(By.ID, "search_query_top")
search.send_keys("dress" + Keys.ENTER)
time.sleep(2)

dress = driver.find_element(By.XPATH, "//a[@href='http://automationpractice.com/index.php?id_product=2&controller=product&search_query=dress&results=7']")
driver.execute_script("arguments[0].click()", dress)
time.sleep(3)

add_to_cart = driver.find_element(By.XPATH, "//button[@class='exclusive']")
driver.execute_script("arguments[0].click()", add_to_cart)
time.sleep(2)

continue_to_checkout = driver.find_element(By.XPATH, "//a[@class='btn btn-default button button-medium']")
driver.execute_script("arguments[0].click()", continue_to_checkout)
time.sleep(3)


procceded_to_checkout_1 = driver.find_element(By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']")
driver.execute_script("arguments[0].click()", procceded_to_checkout_1)
time.sleep(3)




create_ann_account = driver.find_element(By.ID, "email_create")
create_ann_account.send_keys("denisszuaabb@yahoo.com")


submit_create = driver.find_element(By.ID, "SubmitCreate")
submit_create.click()
time.sleep(4)

mr = driver.find_element(By.XPATH, "//input[@id='id_gender1']")
driver.execute_script("arguments[0].click()", mr)
time.sleep(1)

first_name = driver.find_element(By.ID, "customer_firstname")
first_name.send_keys("Denis")
time.sleep(1)

second_name = driver.find_element(By.ID, "customer_lastname")
second_name.send_keys("Gabriel")
time.sleep(1)

password = driver.find_element(By.ID, "passwd")
password.send_keys("Testare00")
time.sleep(1)

day = driver.find_element(By.ID, "days")
day.click()
dropdown_1=Select(day)
dropdown_1.select_by_value("5")
time.sleep(1)

month = driver.find_element(By.ID, "months")
month.click()
dropdown_1=Select(month)
dropdown_1.select_by_value("10")
time.sleep(1)

year = driver.find_element(By.ID, "years")
year.click()
dropdown_1=Select(year)
dropdown_1.select_by_value("1997")
time.sleep(1)


company = driver.find_element(By.ID, "company")
company.send_keys("Telecom-Academy")
time.sleep(1)

adress = driver.find_element(By.ID, "address1")
adress.send_keys("strada Florilor 69")
time.sleep(1)

city = driver.find_element(By.ID, "city")
city.send_keys("Floresti")
time.sleep(1)

postal_code = driver.find_element(By.ID, "postcode")
postal_code.send_keys("12345")
time.sleep(1)

state = driver.find_element(By.ID, "id_state")
state.click()
dropdown_1=Select(state)
dropdown_1.select_by_value("5")
time.sleep(1)


mobile_phone = driver.find_element(By.ID, "phone_mobile")
mobile_phone.send_keys("0065758909")
time.sleep(1)

register = driver.find_element(By.ID, "submitAccount")
register.click()
time.sleep(1)


procedded_to_checkout_2 = driver.find_element(By.XPATH, "//button[@class='button btn btn-default button-medium']")
procedded_to_checkout_2.click()
time.sleep(1)


terms_button = driver.find_element(By.ID, "cgv")
terms_button.click()
time.sleep(1)

procceded_to_checkout_3 = driver.find_element(By.XPATH, "//button[@class='button btn btn-default standard-checkout button-medium']")
procceded_to_checkout_3.click()
time.sleep(1)

bank_wire = driver.find_element(By.XPATH, "//a[@class='bankwire']")
bank_wire.click()
time.sleep(1)


confirm_order = driver.find_element(By.XPATH, "//button[@class='button btn btn-default button-medium']")
confirm_order.click()
print("Your order on My Store is complete.")
time.sleep(5)


driver.close()

























