import unittest
import math
from geometry.description import compare, shape,size
from geometry.calculation.rectangle_cal import Rectangle
from geometry.calculation.round_cal import Round
class TestSize(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n====This is the beginning of the test for module test_size====')

    @classmethod
    def tearDownClass(cls):
        print('\n====This is the end of the test for module test_size====')


    def setUp(self):
        self.a = Round(5)
        self.b = Round(6)
        self.c = Rectangle(1,2)
        self.d = Rectangle(5,10)
        self.e = 1

    def tearDown(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None


    def test_change_side_for_rec(self):

        self.assertEqual(size.change_side_for_rec(self.a,"long",3),None)
        self.assertEqual(size.change_side_for_rec(self.c,"error",3),None)
        self.assertEqual(size.change_side_for_rec(self.c,"long",3).long_len,5)
        self.assertEqual(size.change_side_for_rec(self.c,"short",3).short_len,4)
        self.assertEqual(size.change_side_for_rec(self.c,"long",-1).long_len,1)
        self.assertEqual(size.change_side_for_rec(self.c,"long",-5),None)
        self.assertEqual(size.change_side_for_rec(self.c,"short",-15),None)
        self.assertEqual(size.change_side_for_rec(self.c,"short",0).short_len,1)

    def test_change_radius_for_round(self):
        self.assertEqual(size.change_radius_for_round(self.c,3),None)
        self.assertEqual(size.change_radius_for_round(self.a,3).radius,8)
        self.assertEqual(size.change_radius_for_round(self.b,3).radius,9)
        self.assertEqual(size.change_radius_for_round(self.a,-3).radius,2)
        self.assertEqual(size.change_radius_for_round(self.a,0).radius,5)
        self.assertEqual(size.change_radius_for_round(self.b,-10),None)

    def test_change_area(self):
        self.assertEqual(size.change_area(self.e,4),None)
        self.assertEqual(size.change_area(self.a,-150),None)
        self.assertEqual(size.change_area(self.a,1).area,math.pi*25+1)
        self.assertEqual(size.change_area(self.c,4).area,6)
        self.assertEqual(size.change_area(self.d,4).area,54)
        self.assertEqual(size.change_area(self.d,-4).area,46)
        self.assertEqual(size.change_area(self.c,-10),None)
        self.assertEqual(size.change_area(self.c,0).area,2)
