from __future__ import annotations
from pyexpat import ErrorString


class Scale: 
    Kelvin = "K"
    Fahrenheit = "F"
    Celcius = "C"

class Temperature(Scale): 
    errstring = "Not the same scale"
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
    def TempToString(self):
        return f"{self.value} {self.scale}"
    def Addition(self, temp2: Temperature):
        if(self.scale == temp2.scale): 
            add = self.value + temp2.value
            resultTemp = Temperature(add, self.scale)
            return resultTemp
        else:
            return Temperature.errstring

    def Substract(self, temp2: Temperature):
        diff = self.value - temp2.value
        if(diff == 0):
            return "Result must not be 0"
        if(self.scale == temp2.scale):
            resultTemp = Temperature(diff, self.scale)
            return resultTemp
        else:
            return Temperature.errstring
    
    def Multiply(self, temp2: Temperature):
        if(self.scale == temp2.scale):
            tempResult = Temperature((self.value * temp2.value),self.scale)
            return tempResult
        else:
            return Temperature.errstring

    
        