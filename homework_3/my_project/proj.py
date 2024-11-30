# -*- coding: utf-8 -*-
from my_package.my_module import NumberProcessor
if __name__ == "__main__":
    numbers = [1, 2, 3, 4.5, 5]
    try:
        result = NumberProcessor.sum_numbers(numbers)
        print(f"Сумма чисел: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

