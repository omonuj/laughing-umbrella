import unittest
from unittest import TestCase
from pythonProject.classwork.tv import Television


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.tv1 = Television()

    def test_that_tv_can_turn_on(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_state())

    def test_that_tv_can_turn_off(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_state())
        self.tv1.turn_off()
        self.assertFalse(self.tv1.get_state())

    def test_that_volume_can_increase(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_state())
        self.tv1.increase_volume()
        self.assertEqual(self.tv1.get_volume(), 8)

    def test_that_volume_can_decrease(self):
        self.tv1.turn_on()
        self.tv1.decrease_volume()
        self.assertEqual(self.tv1.get_volume(), 6)

    def test_that_volume_cannot_increase_beyond10(self):
        self.tv1.turn_on()
        self.tv1.set_volume(10)
        with self.assertRaises(ValueError):
            self.tv1.increase_volume()

    def test_that_volume_cannot_decrease_bellow1(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_state())
        self.tv1.set_volume(1)
        with self.assertRaises(ValueError):
            self.tv1.decrease_volume()

    def test_that_can_get_volume(self):
        self.tv1.turn_on()
        self.tv1.get_volume()
        self.assertEqual(self.tv1.get_volume(), 7)


    def test_that_tv_can_increase_channel(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.is_on)
        self.tv1.increase_channel()
        self.assertEqual(self.tv1.get_channel(), 5)

    def test_that_tv_can_decrease_channel(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.is_on)
        self.tv1.decrease_channel()
        self.assertEqual(self.tv1.get_channel(), 3)

    def test_that_tv_can_channel_cannot_go_below1(self):
        self.tv1.turn_on()
        self.tv1.set_channel(1)
        with self.assertRaises(ValueError):
            self.tv1.decrease_channel()

    def test_that_tv_cannot_increase_channel_above_100(self):
        self.tv1.turn_on()
        self.tv1.set_channel(100)
        with self.assertRaises(ValueError):
            self.tv1.increase_channel()

    def test_that_tv_can_get_channel(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_channel())
        self.tv1.get_channel()
        self.assertEqual(self.tv1.get_channel(), 4)

    def test_that_tv_can_reset_channel(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_channel())
        self.tv1.set_channel(50)
        self.tv1.reset_channel()
        self.assertEqual(self.tv1.get_channel(), 1)

    def test_that_tv_can_reset_volum(self):
        self.tv1.turn_on()
        self.assertTrue(self.tv1.get_state())
        self.tv1.reset_volume()
        self.assertEqual(self.tv1.get_volume(), 1)



if __name__ == '__main__':
    unittest.main()
