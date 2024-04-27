import unittest

def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

m = int(input("Введите первое число (M): "))
n = int(input("Введите второе число (N): "))
result = gcd(m, n)
print(f"Наибольший общий делитель чисел {m} и {n} равен {result}")

"""
class TestEuclidAlgorithm(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(10, 5), 5)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(21, 14), 7)
        self.assertEqual(gcd(14, 28), 14)
        self.assertEqual(gcd(100, 10), 10)
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(24, 36), 12)
        self.assertEqual(gcd(1071, 462), 21)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative(self):
        self.assertEqual(gcd(-10, -5), 5)
        self.assertEqual(gcd(-10, 5), 5)
        self.assertEqual(gcd(10, -5), 5)

if __name__ == '__main__':
    unittest.main()

"""
