from src.calc import calculate


def test_calc_division(): # тестирование деления
    assert calculate(10, 5, '/') == 2

def test_calc_subtraction(): # тестирование вычитания
    assert calculate(47282, 342, '-') == 46940

def test_calc_multiplication(): # тестирование умножение
    assert calculate(23432, 908332, '*') == 21284035424

def test_calc_addition(): # тестирование cложение
    assert calculate(100, 200, '+') == 300
