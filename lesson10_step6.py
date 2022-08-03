from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.ID, "button")
    
    #Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
