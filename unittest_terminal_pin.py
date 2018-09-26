import unittest

import terminal
from terminal import Atm

"TEST PIN TRUE AND FALSE"
class TestAtm(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_pin1(self):
        pin = self.atm.enter_pin(777)
        self.assertEqual(pin, True)

    def test_pin2(self):
        pin = self.atm.enter_pin(7777)
        self.assertEqual(pin, True)

    def test_pin3(self):
        pin = self.atm.enter_pin(seven)
        self.assertEqual(pin, True)

    def test_pin4(self):
        pin = self.atm.enter_pin(000)
        self.assertEqual(pin, True)

    def test_pin5(self):
        pin = self.atm.enter_pin(-1)
        self.assertEqual(pin, True)

    def test_pin6(self):
        pin = self.atm.enter_pin(0)
        self.assertEqual(pin, True)

    def test_pin7(self):
        pin = self.atm.enter_pin(777)
        self.assertTrue(777)


if __name__ == '__main__':
    unittest.main()