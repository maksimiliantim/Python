# -*- coding: utf-8 -*-
class NumberProcessor:
    @staticmethod
    def sum_numbers(numbers):
        if not isinstance(numbers, list):
            raise TypeError("Аргумент должен быть списком.")
        if not all(isinstance(n, (int, float)) for n in numbers):
            raise ValueError("Список должен содержать только числа.")
        return sum(numbers)

