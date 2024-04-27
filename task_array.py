import unittest

def find_max_min(arr):
    if not arr:
        print("Массив пуст.")
        return
    max_val = min_val = arr[0]
    max_idx = min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    print(f"Максимальный элемент: индекс {max_idx}, значение {max_val}")
    print(f"Минимальный элемент: индекс {min_idx}, значение {min_val}")

def calculate_average(arr):
    if not arr:
        print("Массив пуст.")
        return
    total = 0
    for num in arr:
        total += num
    average = total / len(arr)
    print(f"Среднее арифметическое: {average}")

def transform_real_numbers(arr):
    transformed = []
    for num in arr:
        if num > 0:
            transformed.append(num ** 2)
        else:
            transformed.append(abs(num))
    print(f"Исходный массив: {arr}")
    print(f"Преобразованный массив: {transformed}")

def find_zero_indices(arr):
    indices = []
    for i in range(len(arr)):
        if arr[i] == 0:
            indices.append(i)
    print(f"Индексы нулевых элементов: {indices}")

def product_greater_than(arr, M):
    product = 1
    found = False
    for num in arr:
        if num > M:
            product *= num
            found = True
    if not found:
        print("Нет чисел больше заданного.")
    else:
        print(f"Произведение чисел, больших {M}: {product}")

def find_most_frequent_smallest_number(arr):
    if not arr:
        print("Массив пуст.")
        return
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = max(frequency.values())
    smallest_number = float('inf')
    for num, freq in frequency.items():
        if freq == max_freq and num < smallest_number:
            smallest_number = num
    print(f"Наиболее часто встречающееся наименьшее число: {smallest_number}")

if __name__ == "__main__":
    # З_1
    arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
    find_max_min(arr1)

    # З_2
    calculate_average(arr1)

    # З_3
    arr3 = [-3.5, 2.1, 0, -1.2, 3.3]
    transform_real_numbers(arr3)

    # З_4
    arr4 = [1, 0, 2, 0, 3, 0, 4]
    find_zero_indices(arr4)

    # З_5
    arr5 = [1, 5, 2, 6, 3, 7, 4, 8]
    M = int(input("Введите число M: "))
    product_greater_than(arr5, M)

    # З_6
    arr6 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5]
    find_most_frequent_smallest_number(arr6)

    #unittest.main() - запусе теста

"""
class TestMathFunctions(unittest.TestCase):
    def test_find_max_min(self):
        self.assertEqual(find_max_min([3, 1, 4, 1, 5, 9, 2, 6]), ((5, 9), (1, 1)))
        self.assertIsNone(find_max_min([]))

    def test_calculate_average(self):
        self.assertEqual(calculate_average([10, 20, 30, 40]), 25)
        self.assertIsNone(calculate_average([]))

    def test_transform_real_numbers(self):
        self.assertEqual(transform_real_numbers([-3.5, 2.1, 0, -1.2, 3.3]), ([-3.5, 2.1, 0, -1.2, 3.3], [3.5, 4.41, 0, 1.2, 10.89]))

    def test_find_zero_indices(self):
        self.assertEqual(find_zero_indices([1, 0, 2, 0, 3, 0, 4]), [1, 3, 5])

    def test_product_greater_than(self):
        self.assertEqual(product_greater_than([1, 5, 2, 6, 3, 7, 4, 8], 5), 336)
        self.assertIsNone(product_greater_than([1, 2, 3, 4], 5))

    def test_find_most_frequent_smallest_number(self):
        self.assertEqual(find_most_frequent_smallest_number([1, 2, 2, 3, 3, 3, 4, 4, 4, 5]), 3)
        self.assertIsNone(find_most_frequent_smallest_number([]))
"""
