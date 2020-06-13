import unittest
from pkg_resources import parse_version
import types
import motiontools

class MotionToolsTestCase(unittest.TestCase):

  def test_motiontools(self):
    a = motiontools.MotionTools()
    self.assertEqual(type(a), motiontools.MotionTools)
    self.assertTrue(parse_version(motiontools.__version__) >= parse_version('0.0.1'))

  def test_int(self):
    self.assertEqual(3, 1+2)

  def test_type(self):
    def f():
      pass
    self.assertTrue(isinstance(f, types.FunctionType))
