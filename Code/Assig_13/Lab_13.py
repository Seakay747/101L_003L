########################################################################
##
## CS 101 Lab
## Program #13
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that uses unit testing to check math functions
##
## ALGORITHM : 
##      1. Set up the imports and function library
##      2. Set up functions in the function library
##      3. Set up the unit testing and error handeling
## 
## ERROR HANDLING:
##      coords must be coords, colors must be colors
##
## OTHER COMMENTS:
##      Any special comments
##              
######################################################################## 

import unittest
import math
from Grades_13 import *

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    def test_total_returns_zero(self):
        result = total([])
        self.assertEqual(result,0,"The total function should return 0")
    def test_average_one(self):
        result = average([2,5,9])
        self.assertAlmostEqual(result,5.33333,5,"The average should return 5 and 1/3")
    def test_average_two(self):
        result = average([2,15,22,9])
        self.assertAlmostEqual(result,12.0000,4,"The average should return 12")
    def test_average_returns_nan(self):
        result = average([])
        self.assertIs(result,math.nan,"The average should return nan")
    def test_median_returns_one(self):
        result = median([2,5,1])
        self.assertEqual(result,2,"The median should return 2")
    def test_median_returns_two(self):
        result = median([5,2,1,3])
        self.assertAlmostEqual(result,2.5,1,"The median should return 2.5")
    def test_median_raise_error(self):
        with self.assertRaises(ValueError):
            result = median([])
if __name__ == '__main__':
    unittest.main()