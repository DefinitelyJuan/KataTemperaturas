import unittest
from Temperature import Temperature

class TestCases(unittest.TestCase):
    def test_Addition1(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(10, Temperature.Celcius)
        self.assertEqual(temp1.Add(temp2).TempToString(),"42 C")
    def test_Addition2(self):
        temp1 = Temperature(80, Temperature.Fahrenheit)
        temp2 = Temperature(40, Temperature.Fahrenheit)
        self.assertEqual(temp1.Add(temp2).TempToString(),"120 F")
    def test_Addition3(self):
        temp1 = Temperature(320, Temperature.Kelvin)
        temp2 = Temperature(200, Temperature.Kelvin)
        self.assertEqual(temp1.Add(temp2).TempToString(),"520 K")
    def test_Addition4(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(80, Temperature.Fahrenheit)
        self.assertEqual(temp1.Add(temp2).TempToString(),Temperature.errString)
    def test_Addition5(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(-32, Temperature.Celcius)
        self.assertEqual(temp1.Add(temp2).TempToString(),"Result cannot be 0")



