'''# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
browser.get("https://fake-shop.com/book1.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements_by_css_selector(".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2

#Также для поиска нескольких элементов мы можем использовать универсальный метод find_elements вместе с атрибутами класса By:

from selenium.webdriver.common.by import By

driver.find_elements(By.CSS_SELECTOR, "button.submit")'''
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('div.first_block input')
    for element in elements:
       element.send_keys("Test")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
