from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #получения значение переменных, расчет и перевод суммы в строку
    perem1 = browser.find_element(By.ID, "num1")
    str_perem1 = perem1.text
    perem2 = browser.find_element(By.ID, "num2")
    str_perem2 = perem2.text
    y=int(str_perem1)+int(str_perem2)
    
    y_str=str(y)
    
    select = Select(browser.find_element(By.TAG_NAME, "select")) #открываем список
    select.select_by_value(y_str) # ищем элемент с суммой
    
      
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
