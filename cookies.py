# В коде ниже использован метод .get_cookies(), который получает
# список всех cookie на странице.

from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    pprint(cookies)

    # мы можем в цикле for/in итерироваться по списку cookie, который мы
    # получили с помощью метода .get_cookies(). Этим способом мы можем
    # получить не только имя cookie, но и его значение.
    for cookie in cookies:
        print(cookie['name'])  # или cookie['value'] чтобы получить их значение

    # Когда мы знаем имена всех cookie на странице, мы можем получить нужные
    # нам данные по ключу. Мы помним, что .get_cookies() возвращает список словарей.
    # Если вы посмотрите на первый пример с кодом, вы увидите, что в cookie
    # хранится время экспирации 'expiry': 1685518907 т.е., время истечения
    # срока жизни cookie.
    # Пример кода ниже поможет нам извлечь конкретное значение из cookie.
    pprint(webdriver.get_cookie('sso_status')['name'])


