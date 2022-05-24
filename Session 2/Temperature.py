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

    
        