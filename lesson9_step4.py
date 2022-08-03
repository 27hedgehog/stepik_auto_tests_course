from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math 

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
#Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    browser.get(link)
#Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
#Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
#На новой странице решить капчу для роботов, чтобы получить число с ответом
#Посчитать математическую функцию от x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # ввод посчитанного
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
