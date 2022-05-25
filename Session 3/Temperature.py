from __future__ import annotations

class Scale:
    def __init__(self, scale):
        self.scale = scale

    Kelvin = "K"
    Fahrenheit = "F"
    Celcius = "C"

class Temperature(Scale):
    errString = "Temperatures are not in the same scale"

    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def Add(self, temp2: Temperature):
        sum = round((self.value + temp2.value),2)
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
        diff = round((self.value - temp2.value),2)
        if(diff == 0):
            resTemp = Temperature("Result cannot be 0", "E")
            return resTemp
        elif(self.scale == temp2.scale):
            resTemp = Temperature(diff, self.scale)
            return resTemp
        else: 
            resTemp = Temperature(Temperature.errString, "E")
            return resTemp

    def Multiply(self, temp2: Temperature):
        mult = round((self.value * temp2.value),2)
        if(mult == 0):
            resTemp = Temperature("Result cannot be 0", "E")
            return resTemp
        elif(self.scale == temp2.scale):
            resTemp = Temperature(mult, self.scale)
            return resTemp
        else: 
            resTemp = Temperature(Temperature.errString, "E")
            return resTemp

    def Divide(self, temp2: Temperature):
        if(temp2.value == 0):
            resTemp = Temperature("Cannot divide by 0", "E")
            return resTemp
        div = round((self.value / temp2.value),2)
        if(div == 0):
            resTemp = Temperature("Result cannot be 0", "E")
            return resTemp
        elif(self.scale == temp2.scale):
            resTemp = Temperature(div, self.scale)
            return resTemp
        else: 
            resTemp = Temperature(Temperature.errString, "E")
            return resTemp

    def GetScale(self):
        scaleobj = Scale(self.scale)
        return scaleobj

    def ToFahrenheit(self):
        match (self.scale):
            case "F":
                resTemp = Temperature(self.value, self.scale)
                return resTemp
            case "C":
                resTemp = Temperature(round(((self.value *9/5)+ 32),2), Temperature.Fahrenheit)
                return resTemp
            case "K":
                resTemp = Temperature(round((((self.value -273.15)*9/5) + 32),2), Temperature.Fahrenheit)
                return resTemp
            case _:
                resTemp = Temperature("Scale not valid", "E")
            
        return resTemp