import unittest
import math
from geometry.calculation import graphic, rectangle_cal, round_cal
from geometry.calculation.rectangle_cal import Rectangle
from geometry.calculation.round_cal import Round

class TestRoundCal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n====This is the beginning of the test for module round_cal====')

    @classmethod
    def tearDownClass(cls):
        print('\n====This is the end of the test for module round_cal====')

    def setUp(self):
        self.a = Round(1)
        self.b = Round(2)
        self.c = Round(3)
        self.d = Round(4)
        self.e = Round(5)
        self.f = Round(-5)

    def tearDown(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None

    def test_cal_perimeter(self):
#        a = Round(3)
        self.assertEqual(self.a.cal_perimeter(), 2*math.pi)
        self.assertEqual(self.b.cal_perimeter(), 4*math.pi)
        self.assertEqual(self.c.cal_perimeter(), 6*math.pi)
        self.assertEqual(self.d.cal_perimeter(), 8*math.pi)
        self.assertEqual(self.e.cal_perimeter(), 10*math.pi)
        self.assertEqual(self.f.cal_perimeter(), None)


    def test_cal_area(self):
#        b = Round(4)
        self.assertEqual(self.a.cal_area(), 1*math.pi)
        self.assertEqual(self.b.cal_area(), 4*math.pi)
        self.assertEqual(self.c.cal_area(), 9*math.pi)
        self.assertEqual(self.d.cal_area(), 16*math.pi)
        self.assertEqual(self.e.cal_area(), 25*math.pi)

    def test_cal_area_ins_square(self):
#        c = Round(5)
        self.assertEqual(self.a.cal_area_ins_square(), 2)
        self.assertEqual(self.b.cal_area_ins_square(), 8)
        self.assertEqual(self.c.cal_area_ins_square(), 18)
        self.assertEqual(self.d.cal_area_ins_square(), 32)
        self.assertEqual(self.e.cal_area_ins_square(), 50)
