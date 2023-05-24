from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
wait = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
button1 = browser.find_element(By.XPATH, '//*[@id="book"]')
button1.click()
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
input1.send_keys(y)
button2 = browser.find_element(By.XPATH, '//*[@id="solve"]')
browser.execute_script("window.scrollBy(0, 70);")
button2.click()
alert = browser.switch_to.alert
print(alert.text)
alert.accept()
