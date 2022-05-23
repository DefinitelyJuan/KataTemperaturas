
from __future__ import annotations
class Scale: 
    Kelvin = "K"
    Celcius = "C"
    Fahrenheit = "F"

class Temperature(Scale):
    errString = "Not the same scale"

    def __init__(self,value,scale):
        self.value = value
        self.scale = scale
    def Add(self, temp2: Temperature):
        if(self.scale == temp2.scale):
            self.value += temp2.value
            return Temperature.TempToString(self)
        else: 
            return "Not the same scale"
    def Substraction(self, temp2: Temperature):
        diff = self.value - temp2.value
        if(diff == 0):
            return "Difference must not be 0"
        if(self.scale == temp2.scale):
            self.value = diff
            return Temperature.TempToString(self)
        else: 
            return "Not the same scale"
            
    def TempToString(self):
        return f"{self.value} {self.scale}"

    def Multiplication(self,temp2 : Temperature):
        if(self.scale == temp2.scale):
            self.value *= temp2.value
            return Temperature.TempToString(self)
        else: 
            return "Not the same scale"
        

