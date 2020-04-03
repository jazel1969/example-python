import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")

    def test_two(self):
        self.assertEqual(awesome.frown(), ":(")
    
    def test_two3(self):
        self.assertEqual(awesome.frown(), ":(")

if __name__ == '__main__':
    unittest.main()
