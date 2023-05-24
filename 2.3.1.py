from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)
    button2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()