#!/usr/bin/env python3

import unittest

from src.integers_in_brackets import integers_in_brackets


class TestIntegersInBrackets(unittest.TestCase):

    def test_first(self):
        s="  afd [asd] [12 ] [a34]  [\t -43 ]tt [+12]xxx"
        result = integers_in_brackets(s)
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [12, -43, 12], msg="Incorrect result for string %s!" % s)

    def test_second(self):
        s="  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"
        result = integers_in_brackets(s)
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [47, 12], msg="Incorrect result for string %s!" % s)

    def test_empty(self):
        result = integers_in_brackets("")
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [],
                         msg="Incorrect result for an empty string!")

    def test_no_brackets_gives_an_empty_list(self):
        result = integers_in_brackets("no brackets here at all")
        self.assertIsInstance(result, list, f"Integers_in_brackets should return a list. Got {type(result)}.")
        self.assertEqual(result, [],
                         msg="A string with no bracketed content should return [].")

if __name__ == '__main__':
    unittest.main()
