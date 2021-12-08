import unittest
import math
from geometry.calculation import graphic, rectangle_cal, round_cal
from geometry.calculation.rectangle_cal import Rectangle
from geometry.calculation.round_cal import Round

class TestGraphic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n====This is the beginning of the test for module graphic====')

    @classmethod
    def tearDownClass(cls):
        print('\n====This is the end of the test for module graphic====')

    def setUp(self):
        self.a = graphic.Graphic(1,2,3)
        self.b = graphic.Graphic(4,5,6)
        self.c = graphic.Graphic(7,8,9)
        self.d = graphic.Graphic(10,11,12)
        self.e = graphic.Graphic(13,14,15)

    def tearDown(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None

    def test_print_perimeter(self):
#        a = graphic.Graphic(1,2,3)
        self.assertEqual(self.a.print_perimeter(), 1)
        self.assertEqual(self.b.print_perimeter(), 4)
        self.assertEqual(self.c.print_perimeter(), 7)
        self.assertEqual(self.d.print_perimeter(), 10)
        self.assertEqual(self.e.print_perimeter(), 13)

    def test_print_area(self):
#        b = graphic.Graphic(4,5,6)
        self.assertEqual(self.a.print_area(), 2)
        self.assertEqual(self.b.print_area(), 5)
        self.assertEqual(self.c.print_area(), 8)
        self.assertEqual(self.d.print_area(), 11)
        self.assertEqual(self.e.print_area(), 14)

    def test_print_perimeter_and_area(self):
#        c = graphic.Graphic(7,8,3)
        self.assertEqual(self.a.print_perimeter_and_area(), (1, 2))
        self.assertEqual(self.b.print_perimeter_and_area(), (4, 5))
        self.assertEqual(self.c.print_perimeter_and_area(), (7, 8))
        self.assertEqual(self.d.print_perimeter_and_area(), (10, 11))
        self.assertEqual(self.e.print_perimeter_and_area(), (13, 14))
