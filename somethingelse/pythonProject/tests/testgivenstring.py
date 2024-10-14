import unittest

from classwork.givenstring import get_strings
from classwork.middleinput import middle_input_ce
from classwork.arrangeword import arrange_word
from classwork.occurence import count_char_occurences



class MyTestCase(unittest.TestCase):
    def test_that_given_strings_exists(self):
        get_strings("jonah", "me")

    def test_that_swap_two_strings(self):
        str_first = "hello"
        str_last = "world"
        expected_output = "wollo herld"
        self.assertEqual(str_last, str_last)

    def test_swap_first_two_chars_strings(self):
        str_first = "hil"
        str_last  = "hello"
        expected_output = "hillo hel"
        self.assertEqual(str_last, str_last)

    def test_that_middle_input_ce_exists(self):
        middle_input_ce("hello")

    def test_middle_input_ce_can_add_ce_inthe_middle(self):
        word = middle_input_ce("helloo")
        expected_output = "helceloo"
        self.assertEqual(expected_output ,word)

    def test_that_middle_input_ce_can_add_at_the_end(self):
        actual = middle_input_ce("hello")
        expected_output = "helloce"
        self.assertEqual(expected_output, actual)

    def test_that_middle_input_ce_can_add_to_empty_string(self):
        actual = middle_input_ce("")
        expected_output = "ce"
        self.assertEqual(expected_output, actual)

    def test_that_middle_input_ce_add_to_hi(self):
        actual = middle_input_ce("hi")
        expected_output = "hcei"
        self.assertEqual(expected_output, actual)

    def test_that_middle_input_ce_can_add_to_h(self):
        actual = middle_input_ce("h")
        expected_output = "hce"
        self.assertEqual(expected_output, actual)

    def test_that_middle_input_ce_can_add_to_e(self):
        actual = middle_input_ce("e")
        expected_output = "ece"
        self.assertEqual(expected_output, actual)

    def test_that_arrange_word_exists(self):
        arrange_word("word")

    def test_that_arrange_word_even_length(self):
        actual = arrange_word("word")
        expected_output = "WOrd"
        self.assertEqual(expected_output, actual)

    def test_that_arrange_word_odd_length(self):
        actual = arrange_word("words")
        expected_output = "WORds"
        self.assertEqual(expected_output, actual)

    def test_that_arrange_word_short_word(self):
        actual = arrange_word("hi")
        expected_output = "Hi"
        self.assertEqual(expected_output, actual)

    def test_that_arrange_word_long_word(self):
        actual = arrange_word("africancountry")
        expected_output = "AFRICANcountry"
        self.assertEqual(expected_output, actual)

    def test_that_arrange_word_h(self):
        actual = arrange_word("h")
        expected_output = "H"
        self.assertEqual(expected_output, actual)

    def test_that_arrange_word_long(self):
        actual = arrange_word("HELLOWORLD")
        expected_output = "HELLOworld"
        self.assertEqual(expected_output, actual)

    def test_that_occurences_exists(self):
        count_char_occurences("jonah", "odoh")

    def test_that_occurences_semicolon_has_2_o(self):
        actual = count_char_occurences("semicolon", "o")
        expected_output = ("o", 2)
        self.assertEqual(expected_output, actual)

    def test_that_occurences_hellooo_has_3_o(self):
        actual = count_char_occurences("hellooo", "o")
        expected_output = ("o", 3)
        self.assertEqual(expected_output, actual)

    def test_that_occurences_has_zero_x_in_hello(self):
        actual = count_char_occurences("hello", "x")
        expected_output = ("x", 0)
        self.assertEqual(expected_output, actual)

    def test_that_occurences_has_zero_o_in_empty_string(self):
        actual = count_char_occurences("", "o")
        expected_output = ("o", 0)
        self.assertEqual(expected_output, actual)


if __name__ == '__main__':
    unittest.main()
