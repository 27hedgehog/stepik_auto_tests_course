from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
#Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    #Нажать на кнопку
    button = browser.find_element(By.ID, "book")
    button.click()
    
     #Посчитать математическую функцию от x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # ввод посчитанного
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    
    # Нажать на кнопку Submit.
    button = browser.find_element(By.ID, "solve")
    button.click()
    
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
