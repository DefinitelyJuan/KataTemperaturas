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
    def test_Addition6(self):
        temp1 = Temperature(320, Temperature.Kelvin)
        temp2 = Temperature(200.40, Temperature.Kelvin)
        self.assertEqual(temp1.Add(temp2).TempToString(),"520.4 K")


    def test_Substraction1(self):
        temp1 = Temperature(12, Temperature.Celcius)
        temp2 = Temperature(13, Temperature.Celcius)
        self.assertEqual(temp1.Substract(temp2).TempToString(),"-1 C")
    def test_Substraction2(self):
        temp1 = Temperature(70, Temperature.Fahrenheit)
        temp2 = Temperature(50, Temperature.Fahrenheit)
        self.assertEqual(temp1.Substract(temp2).TempToString(),"20 F")
    def test_Substraction3(self):
        temp1 = Temperature(320, Temperature.Kelvin)
        temp2 = Temperature(280, Temperature.Kelvin)
        self.assertEqual(temp1.Substract(temp2).TempToString(),"40 K")
    def test_Substraction4(self):
        temp1 = Temperature(546, Temperature.Kelvin)
        temp2 = Temperature(52, Temperature.Fahrenheit)
        self.assertEqual(temp1.Substract(temp2).TempToString(),Temperature.errString)
    def test_Substraction5(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(32, Temperature.Celcius)
        self.assertEqual(temp1.Substract(temp2).TempToString(),"Result cannot be 0")
    def test_Substraction6(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(-32, Temperature.Celcius)
        self.assertEqual(temp1.Substract(temp2).TempToString(),"64 C")
    def test_Substraction7(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(4.80, Temperature.Celcius)
        self.assertEqual(temp1.Substract(temp2).TempToString(),"27.2 C")

    def test_Multiplication1(self):
        temp1 = Temperature(12, Temperature.Celcius)
        temp2 = Temperature(2, Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),"24 C")
    def test_Multiplication2(self):
        temp1 = Temperature(65, Temperature.Fahrenheit)
        temp2 = Temperature(10, Temperature.Fahrenheit)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),"650 F")
    def test_Multiplication3(self):
        temp1 = Temperature(222, Temperature.Kelvin)
        temp2 = Temperature(340, Temperature.Kelvin)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),"75480 K")
    def test_Multiplication4(self):
        temp1 = Temperature(300, Temperature.Kelvin)
        temp2 = Temperature(15, Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),Temperature.errString)
    def test_Multiplication5(self):
        temp1 = Temperature(18, Temperature.Celcius)
        temp2 = Temperature(0, Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),"Result cannot be 0")
    def test_Multiplication6(self):
        temp1 = Temperature(32, Temperature.Celcius)
        temp2 = Temperature(1.5, Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),"48.0 C")
    def test_Multiplication7(self):
        temp1 = Temperature(22.2, Temperature.Celcius)
        temp2 = Temperature(12.8, Temperature.Celcius)
        self.assertEqual(temp1.Multiply(temp2).TempToString(),"284.16 C")

    def test_Division1(self):
        temp1 = Temperature(30, Temperature.Celcius)
        temp2 = Temperature(3, Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"10.0 C")
    def test_Division2(self):
        temp1 = Temperature(65, Temperature.Fahrenheit)
        temp2 = Temperature(10, Temperature.Fahrenheit)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"6.5 F")
    def test_Division3(self):
        temp1 = Temperature(423, Temperature.Kelvin)
        temp2 = Temperature(325, Temperature.Kelvin)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"1.3 K")
    def test_Division4(self):
        temp1 = Temperature(67, Temperature.Fahrenheit)
        temp2 = Temperature(15, Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2).TempToString(),Temperature.errString)
    def test_Division5(self):
        temp1 = Temperature(18, Temperature.Celcius)
        temp2 = Temperature(0, Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"Cannot divide by 0")
    def test_Division6(self):
        temp1 = Temperature(0, Temperature.Celcius)
        temp2 = Temperature(18, Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"Result cannot be 0")   
    def test_Division7(self):
        temp1 = Temperature(70, Temperature.Fahrenheit)
        temp2 = Temperature(65.5, Temperature.Fahrenheit)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"1.07 F")
    def test_Division8(self):
        temp1 = Temperature(22.2, Temperature.Celcius)
        temp2 = Temperature(12.8, Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2).TempToString(),"1.73 C")
