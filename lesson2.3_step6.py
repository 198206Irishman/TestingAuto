# Переход на новую вкладку браузера
'''browser.switch_to.window(window_name)
new_window = browser.window_handles[1] # узнать имя вкладки, 1 - вторая открытая вкладка
first_window = browser.window_handles[0] # запомнить имя первой вкладки, чтобы вернуться'''
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button_trollface = browser.find_element_by_css_selector('button.btn')
    button_trollface.click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
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
    time.sleep(5)
    browser.quit()
