def print_multiplication_table():
    print("Таблица умножения:")
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i * j:3}", end=" ")
        print()

def draw_rectangle(a, b):
    print("Прямоугольник из символов 'X':")
    for _ in range(b):
        print('X' * a)

def draw_custom_rectangle(a, b, border_char, fill_char):
    print("Прямоугольник с контуром и заливкой:")
    for i in range(b):
        if i == 0 or i == b - 1:
            print(border_char * a)
        else:
            print(border_char + fill_char * (a - 2) + border_char)

def find_primes(a, b):
    primes = []
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def find_perfect_numbers(limit=10000):
    perfect_numbers = []
    for num in range(2, limit):
        sum_divisors = sum(i for i in range(1, num) if num % i == 0)
        if sum_divisors == num:
            perfect_numbers.append(num)
    return perfect_numbers


print_multiplication_table()
draw_rectangle(4, 3)
draw_custom_rectangle(6, 4, 'O', '*')
print("Простые числа от 10 до 20:", find_primes(10, 20))
print("Совершенные числа до 10000:", find_perfect_numbers())

"""
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_multiplication_table(self):
        # Тест таблицы умножения на корректный вывод (сложно проверить без перехвата stdout)
        pass

    def test_draw_rectangle(self):
        expected_output = "XXXX\nXXXX\nXXXX\n"
        self.assertEqual(draw_rectangle(4, 3), expected_output)

    def test_draw_custom_rectangle(self):
        expected_output = "OOOOOO\nO****O\nO****O\nOOOOOO\n"
        self.assertEqual(draw_custom_rectangle(6, 4, 'O', '*'), expected_output)

    def test_find_primes(self):
        self.assertEqual(find_primes(10, 20), [11, 13, 17, 19])
        self.assertEqual(find_primes(1, 5), [2, 3, 5])

    def test_perfect_numbers(self):
        self.assertIn(6, find_perfect_numbers())
        self.assertIn(28, find_perfect_numbers())
        self.assertIn(496, find_perfect_numbers())
        self.assertIn(8128, find_perfect_numbers())

if __name__ == '__main__':
    unittest.main()
"""
