# main.py
#This Python code is a script that utilizes the NominalResistorCalculator class from the Nominal_Resistance_Calculator module.
#The script allows the user to input the color bands of a resistor and then calculates and prints the corresponding nominal resistance and tolerance.

from Nominal_Resistance_Calculator import NominalResistorCalculator
#This line imports the NominalResistorCalculator class from the Nominal_Resistance_Calculator .py file.
#The assumption here is that the calculator class is defined in a .py file named Nominal_Resistance_Calculator

def main(): #This function serves as the main entry point for the code.
    print("Nominal Resistance Color Coding Calculator")

    color_band1 = input("Enter the first color: ").lower()
    color_band2 = input("Enter the second color: ").lower()
    #The script prompts the user to enter the colors of the resistor bands.
    # The .lower() method is used to convert the input to lowercase, ensuring case-insensitivity.
    multiplier_band3 = input("Enter the multiplier color: ").lower()
    tolerance_band4 = input("Enter the tolerance color: ").lower()

    calculator = NominalResistorCalculator(color_band1, color_band2, multiplier_band3, tolerance_band4)
    #An instance of the NominalResistorCalculator class is created with the provided color band inputs.
    nominal_resistance, tolerance_value = calculator.calculate_nominal_resistance()
    #The calculate_nominal_resistance() method is called on the calculator object, and the resulting nominal resistance and tolerance values are assigned to variables.

    print("Nominal Resistance and Tolerance: {} Ω ± {}%".format(nominal_resistance, tolerance_value))
    #The script then prints the calculated nominal resistance and tolerance values in a formatted string.

if __name__ == "__main__":
    main()
    #The script checks if it is being run directly (not imported as a .py file).
    #If so, it calls the main() function, initiating the execution of the script.
