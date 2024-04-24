def print_geometric_progression(start_number, multiplier, quantity):
    current_number = start_number
    for _ in range(quantity):
        print(current_number)
        current_number *= multiplier

start_number = int(input("Введите начальное число: "))
multiplier = int(input("Введите множитель: "))
quantity = int(input("Введите количество чисел: "))
print_geometric_progression(start_number, multiplier, quantity)


def sum_of_numbers(n):
    total_sum = sum(range(1, n+1))
    print(f"Сумма чисел от 1 до {n} равна {total_sum}")


n = int(input("Введите число n: "))
sum_of_numbers(n)


def product_of_even_numbers(n):
    product = 1
    for number in range(2, n + 1, 2):
        product *= number
    print(f"Произведение всех четных чисел от 1 до {n} равно {product}")

n = int(input("Введите число n: "))
product_of_even_numbers(n)


def calculate_total_distance():
    distance = 10  # начальное расстояние
    total = distance
    for _ in range(6):  # еще 6 дней
        distance *= 1.1  # увеличение на 10%
        total += distance
    print(f"Спортсмен пробежит за 7 дней: {total:.2f} км")

calculate_total_distance()


def find_animal_combinations(total_legs=64):
    for rabbits in range(total_legs // 4 + 1):
        geese = (total_legs - 4 * rabbits) // 2
        if 2 * geese + 4 * rabbits == total_legs:
            print(f"Кролики: {rabbits}, Гуси: {geese}")

find_animal_combinations()



"""
тесты
пример 1.1
import unittest

def geometric_progression(start_number, multiplier, quantity):
    result = []
    current_number = start_number
    for _ in range(quantity):
        result.append(current_number)
        current_number *= multiplier
    return result

class TestGeometricProgression(unittest.TestCase):
    def test_progression(self):
        self.assertEqual(geometric_progression(2, 3, 5), [2, 6, 18, 54, 162])
        self.assertEqual(geometric_progression(1, 2, 4), [1, 2, 4, 8])

if __name__ == '__main__':
    unittest.main()

"""
