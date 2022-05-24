from __future__ import annotations



class Scale: 
    Kelvin = "K"
    Fahrenheit = "F"
    Celcius = "C"
    def __init__(self, scale):
        self.scale = scale


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

    def Divide(self, temp2: Temperature):
        if(temp2.value == 0):
            return "Temp2 value cannot be 0"
        if(self.scale == temp2.scale):
            tempResult = Temperature(round((self.value/temp2.value),2), self.scale)
            return tempResult
        else:
            return Temperature.errstring

    def getScale(self):
        objScale = Scale(self.scale)
        return objScale

    def ToFahrenheit(self):
        match self.scale:
            case "F":
                resTemp = Temperature(self.value, self.scale)
            case "C":
                resTemp = Temperature(round(((self.value * 9/5) + 32), 2), "F")
            case "K":
                resTemp = Temperature(round((((self.value - 273.15) * 9/5)+32), 2),"F")
            case _:
                resTemp = "Scale not valid"
            
        return resTemp

    def ToCelcius(self):
        match self.scale:
            case "F":
                resTemp = Temperature(round(((self.value -32) * 5/9), 2),"C")
            case "C":
                resTemp = Temperature(self.value, self.scale)
            case "K":
                resTemp = Temperature(round((self.value - 273.15), 2),"C")
            case _:
                resTemp = "Scale not valid"
            
        return resTemp

    def ToKelvin(self):
        match self.scale:
            case "F":
                resTemp = Temperature(round((((self.value -32) * 5/9) + 273.15), 2),"K")
            case "C":
                resTemp = Temperature(round((self.value + 273.15), 2),"K")
            case "K":
                resTemp = Temperature(self.value, self.scale)
            case _:
                resTemp = "Scale not valid"
            
        return resTemp

        