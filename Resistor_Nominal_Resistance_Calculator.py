# nominal .py
from Resistor_Color_Codes import color_codes, multipliers, tolerances


class ResistorNominalResistanceCalculator:
    def __init__(self, color_band1, color_band2, color_band3, color_band4, color_band5=None):
        self.color_band1 = color_band1
        self.color_band2 = color_band2
        self.color_band3 = color_band3
        self.color_band4 = color_band4
        self.color_band5 = color_band5 if color_band5 else None

    def calculate_nominal_resistance(self):
        code1 = color_codes[self.color_band1]
        code2 = color_codes[self.color_band2]
        code3 = color_codes[self.color_band3]

        if self.color_band5 is not None:
            code5 = tolerances[self.color_band5]
            multiplier = multipliers[self.color_band4]
            nominal_resistance = int(f"{code1}{code2}{code3}") * multiplier
            tolerance_value = float(code5) / 100
        else:
            multiplier = multipliers[self.color_band3]
            nominal_resistance = int(f"{code1}{code2}") * multiplier
            tolerance = tolerances[self.color_band4]
            tolerance_value = float(tolerance) / 100

        return nominal_resistance, tolerance_value

'''
        if self.color_band4 in tolerances:
            tolerance = tolerances[self.color_band4]
        else:
            print(f'Invalid tolerance color band: {self.color_band4}')
            return None
'''
