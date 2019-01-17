#!/usr/bin/env python

import unittest
import pynance.dummy_test

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests(pynance.dummy_test.test_suite())

    return suite

def run_all_unit_tests():
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite())

if __name__ == "__main__":
    run_all_unit_tests()