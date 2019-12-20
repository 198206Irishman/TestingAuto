# Как работают методы get и find_element
# Метод "неявное ожидание" для синхронизации с интерактивным сайтом Implicit Waits
# явные ожидания (Explicit Waits) с помощью инструментов WebDriverWait и expected_conditions
# в этом случае нужно использовать поиск элементов с помощью класса By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")
#browser.get('http://suninjuly.github.io/cats.html')
#button = browser.find_element_by_id('button')
# говорим WebDriver искать каждый элемент в течение 5 секунд
'''browser.implicitly_wait(5)'''
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#функция until, в которую передается правило ожидания
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
#element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае
# time.sleep(2) # Сайт интерактивный, задержка 1 секунда, без таймера тест валится
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
'''button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))'''
# негативное правило с помощью метода until_not
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text # assert проверка