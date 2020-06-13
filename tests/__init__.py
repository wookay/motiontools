import os.path
import unittest


def get_tests():
    return full_suite()

def full_suite():
    from .motiontools import MotionToolsTestCase

    suite = unittest.TestLoader().loadTestsFromTestCase(MotionToolsTestCase)
    return unittest.TestSuite([suite])
