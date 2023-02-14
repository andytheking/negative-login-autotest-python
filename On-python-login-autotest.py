#сценарий негативного автотеста на вход в систему:
#открыть страницу
#ввести заведомо ложный email
#ввести заведомо ложный пароль с использованием спецсимволов
#нажать на кнопку входа
#получить ошибку доступа
#закрыть страницу

import time
from selenium import webdriver

dc = webdriver.Chrome()
dc.get("http://testerlaru.temp.swtest.ru/index.php?route=account/login")
dc.find_element("name", "email").send_keys('example@mail.com')
time.sleep(3)
dc.find_element("name", "password").send_keys('1a3@5_7')
time.sleep(3)
dc.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/form/input").click()
time.sleep(6)
dc.quit()