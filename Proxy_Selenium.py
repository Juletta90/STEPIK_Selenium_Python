# Мы можем узнать свой IP на сайте 2ip.ru.
# Выполните код ниже, чтобы увидеть принт с  вашим IP адресом.

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://2ip.ru/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)


# Теперь модифицируем данный код, чтобы запрос отправлялся через прокси.
# Прокси должен быть вида IP:PORT

# proxy = '8.210.83.33:80'
# url = 'https://2ip.ru/'
# chrome_options = webdriver.ChromeOptions()


#  передали параметр '--proxy-server=%s' % proxy методу .add_argument() в
#  класс дополнительных опций .ChromeOptions() и передали сам прокси,
#  который лежал в переменной proxy.
# chrome_options.add_argument('--proxy-server=%s' % proxy)
#
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)




# Подобно requests,  мы можем установить timeout= для загрузки страницы,
# после истечению которого произойдет, либо закрытие окна,
# либо переход к следующему прокси.

# В этом примере, есть список прокси proxy_list, по которому мы итерируемая
# в цикле for, передавая на каждой итерации в переменную PROXY,
# следующий IP из этого списка. Мы применили конструкцию try/except,
# чтобы наш скрипт не падал с ошибкой, и продолжал работать.
# Если не обернуть код в try/except, мы после каждого истекшего timeout= мы
# будем получать ошибку:
# Message: unknown error: net::ERR_TUNNEL_CONNECTION_FAILED.
#
# timeout в Selenium применяется методом .set_page_load_timeout(5)
# где цифра 5 длительность в секундах.

from selenium import webdriver
from selenium.webdriver.common.by import By

proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
'103.151.246.38:10001', '199.60.103.228:80',
'199.60.103.228:80', '199.60.103.28:80', ]

for PROXY in proxy_list:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        url = 'https://2ip.ru/'

        with webdriver.Chrome(options=chrome_options) as browser:
            browser.get(url)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

            browser.set_page_load_timeout(5)

            proxy_list.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue

