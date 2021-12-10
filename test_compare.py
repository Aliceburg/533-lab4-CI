import unittest
from geometry.description import compare, shape,size
from geometry.calculation.rectangle_cal import Rectangle
from geometry.calculation.round_cal import Round


class TestCompare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n====This is the beginning of the test for module test_compare====')


    @classmethod
    def tearDownClass(cls):
        print('\n====This is the end of the test for module test_compare====')


    def setUp(self):
        self.a = Round(5)
        self.b = Round(6)
        self.c = Rectangle(1,1)
        self.d = Round(5)
        self.e = 1

    def tearDown(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None


    def test_is_same_shape(self):
        self.assertEqual(compare.is_same_shape(self.a,self.b),True)
        self.assertEqual(compare.is_same_shape(self.a,self.c),False)
        self.assertEqual(compare.is_same_shape(self.b,self.c),False)
        self.assertEqual(compare.is_same_shape(self.a,self.d),True)
        self.assertEqual(compare.is_same_shape(self.b,self.d),True)
        

    def test_is_same(self):
        self.assertEqual(compare.is_same(self.d,self.a),True)
        self.assertEqual(compare.is_same(self.a,self.c),False)
        self.assertEqual(compare.is_same(self.a,self.b),False)
        self.assertEqual(compare.is_same(self.b,self.c),False)
        self.assertEqual(compare.is_same(self.b,self.d),False)
        self.assertEqual(compare.is_same(self.a,self.e),None)
        self.assertEqual(compare.is_same(self.e,self.b),None)
    def test_big_area(self):
        self.assertEqual(compare.big_area(self.a,self.b),self.b)
        self.assertEqual(compare.big_area(self.a,self.d),None)
        self.assertEqual(compare.big_area(self.a,self.c),self.a)
        self.assertEqual(compare.big_area(self.c,self.d),self.d)
        self.assertEqual(compare.big_area(self.b,self.d),self.b)
        self.assertEqual(compare.big_area(self.e,self.d),None)
        self.assertEqual(compare.big_area(self.c,self.e),None)