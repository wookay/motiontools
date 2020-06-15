import unittest
from motiontools import normpath, dir_of_file
import os

class PathTestCase(unittest.TestCase):

  def test_dir_of_file(self):
    d = dir_of_file()
    self.assertEqual(os.path.basename(d), "tests")

  def test_normpath(self):
    self.assertEqual(normpath("a", "b"), "a/b")
