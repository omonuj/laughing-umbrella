import unittest

from python.airconditioner import AirConditioner


class TestAirConditioner(unittest.TestCase):

    def test_turn_on_and_its_on(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.is_on(), "AC should be on after turning on") # add assertion here


if __name__ == '__main__':
    unittest.main()
