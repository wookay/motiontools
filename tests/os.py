import unittest
import types

class OsTestCase(unittest.TestCase):

  def test_os_path(self):
    import os
    self.assertTrue(isinstance(os.path.expanduser, types.FunctionType))
