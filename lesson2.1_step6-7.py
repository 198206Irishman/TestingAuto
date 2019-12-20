# Get_atribute метод
from selenium import webdriver
import time

'''try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default" # проверка истинности assert
    # assert people_checked == "true", "People radio is not selected by default" # проверка истинности assert
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked is None, "Robot radio is not selected by default"
    button = browser.find_element_by_css_selector("button.btn")
    button_test = button.get_attribute("Disabled")
    print("Disabled", button_test)
    button.click()
finally:
    time.sleep(10)
    browser.quit()'''
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('treasure')
    x_element_valuex = x_element.get_attribute('valuex')
    print(x_element_valuex)
finally:
    time.sleep(10)
    browser.quit()