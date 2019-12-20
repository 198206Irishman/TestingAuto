'''from selenium import webdriver
import time

try:
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name('div.first_block:nth-child(1) input')
    input1.send_keys('Test1')
    input2 = browser.find_element_by_tag_name('div.first_block:nth-child(2) input')
    input2.send_keys('Test2')
    input3 = browser.find_element_by_tag_name('div.second_block:nth-child(1) input')
    input3.send_keys('Test3')
    input4 = browser.find_element_by_tag_name('div.second_block:nth-child(2) input')
    input4.send_keys('Test4')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()'''
import time
from selenium import webdriver

__author__ = 'ivan chistov'

try:
    # Link to registration form without bug
    link_old = 'http://suninjuly.github.io/registration1.html'
    # Link to reg form with bug
    link_new = 'http://suninjuly.github.io/registration2.html'

    # Start WebDriver
    browser = webdriver.Chrome()
    browser.get(link_new)
    browser.get(link_old)

    # WebDriver is filling registration form
    first_name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
    last_name.send_keys('Chistov')
    email = browser.find_element_by_css_selector("input[placeholder='Input your email']")
    email.send_keys('qwert@ro.ru')

    # Click to button in form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    # Expected result
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
