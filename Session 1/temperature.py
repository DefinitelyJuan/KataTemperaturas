
from __future__ import annotations
from tkinter.tix import CheckList
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
        return f"{round(self.value,2)} {self.scale}"

    def Multiplication(self,temp2 : Temperature):
        if(self.scale == temp2.scale):
            self.value *= temp2.value
            return Temperature.TempToString(self)
        else: 
            return "Not the same scale"
        
    def Divide(self, temp2 : Temperature):
        if(temp2.value == 0):
            return "Can't divide by 0"

        if(self.scale == temp2.scale):
            self.value /= temp2.value
            return Temperature.TempToString(self)
        else: 
            return "Not the same scale"
    def getScale(self):
        return self.scale

    def ToFahrenheit(self):
        match self.scale:
            case Temperature.Kelvin:
                self.value = ((self.value - 273.15) *9/5) + 32
            case Temperature.Celcius:
                self.value = (self.value *9/5) + 32
            case Temperature.Fahrenheit:
                self.value = self.value
            case _:
                return "Scale not valid. Should be K/C/F"

        self.scale = Temperature.Fahrenheit
        return Temperature.TempToString(self)     

    def ToCelcius(self):
        match self.scale:
            case Temperature.Kelvin:
                self.value = (self.value - 273.15)
            case Temperature.Celcius:
                self.value = self.value
            case Temperature.Fahrenheit:
                self.value = (self.value - 32) *5/9
            case _:
                return "Scale not valid. Should be K/C/F"

        self.scale = Temperature.Celcius
        return Temperature.TempToString(self)
    
        
