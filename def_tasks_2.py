from functools import reduce
import math
import unittest

# Задание 5: НОД произвольного количества чисел
def gcd(*numbers):
    def find_gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return reduce(find_gcd, numbers)

# Задание 6: НОК трех натуральных чисел
def lcm_of_three(a, b, c):
    def lcm(x, y):
        return x * y // gcd(x, y)
    return lcm(lcm(a, b), c)

# Задание 7: НОК произвольного количества натуральных чисел
def lcm(*numbers):
    return reduce(lambda a, b: a * b // gcd(a, b), numbers)

# Задание 8: Проверка на взаимную простоту трех чисел
def are_coprime(*numbers):
    return gcd(*numbers) == 1

# Пример использования
if __name__ == "__main__":
    # Задание 5 - НОД произвольного количества чисел
    print(f"НОД чисел (60, 72, 120): {gcd(60, 72, 120)}")
    
    # Задание 6 - НОК трех натуральных чисел
    print(f"НОК чисел (6, 8, 12): {lcm_of_three(6, 8, 12)}")
    
    # Задание 7 - НОК произвольного количества натуральных чисел
    print(f"НОК чисел (6, 8, 12, 14): {lcm(6, 8, 12, 14)}")
    
    # Задание 8 - Проверка на взаимную простоту
    print(f"Числа (35, 64, 13) взаимно простые: {are_coprime(35, 64, 13)}")
    #unittest.main()


"""
class TestMathFunctions(unittest.TestCase):

    def test_gcd_multiple_numbers(self):
        self.assertEqual(gcd(60, 72, 120), 12)
        self.assertEqual(gcd(20, 100), 20)
        self.assertEqual(gcd(17), 17)

    def test_lcm_of_three(self):
        self.assertEqual(lcm_of_three(6, 8, 12), 24)
        self.assertEqual(lcm_of_three(1, 3, 5), 15)
        self.assertEqual(lcm_of_three(7, 11, 13), 7 * 11 * 13)

    def test_lcm_multiple_numbers(self):
        self.assertEqual(lcm(6, 8, 12, 14), 168)
        self.assertEqual(lcm(4, 5, 10), 20)
        self.assertEqual(lcm(21, 6), 42)

    def test_are_coprime(self):
        self.assertTrue(are_coprime(35, 64, 13))
        self.assertFalse(are_coprime(6, 8, 12))
        self.assertTrue(are_coprime(17, 31, 43))
"""
