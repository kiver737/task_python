import unittest
from math import sqrt, pi

def right_triangle_perimeter_and_area(a, b):
    perimeter = a + b + sqrt(a**2 + b**2)
    area = 0.5 * a * b
    return perimeter, area

def circle_length_and_area(radius):
    circumference = 2 * pi * radius
    area = pi * radius**2
    return circumference, area

def area_from_circumference(circumference):
    radius = circumference / (2 * pi)
    area = pi * radius**2
    return area

def triangle_perimeter_and_area(x1, y1, x2, y2, x3, y3):
    side1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side2 = sqrt((x3 - x2)**2 + (y3 - y2)**2)
    side3 = sqrt((x1 - x3)**2 + (y1 - y3)**2)
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    area = sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return perimeter, area

def equilateral_triangle_metrics(side):
    area = (sqrt(3) / 4) * side**2
    height = (sqrt(3) / 2) * side
    circumradius = (side * sqrt(3)) / 3
    inradius = (side * sqrt(3)) / 6
    return area, height, circumradius, inradius

# Юнит тесты
class TestGeometryTasks(unittest.TestCase):
    def test_right_triangle_perimeter_and_area(self):
        self.assertEqual(right_triangle_perimeter_and_area(3, 4), (12, 6))

    def test_circle_length_and_area(self):
        self.assertAlmostEqual(circle_length_and_area(1)[0], 2 * pi)
        self.assertAlmostEqual(circle_length_and_area(1)[1], pi)

    def test_area_from_circumference(self):
        self.assertAlmostEqual(area_from_circumference(2 * pi), pi)

    def test_triangle_perimeter_and_area(self):
        self.assertAlmostEqual(triangle_perimeter_and_area(0, 0, 4, 0, 0, 3)[0], 12)
        self.assertAlmostEqual(triangle_perimeter_and_area(0, 0, 4, 0, 0, 3)[1], 6)

    def test_equilateral_triangle_metrics(self):
        self.assertAlmostEqual(equilateral_triangle_metrics(2)[0], sqrt(3))
        self.assertAlmostEqual(equilateral_triangle_metrics(2)[1], sqrt(3))

if __name__ == "__main__":
    unittest.main()

