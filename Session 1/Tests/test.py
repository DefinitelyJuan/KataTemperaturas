import unittest
from temperature import Temperature 
class testcases(unittest.TestCase):
    def test_add1(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        temp2 = Temperature(200,Temperature.Kelvin)
        self.assertEqual(temp1.Add(temp2),"600 K")
    def test_add2(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(-20,Temperature.Celcius)
        self.assertEqual(temp1.Add(temp2),"20 C")
    
    def test_add3(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        temp2 = Temperature(0,Temperature.Celcius)
        self.assertEqual(temp1.Add(temp2), Temperature.errString)
    
    def test_substraction1(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        temp2 = Temperature(400,Temperature.Kelvin)
        self.assertEqual(temp1.Substraction(temp2),"Difference must not be 0")
    
    def test_substraction2(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(20,Temperature.Celcius)
        self.assertEqual(temp1.Substraction(temp2),"20 C")
    
    def test_substraction3(self):
        temp1 = Temperature(400,Temperature.Fahrenheit)
        temp2 = Temperature(0,Temperature.Celcius)
        self.assertEqual(temp1.Substraction(temp2), Temperature.errString)

    def test_substraction4(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(0,Temperature.Celcius)
        self.assertEqual(temp1.Substraction(temp2), "40 C")      

    def test_multiplication1(self):
        temp1 = Temperature(12,Temperature.Celcius)
        temp2 = Temperature(3,Temperature.Celcius)
        self.assertEqual(temp1.Multiplication(temp2),"36 C")
    
    def test_multiplication2(self):
        temp1 = Temperature(60,Temperature.Fahrenheit)
        temp2 = Temperature(10,Temperature.Fahrenheit)
        self.assertEqual(temp1.Multiplication(temp2),"600 F")
    
    def test_multiplication3(self):
        temp1 = Temperature(400,Temperature.Fahrenheit)
        temp2 = Temperature(0,Temperature.Celcius)
        self.assertEqual(temp1.Multiplication(temp2), Temperature.errString)

    def test_multiplication4(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(0,Temperature.Celcius)
        self.assertEqual(temp1.Multiplication(temp2), "0 C")      

    def test_multiplication5(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(-2,Temperature.Celcius)
        self.assertEqual(temp1.Multiplication(temp2), "-80 C")   
    

