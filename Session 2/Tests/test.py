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
    
    def test_Substraction1(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(20,Temperature.Celcius)
        self.assertEqual(temp1.Substract(temp2).TempToString(), "20 C")    
    def test_Substraction2(self):
        temp1 = Temperature(230,Temperature.Kelvin)
        temp2 = Temperature(300,Temperature.Kelvin)
        self.assertEqual(temp1.Substract(temp2).TempToString(), "-70 K")    
    def test_Substraction3(self):
        temp1 = Temperature(65,Temperature.Fahrenheit)
        temp2 = Temperature(50,Temperature.Fahrenheit)
        self.assertEqual(temp1.Substract(temp2).TempToString(), "15 F")   
    def test_Substraction4(self):
        temp1 = Temperature(23,Temperature.Celcius)
        temp2 = Temperature(200,Temperature.Kelvin)
        self.assertEqual(temp1.Substract(temp2), Temperature.errstring)         
    def test_Substraction5(self):
        temp1 = Temperature(23,Temperature.Celcius)
        temp2 = Temperature(200,Temperature.Kelvin)
        with self.assertRaises(AttributeError):
            temp1.Substract(temp2).TempToString()    

    def test_Multiplication1(self):
        temp1 = Temperature(31,Temperature.Celcius)
        temp2 = Temperature(16,Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2).TempToString(), "496 C")    
    def test_Multiplication2(self):
        temp1 = Temperature(212,Temperature.Kelvin)
        temp2 = Temperature(423,Temperature.Kelvin)
        self.assertEqual(temp1.Multiply(temp2).TempToString(), "89676 K")    
    def test_Multiplication3(self):
        temp1 = Temperature(62,Temperature.Fahrenheit)
        temp2 = Temperature(80,Temperature.Fahrenheit)
        self.assertEqual(temp1.Multiply(temp2).TempToString(), "4960 F")   
    def test_Multiplication4(self):
        temp1 = Temperature(322,Temperature.Kelvin)
        temp2 = Temperature(22,Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2), Temperature.errstring)         
    def test_Multiplication5(self):
        temp1 = Temperature(80,Temperature.Fahrenheit)
        temp2 = Temperature(200,Temperature.Kelvin)
        with self.assertRaises(AttributeError):
            temp1.Multiply(temp2).TempToString()

    def test_Division1(self):
        temp1 = Temperature(31,Temperature.Celcius)
        temp2 = Temperature(10,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2).TempToString(), "3.1 C")    
    def test_Division2(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        temp2 = Temperature(200,Temperature.Kelvin)
        self.assertEqual(temp1.Divide(temp2).TempToString(), "2.0 K")    
    def test_Division3(self):
        temp1 = Temperature(86,Temperature.Fahrenheit)
        temp2 = Temperature(43,Temperature.Fahrenheit)
        self.assertEqual(temp1.Divide(temp2).TempToString(), "2.0 F")   
    def test_Division4(self):
        temp1 = Temperature(322,Temperature.Kelvin)
        temp2 = Temperature(22,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2), Temperature.errstring)         
    def test_Division5(self):
        temp1 = Temperature(80,Temperature.Fahrenheit)
        temp2 = Temperature(200,Temperature.Kelvin)
        with self.assertRaises(AttributeError):
            temp1.Divide(temp2).TempToString()
    def test_Division6(self):
        temp1 = Temperature(62,Temperature.Fahrenheit)
        temp2 = Temperature(0,Temperature.Fahrenheit)
        self.assertEqual(temp1.Divide(temp2), "Temp2 value cannot be 0")  
    def test_Division7(self):
        temp1 = Temperature(62,Temperature.Fahrenheit)
        temp2 = Temperature(0,Temperature.Fahrenheit)
        with self.assertRaises(AttributeError):
            temp1.Divide(temp2).TempToString()

    def test_FahrenheitConv1(self):
        temp1 = Temperature(17, Temperature.Celcius)
        self.assertEqual(temp1.ToFahrenheit().TempToString(), "62.6 F")    
    def test_FahrenheitConv2(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        self.assertEqual(temp1.ToFahrenheit().TempToString(), "260.33 F")    
    def test_FahrenheitConv3(self):
        temp1 = Temperature(86,Temperature.Fahrenheit)
        self.assertEqual(temp1.ToFahrenheit().TempToString(), "86 F")   
    def test_FahrenheitConv4(self):
        temp1 = Temperature(322,"T")
        self.assertEqual(temp1.ToFahrenheit(), "Scale not valid")         
    def test_FahrenheitConv5(self):
        temp1 = Temperature(80,"T")
        with self.assertRaises(AttributeError):
            temp1.ToFahrenheit().TempToString()
