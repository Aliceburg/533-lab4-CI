import unittest
import math
from geometry.description import compare, shape,size
from geometry.calculation.rectangle_cal import Rectangle
from geometry.calculation.round_cal import Round


class TestShape(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n====This is the beginning of the test for module test_shape====')


    @classmethod
    def tearDownClass(cls):
        print('\n====This is the end of the test for module test_shape====')


    def setUp(self):
        self.a = Round(5)
        self.b = Round(6)
        self.c = Rectangle(1,1)
        self.d = Round(5)
        self.e = Rectangle(1,2)
        self.f = Rectangle(3,4)

    def tearDown(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None


    def test_round_to_square(self):

        self.assertEqual(type(shape.round_to_square(self.a)),Rectangle)
        self.assertEqual(type(shape.round_to_square(self.b)),Rectangle)
        self.assertEqual(type(shape.round_to_square(self.d)),Rectangle)
        self.assertAlmostEqual(shape.round_to_square(self.a).area,math.pi*25)
        self.assertAlmostEqual(shape.round_to_square(self.b).area,math.pi*36)

    def test_square_to_round(self):

        self.assertEqual(type(shape.square_to_round(self.c)),Round)
        self.assertEqual(type(shape.square_to_round(self.e)),Round)
        self.assertEqual(type(shape.square_to_round(self.f)),Round)
        self.assertAlmostEqual(shape.square_to_round(self.c).radius,math.sqrt(1/math.pi))
        self.assertAlmostEqual(shape.square_to_round(self.e).area,2)

    def test_round_to_rect(self):

        self.assertEqual(type(shape.round_to_rect(self.a,2)),Rectangle)
        self.assertEqual(type(shape.round_to_rect(self.b,2)),Rectangle)
        self.assertEqual(type(shape.round_to_rect(self.d,2)),Rectangle)
        self.assertEqual(shape.round_to_rect(self.a,2).short_len,2)
        self.assertAlmostEqual(shape.round_to_rect(self.a,4).area,25*math.pi)
