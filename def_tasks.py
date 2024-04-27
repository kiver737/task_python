import math
import unittest

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return 0
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def lcm(x, y):
    return x * y // gcd(x, y)

def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)


if __name__ == "__main__":
    # Задание 1 - Пример вычисления площади треугольника
    a, b, c = 3, 4, 5
    print(f"Площадь треугольника со сторонами {a}, {b}, {c} равна {triangle_area(a, b, c)}")

    # Задание 3 - Пример нахождения НОК
    x, y = 15, 20
    print(f"Наименьшее общее кратное чисел {x} и {y} равно {lcm(x, y)}")

    # Задание 4 - Пример нахождения НОД трех чисел
    d, e, f = 48, 64, 1024
    print(f"Наибольший общий делитель чисел {d}, {e} и {f} равен {gcd_three(d, e, f)}")

"""
class TestMathFunctions(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4, 5), 6)
        self.assertEqual(triangle_area(10, 10, 10), math.sqrt(3) * 25)
        self.assertEqual(triangle_area(0, 0, 0), 0)
        self.assertEqual(triangle_area(3, 7, 2), 0)

    def test_gcd(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(1071, 462), 21)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_lcm(self):
        self.assertEqual(lcm(21, 6), 42)
        self.assertEqual(lcm(8, 9), 72)
        self.assertEqual(lcm(0, 1), 0)
        self.assertEqual(lcm(7, 1), 7)

    def test_gcd_three(self):
        self.assertEqual(gcd_three(54, 24, 36), 6)
        self.assertEqual(gcd_three(12, 15, 21), 3)
        self.assertEqual(gcd_three(1071, 462, 21), 21)
        self.assertEqual(gcd_three(0, 0, 5), 5)


unittest.main()
"""
