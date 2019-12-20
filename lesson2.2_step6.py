# execute_script
'''from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскролить страницу.
button.click()
#browser.execute_script("window.scrollBy(0, 100);") Эта команда проскроллит страницу на 100 пикселей вниз
assert True'''
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);") # опускаем лишнее окно
    x_element = browser.find_element_by_id('input_value').text
    x_element_valuex = int(x_element)

    x = x_element_valuex
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()