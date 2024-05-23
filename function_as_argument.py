def talk(say):
    prt = say('Мир')
    print(prt)


def hello(name):
    return f'Привет {name}.'


def goodbye(name):
    return f'Пока {name}.'


talk(hello)  # Привет Мир.
talk(goodbye)  # Пока Мир.

# https://docs-python.ru/tutorial/opredelenie-funktsij-python/peredacha-funktsii-drugoj-funktsii/




def calculate(a, b, operation):
    result = operation(a, b)
    print(result)


def summa(a, b):
    return a + b


def multiply(a, b):
    return a * b


calculate(2, 3, summa)  # 5
calculate(3, 4, multiply)  # 12
