import unittest

from pythonProject.classwork.airconditioner import AirConditioner


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ac = AirConditioner()

    def test_that_ac_was_off_and_can_turn_on(self):
        assert self.ac.get_status() == "OFF"
        self.ac.toggle_power()
        assert self.ac.get_status() == "ON"


    def test_that_ac_was_off_can_turn_on_and_off(self):
        assert self.ac.get_status() == "OFF"
        self.ac.toggle_power()
        assert self.ac.get_status() == "ON"
        self.ac.toggle_power()
        assert self.ac.get_status() == "OFF"

    def test_that_can_turn_on_and_increase_temperature_and_cooling_level_reduce(self):
        assert self.ac.get_status() == "OFF"
        self.ac.toggle_power()
        assert self.ac.get_status() == "ON"
        self.assertEqual(24, self.ac.get_temperature())
        self.assertEqual(10, self.ac.get_cooling_level())
        self.ac.increase_temperature()
        self.assertEqual(25, self.ac.get_temperature())
        self.assertEqual(9, self.ac.get_cooling_level())

    def test_that_ac_can_turn_on_decrease_temperature_and_cooling_will_reduce(self):
        assert self.ac.get_status() == "OFF"
        self.ac.toggle_power()
        assert self.ac.get_status() == "ON"
        self.assertEqual(24, self.ac.get_temperature())
        self.assertEqual(10, self.ac.get_cooling_level())
        self.ac.decrease_temperature()
        self.assertEqual(23, self.ac.get_temperature())
        self.assertEqual(11, self.ac.get_cooling_level())

    def test_ac_boundaries_high(self):
        assert self.ac.get_status() == "OFF"
        self.ac.toggle_power()
        assert self.ac.get_status() == "ON"
        self.assertEqual(24, self.ac.get_temperature())
        self.assertEqual(10, self.ac.get_cooling_level())
        for _ in range(6):
            self.ac.increase_temperature()
        self.assertEqual(30, self.ac.get_temperature())
        self.assertEqual(4, self.ac.get_cooling_level())
        self.ac.increase_temperature()
        self.assertEqual(30, self.ac.get_temperature())


    def test_ac_boundaries_low(self):
        assert self.ac.get_status() == "OFF"
        self.ac.toggle_power()
        assert self.ac.get_status() == "ON"
        self.assertEqual(24, self.ac.get_temperature())
        self.assertEqual(10, self.ac.get_cooling_level())
        for _ in range(10):
            self.ac.decrease_temperature()
        self.assertEqual(16, self.ac.get_temperature())
        self.assertEqual(18, self.ac.get_cooling_level())
        self.ac.decrease_temperature()

if __name__ == '__main__':
    unittest.main()
