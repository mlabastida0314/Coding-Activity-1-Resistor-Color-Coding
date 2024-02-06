# Resistor Nominal Resistance Calculator

from Resistor_Color_Codes import color_codes, multipliers, tolerances

class ResistorNominalResistanceCalculator:
    def __init__(self, color_band1, color_band2, color_band3, color_band4, color_band5=None):
        self.color_band1 = color_band1
        self.color_band2 = color_band2
        self.color_band3 = color_band3
        self.color_band4 = color_band4
        self.color_band5 = color_band5

    def calculate_nominal_resistance(self):
        try:
            code1 = color_codes[self.color_band1]
            code2 = color_codes[self.color_band2]
            code3 = color_codes[self.color_band3]
            tolerance = tolerances[self.color_band4]

            if self.color_band5 is not None:
                code5 = color_codes[self.color_band5]
                multiplier = multipliers[self.color_band4]
                nominal_resistance = (code1 + code2 + code3) * multiplier
                tolerance_value = code5
            else:
                multiplier = multipliers[self.color_band3]
                nominal_resistance = (code1 + code2) * multiplier
                tolerance_value = tolerance
            return nominal_resistance, tolerance_value

        except KeyError as e:
            print(f"Error: Invalid color entered - {e}")




