# nominal .py
from Resistor_Color_Codes import color_codes, multipliers, tolerances

#class
class ResistorNominalResistanceCalculator:
    def __init__(self, color_band1, color_band2, color_band3, color_band4, color_band5=None): #initialization
        self.color_band1 = color_band1
        self.color_band2 = color_band2
        self.color_band3 = color_band3
        self.color_band4 = color_band4
        self.color_band5 = color_band5 if color_band5 else None

    #method
    def calculate_nominal_resistance(self):
        code1 = color_codes[self.color_band1]
        code2 = color_codes[self.color_band2]
        code3 = color_codes[self.color_band3]

        #conditional statement
        if self.color_band5 is not None: #if resistor has 5 bands
            code5 = tolerances[self.color_band5]
            multiplier = multipliers[self.color_band4]
            nominal_resistance = int(f"({code1}{code2}{code3}") * multiplier
            tolerance_value = float(code5)/100
        else: #otherwise, if resistor has 4 bands
            multiplier = multipliers[self.color_band3]
            nominal_resistance = (code1 + code2) * multiplier
            tolerance = tolerances[self.color_band4]
            tolerance_value = float(tolerance) / 100

        return nominal_resistance, tolerance_value