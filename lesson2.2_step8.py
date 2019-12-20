# Работа с файлом
import os
from selenium import webdriver
import time

'''current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)'''
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    first_name.send_keys('Test1')
    last_name = browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    last_name.send_keys('Test2')
    email = browser.find_element_by_css_selector("input[placeholder='Enter email']")
    email.send_keys('test@test')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test_file.txt')
    test_file = browser.find_element_by_css_selector("input[name='file']")
    test_file.send_keys(file_path)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
