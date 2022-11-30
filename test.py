from test_2 import candy
import unittest

ratings = [1, 2, 2]


class SimplisticTest(unittest.TestCase):
    def test(self):
        self.assertTrue(candy(ratings), "Test")
        self.assertEqual(candy(ratings), 4, "Okay")


if __name__ == '__main__':
    unittest.main()
# main.addNums(6, 9)
# unittest.main.warnings
# print(var)
