from rabbit import answer
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_returns_correct_string(self):
        self.assertEqual(answer(["annie", "bonnie", "liz"]),["bonnie", "liz", "annie"])

    def test_returns_correct_string(self):
        self.assertEqual(answer(["abcdefg", "vi"]),["vi", "abcdefg"])

    def test_returns_correct_string(self):
        self.assertEqual(answer(["abcdefg", "vi", "vi", "vi"]),["vi", "vi", "vi", "abcdefg"])

    def test_returns_correct_string(self):
        self.assertEqual(answer(["abcdefg", "vi", "lmb", "vi", "vi", "lmb", "lmb"]),["vi", "vi", "vi", "abcdefg", "lmb", "lmb", "lmb"])

    def test_returns_correct_string(self):
        self.assertEqual(answer(["abcdefg", "vi", "lmb", "vi", "vi", "lmb", "lmb", "fmb", "hello", "checkout"]),["checkout", "hello", "vi", "vi", "vi", "abcdefg", "lmb", "lmb", "lmb", "fmb"])

    def test_returns_correct_string(self):
        self.assertEqual(answer(["az", "by", "cx", "az", "by", "cx"]), ['cx', 'cx', 'by', 'by', 'az', 'az'])

if __name__ == '__main__':
    unittest.main(exit=False)
