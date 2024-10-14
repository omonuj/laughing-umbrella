from unittest import TestCase

import cornflakesBiggestodd


class TestBiggest_odd(TestCase):
    def test_biggest_function(self):
        self.assertEqual(cornflakesBiggestodd.biggest_odd("234569"), 9)