from src.calc import calculate


def test_calc_division(): # тестирование деления
    assert calculate(100, 100, '/') == 1
    
def test_calc_subtraction(): # тестирование вычитания
    assert calculate(1, 1, '-') == 0
#
def test_calc_multiplication(): # тестирование умножение
    assert calculate(17, 5, '*') == 85
#
def test_calc_addition(): # тестирование cложения
    assert calculate(2, 2, '+') == 4

def test_calc_division_null(): # тестирование деления на ноль
    assert calculate(1, 0, '/') == "Ошибка: деление на ноль!"

def test_calc_bad(): # тестирование неверной операции
    assert calculate(777, 99, '#') == "Неверная опреация"
