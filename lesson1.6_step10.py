from selenium import webdriver
import time

try:
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    '''elements_first = browser.find_elements_by_tag_name(".first_block input")
    for element in elements_first:
       element.send_keys('Test1')
    elements_second = browser.find_elements_by_tag_name(".second_block input")
    for element in elements_second:
        element.send_keys('Test2')'''
    '''input1 = browser.find_element_by_class_name('first')
    input1.send_keys('Test')
    input2 = browser.find_element_by_class_name('second')
    input2.send_keys('Test')
    input3 = browser.find_element_by_class_name('third')
    input3.send_keys('Test')'''
    input1 = browser.find_element_by_tag_name('div.first_block:nth-child(1) input')
    input1.send_keys('Test1')
    input2 = browser.find_element_by_tag_name('div.first_block:nth-child(2) input')
    input2.send_keys('Test2')
    input3 = browser.find_element_by_tag_name('div.second_block:nth-child(1) input')
    input3.send_keys('Test3')
    input4 = browser.find_element_by_tag_name('div.second_block:nth-child(2) input')
    input4.send_keys('Test4')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()