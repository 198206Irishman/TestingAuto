# Select
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_xpath('//span[@id="num1"]').text # вытаскиваем текст
    num2 = browser.find_element_by_xpath('//span[@id="num2"]').text # тут именно искать по xpath
    res = str(int(num1)+int(num2))
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(res)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("option:nth-child(2)").click()
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value("1")  # ищем элемент с текстом
    #select.select_by_visible_text("text") ищет по тексту
    #select.select_by_index(index) ищет по индексу, индекс начинается с 0
finally:
    time.sleep(10)
    browser.quit()