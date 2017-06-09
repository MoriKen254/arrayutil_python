#!/usr/bin/env python
import sys
import os
import unittest
import rostest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../script')
import arrayutil_python_sub as sub


class ArrayUtilPythonTest(unittest.TestCase):
  def setUp(self):
    self.test_array = [1.7, 2.3, 3.2, 4.8]
    self.answer_sum = 12.0
    self.answer_ave = 3.0
    self.answer_min = 1.7
    self.answer_max = 4.8

  def test_sum(self):
    sum_instance = sub.Sum()
    sum_instance.setArray(self.test_array)
    result = sum_instance.operate()
    self.assertEquals(result, self.answer_sum, "Sum test")

  def test_ave(self):
    ave_instance = sub.Ave()
    ave_instance.setArray(self.test_array)
    result = ave_instance.operate()
    self.assertEquals(result, self.answer_ave, "Ave test")

  def test_min(self):
    min_instance = sub.Min()
    min_instance.setArray(self.test_array)
    result = min_instance.operate()
    self.assertEquals(result, self.answer_min, "Min test")

  def test_max(self):
    max_instance = sub.Max()
    max_instance.setArray(self.test_array)
    result = max_instance.operate()
    self.assertEquals(result, self.answer_max, "Max test")


if __name__ == '__main__':
  package_name = 'arrayutil_python'
  test_name = 'arrayutil_python_test'
  rostest.run(package_name, test_name, ArrayUtilPythonTest)