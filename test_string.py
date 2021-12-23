import unittest
import string
from unittest import result

class Teststring(unittest.TestCase):

    def test_add(self):
        result = string.add("code","withTandora")
        self.assertEqual(result)
        