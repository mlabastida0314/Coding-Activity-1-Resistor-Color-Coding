# Calculator for resistor's nominal resistance and tolerance.
#This Python code defines a class called NominalResistorCalculator that calculates the nominal resistance and tolerance value of a resistor based on its color bands.
#The resistor color codes and related information are imported from the module Resistor_Color_Codes, which is assumed to be defined elsewhere.
#This .pyfile provides a simple calculator class for determining the nominal resistance and get the tolerance of a resistor based on its color bands.
#The exception handling ensures that the program doesn't crash if an invalid color is entered.

from Resistor_Color_Codes import color_codes, multipliers, tolerances
#This line imports three dictionaries (color_codes, multipliers, and tolerances) from the .py file Resistor_Color_Codes.
#These dictionaries likely contain information about the color codes for resistor bands, multiplier values, and tolerance values.

class NominalResistorCalculator:
#This line defines a class called NominalResistorCalculator to encapsulate the functionality related to calculating the nominal resistance and getting the tolerance of a resistor.
    def __init__(self, color_band1, color_band2, multiplier_band3, tolerance_band4):
#This method is the class constructor, which initializes the instance variables color_band1, color_band2, multiplier_band3, and tolerance_band4 with the values passed as arguments.
        self.color_band1 = color_band1
        self.color_band2 = color_band2
        self.multiplier_band3 = multiplier_band3
        self.tolerance_band4 = tolerance_band4

    def calculate_nominal_resistance(self):
#This method calculates the nominal resistance and get the tolerance of the resistor based on the color bands provided during the instantiation of the object.
#It retrieves the numeric values corresponding to the color bands, multipliers and tolerances from the dictionaries.
#It then uses these values to calculate the nominal resistance using the formula: (code1 * 10 + code2) * multiplier.
#The calculated values are returned.
        try:
            code1 = color_codes[self.color_band1]
            code2 = color_codes[self.color_band2]
            multiplier = multipliers[self.multiplier_band3]
            tolerance_value = tolerances[self.tolerance_band4]

            nominal_resistance = (code1 * 10 + code2) * multiplier
            return nominal_resistance, tolerance_value

        except KeyError as e: #keyerror kasi kapag ang dictionary key is not found in the set of existing keys.
#The code inside the try block attempts to access values from the dictionaries using the color bands.
#If a KeyError occurs (meaning an invalid color band is entered), it catches the exception and prints an error message indicating the invalid color.
            print(f"Error: Invalid color entered - {e}") #e is short for keyerror










