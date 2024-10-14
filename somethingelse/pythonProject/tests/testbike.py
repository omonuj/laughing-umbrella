import unittest

from pythonProject.classwork.bike import Bike


class MyTestCase(unittest.TestCase):



    def test_that_bike_is_on(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.toggle_power()
        self.assertEqual(False, self.bike.get_state())

    def test_that_bike_is_off(self):
        self.bike = Bike()
        self.assertEqual(False, self.bike.get_state())


    def test_that_bike_is_on_gear_1_and_accelerate_in_the_increment_of_1(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(1)
        self.bike.accelerate()
        self.assertEqual(16, self.bike.get_speed())

    def test_that_bike_is_on_gear_2_and_accelerate_in_the_increment_of_2(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(2)
        self.bike.set_speed(21)
        self.bike.accelerate()
        self.assertEqual(23, self.bike.get_speed())

    def test_that_bike_is_on_gear_3_and_accelerate_in_the_increment_of_3(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(3)
        self.bike.set_speed(33)
        self.bike.accelerate()
        self.assertEqual(36, self.bike.get_speed())

    def test_that_bike_is_on_gear_4_and_accelerate_in_the_increment_of_4(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(4)
        self.bike.set_speed(42)
        self.bike.accelerate()
        self.assertEqual(46, self.bike.get_speed())

    def test_that_bike_is_on_gear_1_and_can_decelerate_in_the_decrement_of_1(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(1)
        self.bike.set_speed(17)
        self.bike.decelerate()
        self.assertEqual(16, self.bike.get_speed())

    def test_that_bike_is_on_gear_2_and_can_decelerate_in_the_decrement_of_2(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(2)
        self.bike.set_speed(28)
        self.bike.decelerate()
        self.assertEqual(26, self.bike.get_speed())

    def test_that_bike_is_on_gear_3_and_can_decelerate_in_the_decrement_of_3(self):
        self.bike = Bike()
        self.bike.toggle_power()
        self.assertEqual(True, self.bike.get_state())
        self.bike.set_gear(3)
        self.bike.set_speed(38)
        self.bike.decelerate()
        self.assertEqual(35, self.bike.get_speed())

if __name__ == '__main__':
    unittest.main()
