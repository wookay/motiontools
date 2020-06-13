import unittest
from motiontools import repeat

class AbstractArrayMathTestCase(unittest.TestCase):

  def test_repeat(self):
    self.assertEqual([3] * 2, [3, 3])
    self.assertEqual(repeat([3], 2), [3, 3])
    self.assertEqual(repeat([3, 4], 2), [3, 4, 3, 4])
