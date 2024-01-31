# Nominal_Resistance_Calculator.py
# Calculator for resistor's nominal resistance and tolerance.
#This Python code defines a class called NominalResistorCalculator that calculates the nominal resistance and tolerance value of a resistor based on its color bands.
#The resistor color codes and related information are imported from the module Resistor_Color_Codes, which is assumed to be defined elsewhere.
#This .pyfile provides a simple calculator class for determining the nominal resistance and get the tolerance of a resistor based on its color bands.
#The exception handling ensures that the program doesn't crash if an invalid color is entered.

import resistor_color
from resistor_color import color_code
#This line imports three dictionaries (color_codes, multipliers, and tolerances) from the .py file Resistor_Color_Codes.
#These dictionaries likely contain information about the color codes for resistor bands, multiplier values, and tolerance values.

class NominalResistorCalculator:
    # This line defines a class called NominalResistorCalculator to encapsulate the functionality related to calculating the nominal resistance and getting the tolerance of a resistor.
    def __init__(self, c1, c2, c3, c4, c5=None):
        # This method is the class constructor, which initializes the instance variables color_band1, color_band2, multiplier_band3, and tolerance_band4 with the values passed as arguments.
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5

    def calculate_nominal_resistance(self):
        # This method calculates the nominal resistance and get the tolerance of the resistor based on the color bands provided during the instantiation of the object.
        # It retrieves the numeric values corresponding to the color bands, multipliers and tolerances from the dictionaries.
        # It then uses these values to calculate the nominal resistance using the formula: (code1 * 10 + code2) * multiplier.
        # The calculated values are returned.
        try:
            color_codes = resistor_color.color_code
            code1 = color_codes[self.c1]
            code2 = color_codes[self.c2]
            code3 = color_codes[self.c3]
            code4 = color_codes[self.c4]
            #  If stmt again to ensure that 5 resistor bands and 4 resistor bands can be calculated correctly
            if self.c5 is not None:   # if merong c5 (means it is a 5 band resistor)
                code5 = color_codes[self.c5]  # magiinitalize ng bagong color
                nominal_resistance = (code1 * 100 + code2 * 10 + code3) * 10 ** code4 # then kukunin yung equivalent value ng code sa dictionary
                tolerance_value = code5
            else: # if 4 resistor band naman ang instance,
                nominal_resistance = (code1 * 10 + code2) * 10 ** code3
                tolerance_value = code4

            return nominal_resistance, tolerance_value  # shows the result ng calculations
        # keyerror kasi kapag ang dictionary key is not found in the set of existing keys.
        # The code inside the try block attempts to access values from the dictionaries using the color bands.
        # If a KeyError occurs (meaning an invalid color band is entered), it catches the exception and prints an error message indicating the invalid color.
        except KeyError as e:
            print(f"Error: Invalid color entered - {e}") # e is short for keyerror