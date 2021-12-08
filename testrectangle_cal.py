import unittest
import math
from geometry.calculation import graphic, rectangle_cal, round_cal
from geometry.calculation.rectangle_cal import Rectangle
from geometry.calculation.round_cal import Round

class TestRectangleCal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n====This is the beginning of the test for module rectangle_cal====')

    @classmethod
    def tearDownClass(cls):
        print('\n====This is the end of the test for module rectangle_cal====')

    def setUp(self):
        self.a = Rectangle(1,2)
        self.b = Rectangle(3,4)
        self.c = Rectangle(5,6)
        self.d = Rectangle(7,8)
        self.e = Rectangle(9,10)

    def tearDown(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None

    def test_cal_perimeter(self):
#        a = Rectangle(2,3)
        self.assertEqual(self.a.cal_perimeter(), 6)
        self.assertEqual(self.b.cal_perimeter(), 14)
        self.assertEqual(self.c.cal_perimeter(), 22)
        self.assertEqual(self.d.cal_perimeter(), 30)
        self.assertEqual(self.e.cal_perimeter(), 38)

    def test_cal_area(self):
#        b = Rectangle(4,5)
        self.assertEqual(self.a.cal_area(), 2)
        self.assertEqual(self.b.cal_area(), 12)
        self.assertEqual(self.c.cal_area(), 30)
        self.assertEqual(self.d.cal_area(), 56)
        self.assertEqual(self.e.cal_area(), 90)

    def test_cal_area_circumcircle(self):
#        c = Rectangle(3,4)
        self.assertEqual(self.a.cal_area_circumcircle(), math.pi*1.25)
        self.assertEqual(self.b.cal_area_circumcircle(), math.pi*6.25)
        self.assertEqual(self.c.cal_area_circumcircle(), math.pi*15.25)
        self.assertEqual(self.d.cal_area_circumcircle(), math.pi*28.25)
        self.assertEqual(self.e.cal_area_circumcircle(), math.pi*45.25)
