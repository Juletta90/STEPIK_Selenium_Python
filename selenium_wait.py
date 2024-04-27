from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# https://github.com/Juletta90/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/using_selenium_tests.py


# o = Options()
# o.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=o)
# driver.get('https://www.selenium.dev/selenium/web/web-form.html')

# def test_eight_components():
#     o = Options()
#     o.add_experimental_option("detach", True)
#
#     # WebDriver waits for all resources to download
#     o.page_load_strategy = 'normal'
#     o.add_experimental_option("excludeSwitches",
#                               ['enable-automation'])
#     driver = webdriver.Chrome(options=o)
#
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#
#     title = driver.title
#     assert title == "Web form"
#
#     driver.implicitly_wait(2)
#
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
#     text_box.send_keys("Selenium")
#     submit_button.click()
#
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

# driver.quit()


# def test_eight_components():
#     driver = webdriver.Chrome()
#
#     driver.implicitly_wait(5)
#
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#
#     driver.implicitly_wait(10)
#
#     title = driver.title
#     assert title == "Web form"
#
#     driver.implicitly_wait(10)
#
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
#     driver.implicitly_wait(5)
#
#     text_box.send_keys("Selenium")
#
#     driver.implicitly_wait(5)
#
#     submit_button.click()
#
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"
#
#     driver.quit()


