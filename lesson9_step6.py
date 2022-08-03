from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    #Переключиться на новую вкладку
    new_window_name = browser.window_handles[1]
    browser.switch_to.window(new_window_name)
    
    #Посчитать математическую функцию от x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # ввод посчитанного
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    
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
