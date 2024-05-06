# Мы можем узнать свой IP на сайте 2ip.ru.
# Выполните код ниже, чтобы увидеть принт с  вашим IP адресом.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://2ip.ru/'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(5)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)


# Теперь модифицируем данный код, чтобы запрос отправлялся через прокси.
# Прокси должен быть вида IP:PORT

proxy = '8.210.83.33:80'
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()

#  передали параметр '--proxy-server=%s' % proxy методу .add_argument() в
#  класс дополнительных опций .ChromeOptions() и передали сам прокси,
#  который лежал в переменной proxy.
chrome_options.add_argument('--proxy-server=%s' % proxy)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)