"""
Задачи из курса Stepik
раздел 3.4 - задачи по материалу
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


""" Задача 1  Мастер заполнения форм
Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
Сканирование: Используйте метод .find_elements() для поиска всех доступных полей для ввода на странице.
Ввод данных: В цикле, переберите все найденные поля и заполните их с помощью метода .send_keys("Текст").
Инициация: Найдите кнопку на странице и нажмите на неё.
Результат: Скопируйте текст, который появится на экране рядом с кнопкой, если вы уложились в трёх секундный интервал.
Фиксация: Запишите результат в отдельную переменную или вставьте ответ в поле ответа степик.
 """

# options = webdriver.ChromeOptions()
# options.add_argument('--window-size=1920,1080')
# url = 'https://parsinger.ru/selenium/1/1.html'
#
# with webdriver.Chrome(options=options) as driver:
#     wait = WebDriverWait(driver, 15)
#     driver.get(url)
#     for item in driver.find_elements('xpath', '//input[@class="form"]'):
#         item.send_keys('Текст')
#
#     wait.until(ec.element_to_be_clickable(driver.find_element('id', 'btn'))).click()
#     time.sleep(30)



""" Задача 2  Охотник за Сокровищами
Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
Поиск Ссылки: Используйте метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT для поиска ссылки с текстом 16243162441624.
Клик по Ссылке: Нажмите на найденную ссылку.
Получение Результата: Скопируйте текст, который появится в теге найденной страницы <p id="result"></p>.
Фиксация: Запишите полученный результат в отдельную переменную или вставьте ответ в поле ответа степик.
"""

# options = webdriver.ChromeOptions()
# options.add_argument('--window-size=1920,1080')
# url = 'https://parsinger.ru/selenium/2/2.html'
#
# with webdriver.Chrome(options=options) as driver:
#     wait = WebDriverWait(driver, 15)
#     driver.get(url)
#     wait.until(ec.element_to_be_clickable((
#         By.LINK_TEXT, '16243162441624'))).click()
#
#     link_text = driver.find_element(By.ID, 'result').text
#     print(link_text)



""" Задача 3  Кодекс Охотников за Цифрами
Вход в Лабиринт: Откройте указанный веб-сайт с помощью Selenium.
Ключи к Сокровищам: Извлеките данные из каждого тега <p> на странице.
Сложение Фрагментов: Просуммируйте все числовые значения, которые вы извлекли.
Отчет о Сокровищах: Запишите сумму в отдельное поле или выведите на экран, полученное значение вставьте в поле ответа степик.
"""

# алгоритм такой: ищем все теги 'p' с помощью "найти элементы" и получим список этих тегов.
# Потом в цикле к каждому из них обращаемся и говорим "отдай текст".
# Не забываем этот текст рассматривать как числа. Всё сие плюсуем и можно в
# консоли распечатать для наглядности.


# # Вариант 1
# with webdriver.Chrome() as browser:
#     browser.get('https://stepik-parsing.ru/selenium/3/3.html')
#
#     result = [int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p")]
#     print(sum(result))
#
#
# # Вариант 2
# url = 'https://parsinger.ru/selenium/3/3.html'
#
# with webdriver.Chrome() as driver:
#     driver.get(url)
#     elements = driver.find_elements(By.TAG_NAME, "p")
#     s = 0
#     for element in elements:
#         s += int(element.text)
#     print(s)


# Мой вариант
# options = webdriver.ChromeOptions()
# options.add_argument('--window-size=1920,1080')
# url = 'https://parsinger.ru/selenium/3/3.html'

# with webdriver.Chrome(options=options) as driver:
#     wait = WebDriverWait(driver, 15)
#     driver.get(url)
#     elements = driver.find_elements(By.TAG_NAME, 'p')  # получим список
#
#     for element in elements:
#         val = int(element.text)
#         sum_val = sum_val + val
#     print(sum_val)



""" Задача 4  Поход за сокровищами в Цифровом Лабиринте
Вход в Цифровой Лабиринт: Используйте Selenium для открытия указанного веб-сайта.
Извлечение Фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
Воссоздание Артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
Ключ к Загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.
"""

# url = 'https://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     result = [int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]
#     print(sum(result))




""" Задача 5  Операция 'Кодовый Замок'
Взлом Кодового Замка: Откройте веб-сайт с помощью Selenium.
Активация Чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
Открывание Секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
Доступ к Секретным Данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.
"""

# url = 'https://parsinger.ru/selenium/4/4.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.click()
#
#     browser.find_element(By.CLASS_NAME, "btn_box").click()  # нашли кнопку, нажали
#     res = browser.find_element(By.TAG_NAME, "p").text
#     print(res)



""" Задача 6   Кодовая Одиссея
Приземление на Острове Чек-боксов: Откройте сайт, на котором вас ждут эти загадочные чек-боксы.
Отбор ценных чек-боксов: С помощью Selenium и метода click() установите в положение checked только те чек-боксы, значение атрибута value которых есть в заданном списке numbers.
Открытие Сундука: Как только все нужные чек-боксы активны, кнопка станет активной. Нажмите на неё.
Извлечение Сокровища: После нажатия на кнопку, результат появится в теге <p id="result">Result</p>. Скопируйте это значение и вставьте полученный код в поле ответа степик.
"""

# numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
#            39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
#            74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
#            119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
#            154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
#            187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
#            208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
#            234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
#            256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
#            292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
#            318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
#            353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
#            419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
#            452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
#            480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
#
#
# # Мой вариант:
# url = 'https://parsinger.ru/selenium/5/5.html'
# with webdriver.Chrome() as browser:
#     wait = WebDriverWait(browser, 15)
#     browser.get(url)
#     checkbox = browser.find_elements(By.CLASS_NAME, "check")
#     for element in checkbox:
#         values = element.get_attribute('value')  # value возвращает строку, а в списке numbers - числа
#         if int(values) in numbers:
#             element.click()
#
#     wait.until(ec.element_to_be_clickable(browser.find_element(
#         By.CLASS_NAME, "btn"))).click()
#
#     res = browser.find_element(By.TAG_NAME, "p").text
#     print(res)
#
#
# # Вариант 2:
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/5/5.html')
#     [x.click() for n, x in enumerate(browser.find_elements(
#         By.CLASS_NAME, 'check'), start=1) for y in numbers if y == n]
#     time.sleep(5)
#
#
# # Вариант 3:
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/5/5.html')
#     [x.click() for x in browser.find_elements(
#         By.CLASS_NAME, 'check') if int(x.get_attribute('value')) in numbers]
#     browser.find_element(By.CLASS_NAME, 'btn').click()
#     print(browser.find_element(By.ID, 'result').text)




""" Задача 7   Операция "Выпадающие списки"
Вход в Кодовую Комнату: Откройте сайт с помощью Selenium.
Извлечение Ключей: Получите значения всех элементов выпадающего списка.
Дешифровка Кода: Сложите (плюсуйте) все извлеченные значения.
Использование Кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
Получение Конечного Результата: Копируйте длинное число, которое появится после нажатия на кнопку.
"""

url = 'https://parsinger.ru/selenium/7/7.html'
with webdriver.Chrome() as browser:
    wait = WebDriverWait(browser, 15)
    browser.get(url)

    # Нахождение элемента выпадающего списка
    for element in browser.find_elements(By.ID, "opt"):



    # dropdown = browser.find_elements(By.ID, "opt")
    # sum_val = 0
    # for element in dropdown:
    #     # Создание объекта класса Select
    #     select = Select(dropdown)
    #     #sum_val = sum_val + val
    # #print(sum_val)

    # input_text = browser.find_element(By.ID, "input_result")
    # input_text.send_keys(sum_val)

    wait.until(ec.element_to_be_clickable(browser.find_element(
        By.CLASS_NAME, "btn"))).click()

    res = browser.find_element(By.TAG_NAME, "p").text
    print(res)

