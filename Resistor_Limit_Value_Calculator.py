#Resistor Limit Value Calculator

from Resistor_Nominal_Resistance_Calculator import ResistorNominalResistanceCalculator

class ResistorLimitValueCalculator:
    def __init__(self):
        pass

    def calculate_limits(self, color_band1, color_band2, color_band3, color_band4, color_band5=None):
        calculator_instance = ResistorNominalResistanceCalculator(color_band1, color_band2, color_band3, color_band4, color_band5=None)

        nominal_resistance, tolerance_value = calculator_instance.calculate_nominal_resistance()

        min_limit_value = nominal_resistance - (nominal_resistance * float(tolerance_value))
        max_limit_value = nominal_resistance + (nominal_resistance * float(tolerance_value))

        return min_limit_value, max_limit_value

