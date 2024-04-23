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


def print_results():
    # Задача 1: Проверка существования треугольника
    a = float(input('Введите сторону a треугольника: '))
    b = float(input('Введите сторону b треугольника: '))
    c = float(input('Введите сторону c треугольника: '))
    print(is_triangle(a, b, c))

    # Задача 2: Проверка существования и типа треугольника
    angle1 = float(input('Введите первый угол треугольника в градусах: '))
    angle2 = float(input('Введите второй угол треугольника в градусах: '))
    print(triangle_type_by_angles(angle1, angle2))

    # Задача 3: Определение возрастной группы котов
    age = float(input('Введите возраст кота: '))
    print(cat_age_group(age))

    # Задача 4: Анализ чисел
    number = int(input('Введите целое число: '))
    print(analyze_number(number))

    # Задача 5: Проверка на переполнение
    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))
    print(check_overflow(a, b))

    # Задача 6: Проход кирпича через отверстие
    a = float(input('Введите сторону A отверстия: '))
    b = float(input('Введите сторону B отверстия: '))
    x = float(input('Введите размер x кирпича: '))
    y = float(input('Введите размер y кирпича: '))
    z = float(input('Введите размер z кирпича: '))
    print(brick_fits(a, b, x, y, z))

if __name__ == '__main__':
    print_results()

