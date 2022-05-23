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
        
    def test_substraction5(self):
        temp1 = Temperature(40,Temperature.Celcius)
        temp2 = Temperature(-10,Temperature.Celcius)
        self.assertEqual(temp1.Substraction(temp2), "50 C")  

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
    
    def test_divition1(self):
        temp1 = Temperature(15,Temperature.Celcius)
        temp2 = Temperature(5,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2),"3.0 C")
    
    def test_divition2(self):
        temp1 = Temperature(80,Temperature.Fahrenheit)
        temp2 = Temperature(20,Temperature.Fahrenheit)
        self.assertEqual(temp1.Divide(temp2),"4.0 F")
    
    def test_divition3(self):
        temp1 = Temperature(400,Temperature.Fahrenheit)
        temp2 = Temperature(23,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2), Temperature.errString)    

    def test_divition4(self):
        temp1 = Temperature(16,Temperature.Fahrenheit)
        temp2 = Temperature(5,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2), Temperature.errString)

    def test_divition5(self):
        temp1 = Temperature(34,Temperature.Fahrenheit)
        temp2 = Temperature(0,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2), "Can't divide by 0")

    def test_divition6(self):
        temp1 = Temperature(16,Temperature.Celcius)
        temp2 = Temperature(5,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2), "3.2 C")    
        
    def test_divition7(self):
        temp1 = Temperature(16,Temperature.Celcius)
        temp2 = Temperature(-5,Temperature.Celcius)
        self.assertEqual(temp1.Divide(temp2), "-3.2 C")    

    def test_fahrenheitConv1(self):
        temp1 = Temperature(15,Temperature.Celcius)
        self.assertEqual(temp1.ToFahrenheit(),"59.0 F")
    
    def test_fahrenheitConv2(self):
        temp1 = Temperature(80,Temperature.Fahrenheit)
        self.assertEqual(temp1.ToFahrenheit(),"80 F")
    
    def test_fahrenheitConv3(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        self.assertEqual(temp1.ToFahrenheit(), "260.33 F")    
            
    def test_fahrenheitConv4(self):
        temp1 = Temperature(400,"P")
        self.assertEqual(temp1.ToFahrenheit(), "Scale not valid. Should be K/C/F") 

    def test_celciusConv1(self):
        temp1 = Temperature(15,Temperature.Celcius)
        self.assertEqual(temp1.ToCelcius(),"15 C")
    
    def test_celciusConv2(self):
        temp1 = Temperature(80,Temperature.Fahrenheit)
        self.assertEqual(temp1.ToCelcius(),"26.67 C")
    
    def test_celciusConv3(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        self.assertEqual(temp1.ToCelcius(), "126.85 C")    
            
    def test_celciusConv4(self):
        temp1 = Temperature(400,"P")
        self.assertEqual(temp1.ToCelcius(), "Scale not valid. Should be K/C/F")   
        
    def test_kelvinConv1(self):
        temp1 = Temperature(15,Temperature.Celcius)
        self.assertEqual(temp1.ToKelvin(),"288.15 K")
    
    def test_kelvinConv2(self):
        temp1 = Temperature(260.33,Temperature.Fahrenheit)
        self.assertEqual(temp1.ToKelvin(),"400.0 K")
    
    def test_kelvinConv3(self):
        temp1 = Temperature(400,Temperature.Kelvin)
        self.assertEqual(temp1.ToKelvin(), "400 K")    
            
    def test_kelvinConv4(self):
        temp1 = Temperature(400,"P")
        self.assertEqual(temp1.ToKelvin(), "Scale not valid. Should be K/C/F")       

    def test_valueupdate1(self):
        temp1 = Temperature(15,Temperature.Celcius)
        temp2 = Temperature(10,Temperature.Celcius)
        temp1.Add(temp2)
        self.assertEqual(temp1.TempToString(), "25 C")
        temp1.ToFahrenheit()
        self.assertEqual(temp1.TempToString(), "77.0 F")
        temp1.ToKelvin()
        self.assertEqual(temp1.TempToString(), "298.15 K")
