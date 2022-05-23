
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
            return f"{self.value} {self.scale}"
        else: 
            return "Not the same scale"

    
        

