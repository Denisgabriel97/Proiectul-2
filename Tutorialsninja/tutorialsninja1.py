from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get("http://tutorialsninja.com/demo/")
driver.maximize_window()
time.sleep(2)


phones = driver.find_element(By.LINK_TEXT, "Phones & PDAs")
phones.click()

select_phone = driver.find_element(By.LINK_TEXT, "HTC Touch HD")
select_phone.click()

add_to_card = driver.find_element(By.ID, "button-cart")
add_to_card.click()
time.sleep(2)


cameras = driver.find_element(By.LINK_TEXT, "Cameras")
cameras.click()

select_camera = driver.find_element(By.LINK_TEXT, "Nikon D300")
select_camera.click()

add_to_card = driver.find_element(By.ID, "button-cart")
add_to_card.click()
time.sleep(2)


cart = driver.find_element(By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
cart.click()

view_cart = driver.find_element(By.XPATH, "//i[@class='fa fa-shopping-cart']")
view_cart.click()

checkout = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
checkout.click()
time.sleep(2)


continue_1 = driver.find_element(By.ID, "button-account")
driver.execute_script("arguments[0].click()", continue_1)
time.sleep(1)


first_name = driver.find_element(By.ID, "input-payment-firstname")
first_name.send_keys("Denis")
time.sleep(1)

last_name = driver.find_element(By.ID, "input-payment-lastname")
last_name.send_keys("Gabriel")
time.sleep(1)

email = driver.find_element(By.ID, "input-payment-email")
email.send_keys("Denissss@gmail.com")
time.sleep(1)

telephone = driver.find_element(By.ID, "input-payment-telephone")
telephone.send_keys("0769696969")
time.sleep(1)

password = driver.find_element(By.ID, "input-payment-password")
password.send_keys("Testare00")
time.sleep(1)

confirm_password = driver.find_element(By.ID, "input-payment-confirm")
confirm_password.send_keys("Testare00")
time.sleep(1)

adress = driver.find_element(By.ID, "input-payment-address-1")
adress.send_keys("Strada Florilor")
time.sleep(1)

city = driver.find_element(By.ID, "input-payment-city")
city.send_keys("Floresti")
time.sleep(1)

post_code = driver.find_element(By.ID, "input-payment-postcode")
post_code.send_keys("12345" + Keys.ENTER)
time.sleep(1)

country = driver.find_element(By.ID, "input-payment-country")
country.click()
dropdown_1=Select(country)
dropdown_1.select_by_value("175")
time.sleep(1)

region = driver.find_element(By.ID, "input-payment-zone")
region.click()
dropdown_2=Select(region)
dropdown_2.select_by_value("2692")
time.sleep(1)


privacy_policy = driver.find_element(By.XPATH, "//input[@name='agree']")
privacy_policy.click()

register = driver.find_element(By.ID, "button-register")
driver.execute_script("arguments[0].click()", register)
time.sleep(2)

continue_2 = driver.find_element(By.ID, "button-shipping-address")
driver.execute_script("arguments[0].click()", continue_2)
time.sleep(2)

continue_3 = driver.find_element(By.ID, "button-shipping-method")
driver.execute_script("arguments[0].click()", continue_3)
time.sleep(2)

terms_cond = driver.find_element(By.NAME, "agree")
terms_cond.click()
time.sleep(2)

continue_4 = driver.find_element(By.ID, "button-payment-method")
driver.execute_script("arguments[0].click()", continue_4)
time.sleep(2)


confirm_order = driver.find_element(By.ID, "button-confirm")
driver.execute_script("arguments[0].click()", confirm_order)

time.sleep(3)

driver.close()



















