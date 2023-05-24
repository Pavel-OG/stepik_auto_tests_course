from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    first_name.send_keys("gregor")
    last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    last_name.send_keys("mawd")
    email_input = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    email_input.send_keys("awed@Awd")
    up_file = browser.find_element(By.XPATH, "//*[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'new_file.txt')  # добавляем к этому пути имя файла
    up_file.send_keys(file_path)
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()