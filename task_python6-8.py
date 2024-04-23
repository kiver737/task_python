import unittest
from math import sqrt, pi
import math

def digit_product(number):
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10
    return product

def inscribed_circle_area(a, b, c):
    # Полупериметр треугольника
    s = (a + b + c) / 2
    # Площадь треугольника по формуле Герона
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Радиус вписанной окружности
    radius = area / s
    # Площадь круга
    return math.pi * radius * radius

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return f"{hours}ч {minutes}мин {seconds}с"

# Вывод результатов в консоль
print("Произведение цифр числа 1234:", digit_product(1234))
print("Площадь круга, вписанного в треугольник со сторонами 2, 2, 2:", inscribed_circle_area(2, 2, 2))
print("Формат времени для 3661 секунды:", format_time(3661))



class TestGeometricCalculations(unittest.TestCase):
    def test_digit_product(self):
        self.assertEqual(digit_product(1234), 24)
        self.assertEqual(digit_product(4321), 24)

    def test_inscribed_circle_area(self):
        self.assertAlmostEqual(inscribed_circle_area(2, 2, 2), math.pi / 3, places=7)

    def test_format_time(self):
        self.assertEqual(format_time(3661), "1ч 1мин 1с")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)

