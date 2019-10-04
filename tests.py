import unittest
from suggest import Suggester


class SuggesterTest (unittest.TestCase):
    def setUp(self):
        self.suggester = Suggester ("ruwords.txt")

    def test_get_find_anything(self):
        result = self.suggester.get("аббат")
        self.assertGreater(len(result), 0)

    def test_get_find_too_more(self):
        result = self.suggester.get("a")
        self.assertEqual(len(result), 10)

    def test_get_empty_word(self):
        result = self.suggester.get("")
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main ()
