from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_element_atr = x_element.get_attribute("valuex")
    x = x_element_atr
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)
    chek1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    chek1.click()
    radio1 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    radio1.click()
    button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()