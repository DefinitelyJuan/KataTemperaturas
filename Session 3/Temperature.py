from __future__ import annotations
class Scale:
    Kelvin = "K"
    Fahrenheit = "F"
    Celcius = "C"

class Temperature(Scale):
    errString = "Temperatures are not in the same scale"

    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def Add(self, temp2: Temperature):
        sum = self.value + temp2.value
        if(sum == 0):
            resTemp = Temperature("Result cannot be 0", "E")
            return resTemp
        elif(self.scale == temp2.scale):
            resTemp = Temperature(sum, self.scale)
            return resTemp
        else: 
            resTemp = Temperature(Temperature.errString, "E")
            return resTemp

    def TempToString(self):
        if(self.scale != "E"):
            return f"{self.value} {self.scale}"
        else:
            return self.value

    def Substract(self, temp2: Temperature):
        diff = self.value - temp2.value
        if(diff == 0):
            resTemp = Temperature("Result cannot be 0", "E")
            return resTemp
        elif(self.scale == temp2.scale):
            resTemp = Temperature(diff, self.scale)
            return resTemp
        else: 
            resTemp = Temperature(Temperature.errString, "E")
            return resTemp
