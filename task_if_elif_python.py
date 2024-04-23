import unittest

# Задача 1: Проверка существования треугольника по его сторонам
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Треугольник существует."
    else:
        return "Треугольник не существует."

# Задача 2: Проверка существования и типа треугольника по двум углам
def triangle_type_by_angles(angle1, angle2):
    if angle1 + angle2 < 180:
        if angle1 == 90 or angle2 == 90 or angle1 + angle2 == 90:
            return "Треугольник существует и он прямоугольный."
        return "Треугольник существует, но он не прямоугольный."
    return "Такой треугольник не существует."

# Задача 3: Определение возрастной группы котов
def cat_age_group(age):
    if age <= 1:
        return 'Котята'
    elif 1 < age <= 3:
        return 'Молодые коты'
    elif 3 < age <= 7:
        return 'Коты средних лет'
    else:
        return 'Почтенные коты'

# Задача 4: Анализ чисел
def analyze_number(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)

# Задача 5: Проверка на переполнение
def check_overflow(a, b):
    result = a + b
    if result > 32767:
        return "Происходит переполнение."
    return f"Сумма чисел: {result}"

# Задача 6: Проход кирпича через отверстие
def brick_fits(a, b, x, y, z):
    dimensions = sorted([x, y, z])
    hole = sorted([a, b])
    if dimensions[0] <= hole[0] and dimensions[1] <= hole[1]:
        return "Кирпич пройдет через отверстие."
    return "Кирпич не пройдет через отверстие."

# Вывод результатов тестов в консоль
def print_results():
    print(is_triangle(3, 4, 5))
    print(triangle_type_by_angles(45, 90))
    print(cat_age_group(4))
    print(analyze_number(15))
    print(check_overflow(20000, 13000))
    print(brick_fits(8, 4, 9, 3, 2))
"""
class TestGeometricCalculations(unittest.TestCase):

    def test_is_triangle(self):
        self.assertEqual(is_triangle(3, 4, 5), "Треугольник существует.")
        self.assertEqual(is_triangle(1, 2, 3), "Треугольник не существует.")

    def test_triangle_type_by_angles(self):
        self.assertEqual(triangle_type_by_angles(45, 45), "Треугольник существует, но он не прямоугольный.")
        self.assertEqual(triangle_type_by_angles(90, 90), "Такой треугольник не существует.")  
        self.assertEqual(triangle_type_by_angles(90, 30), "Треугольник существует и он прямоугольный.")

    def test_cat_age_group(self):
        self.assertEqual(cat_age_group(0.5), 'Котята')
        self.assertEqual(cat_age_group(2), 'Молодые коты')
        self.assertEqual(cat_age_group(5), 'Коты средних лет')
        self.assertEqual(cat_age_group(8), 'Почтенные коты')

    def test_analyze_number(self):
        self.assertEqual(analyze_number(3), 'Fizz')
        self.assertEqual(analyze_number(5), 'Buzz')
        self.assertEqual(analyze_number(15), 'FizzBuzz')
        self.assertEqual(analyze_number(7), '7')

    def test_check_overflow(self):
        self.assertEqual(check_overflow(16000, 17000), "Происходит переполнение.")
        self.assertEqual(check_overflow(1000, 2000), "Сумма чисел: 3000")

    def test_brick_fits(self):
        self.assertEqual(brick_fits(8, 4, 9, 3, 2), "Кирпич не пройдет через отверстие.")
        self.assertEqual(brick_fits(8, 4, 3, 2, 1), "Кирпич пройдет через отверстие.")
"""
if __name__ == '__main__':
    print_results()
#    unittest.main()

