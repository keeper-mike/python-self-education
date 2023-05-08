from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

random = random.randint(10, 100000)
driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua/")
driver.maximize_window()

time.sleep(10)
driver.find_element(By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[2]').click()
name = driver.find_element(By.XPATH, '//*[@id="registerUserName"]')
name.clear()
name.send_keys("Стареім'ятест")
last_name = driver.find_element(By.XPATH, '//*[@id="registerUserSurname"]')
last_name.clear()
last_name.send_keys('Новепрізвищетест')
number = driver.find_element(By.XPATH, '//*[@id="registerUserPhone"]')
number.clear()
number.send_keys('0500050039')
email = driver.find_element(By.XPATH, '//*[@id="registerUserEmail"]')
email.clear()
email.send_keys('rskur380ii+', random, '@gmail.com')
password = driver.find_element(By.XPATH, '//*[@id="registerUserPassword"]')
password.clear()
password.send_keys('Test1234+4321test')
driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-register/div/form/fieldset/div[8]/button[1]').click()

time.sleep(6)
driver.close()
driver.quit()