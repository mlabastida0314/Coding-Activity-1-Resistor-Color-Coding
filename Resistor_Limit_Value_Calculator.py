# resistor limit.py
from Resistor_Nominal_Resistance_Calculator import ResistorNominalResistanceCalculator


class ResistorLimitValueCalculator:
    def __init__(self):
        pass

    def calculate_limits(self, color_band1, color_band2, color_band3, color_band4, color_band5=None):
        calculator_instance = ResistorNominalResistanceCalculator(color_band1, color_band2, color_band3, color_band4, color_band5)

        result = calculator_instance.calculate_nominal_resistance()
        if result is not None:
            nominal_resistance, tolerance_value = result
            min_limit_value = nominal_resistance - (nominal_resistance * float(tolerance_value) / 100)
            max_limit_value = nominal_resistance + (nominal_resistance * float(tolerance_value) / 100)

            return min_limit_value, max_limit_value
        else:
            print("Error in limit.py")
            return None


