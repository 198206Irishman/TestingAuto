from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[style='width:100%']"), "100"))
button_one = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
button_one.click()
x_element = browser.find_element_by_id('input_value').text
x_element_valuex = int(x_element)

x = x_element_valuex
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)
#browser.implicitly_wait(1)
button_two = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
button_two.click()
alert = browser.switch_to.alert
time.sleep(5)
alert.accept()
time.sleep(10)
browser.quit()