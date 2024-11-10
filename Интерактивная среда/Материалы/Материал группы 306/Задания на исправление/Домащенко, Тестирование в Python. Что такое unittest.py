import degree_programm
import unittest

class TestDegreeMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(degree_programm.degree(2, 3), 8)

input()