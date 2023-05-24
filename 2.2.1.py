from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.XPATH, "//*[@id='num1']").text
    num2 = browser.find_element(By.XPATH, "//*[@id='num2']").text
    y = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))  # ищем элемент с текстом "Python"
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()