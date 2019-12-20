# Модальные окна
'''alert = browser.switch_to.alert
alert.accept() # открываем и закрываем окно

alert = browser.switch_to.alert
alert_text = alert.text # получить текст

confirm = browser.switch_to.alert
confirm.accept() # согласиться
confirm.dismiss() # отказаться

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept() # ввод текста'''
from selenium import  webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button_one= browser.find_element_by_css_selector('button.btn')
    button_one.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id('input_value').text
    x_element_valuex = int(x_element)

    x = x_element_valuex
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button_two = browser.find_element_by_css_selector('button.btn')
    button_two.click()
    alert = browser.switch_to.alert
    time.sleep(5)
    alert.accept()
finally:
    time.sleep(10)
    browser.quit()