from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    browser.execute_script("window.scrollBy(0, 100);")
    chek1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    chek1.click()
    radio1 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    radio1.click()
    time.sleep(0.5)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()