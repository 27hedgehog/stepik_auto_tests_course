from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Посчитать математическую функцию от x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # ввод посчитанного
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    
    #СКРОЛЛИМ СТРАНИЦУ НА 150 ПИКСЕЛЕЙ
    browser.execute_script("window.scrollBy(0, 150);")
    
    # Отметить checkbox "I'm the robot".
    ch = browser.find_element(By.ID, "robotCheckbox")
    ch.click()
    #Выбрать radiobutton "Robots rule!".
    rad = browser.find_element(By.ID, "robotsRule")
    rad.click()
    
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
