import unittest
from Temperature import Temperature

class testCases(unittest.TestCase):

    def test_Addition1(self):
        temp1 = Temperature(23,Temperature.Celcius)
        temp2 = Temperature(20,Temperature.Celcius)
        self.assertEqual(temp1.Addition(temp2).TempToString(), "43 C")    
    def test_Addition2(self):
        temp1 = Temperature(230,Temperature.Kelvin)
        temp2 = Temperature(300,Temperature.Kelvin)
        self.assertEqual(temp1.Addition(temp2).TempToString(), "530 K")    
    def test_Addition3(self):
        temp1 = Temperature(65,Temperature.Fahrenheit)
        temp2 = Temperature(50,Temperature.Fahrenheit)
        self.assertEqual(temp1.Addition(temp2).TempToString(), "115 F")   
    def test_Addition4(self):
        temp1 = Temperature(23,Temperature.Celcius)
        temp2 = Temperature(200,Temperature.Kelvin)
        self.assertEqual(temp1.Addition(temp2), Temperature.errstring)         
    def test_Addition5(self):
        temp1 = Temperature(23,Temperature.Celcius)
        temp2 = Temperature(200,Temperature.Kelvin)
        with self.assertRaises(AttributeError):
            temp1.Addition(temp2).TempToString()
    

