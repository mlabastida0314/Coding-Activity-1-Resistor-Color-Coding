# main.py
# This Python code is a script that utilizes the NominalResistorCalculator class from the Nominal_Resistance_Calculator module.
# The script allows the user to input the color bands of a resistor and then calculates and prints the corresponding nominal resistance and tolerance.
import resistor_color
# import for resistor_color.py where the color bands of the resistor is located
from Nominal_Resistance_Calculator import NominalResistorCalculator
# This line imports the NominalResistorCalculator class from the Nominal_Resistance_Calculator .py file.
# The assumption here is that the calculator class is defined in a .py file named Nominal_Resistance_Calculator

# function for user-input where in this way, it asks the user based on the bands they will enter
def get_cband_input(num_colors):                             #  Method cband shortens the collection of data from user
    colors = []                                              # initialize the colors as an empty list which will later be used to store the input
    for i in range(num_colors):                              # for-loop stmt (in input == colors)
        color = input(f"Enter the {i + 1} color: ").lower()  # every input is incremented to assigned name
        # The script prompts the user to enter the colors of the resistor bands.
        # The .lower() method is used to convert the input to lowercase, ensuring case-insensitivity.
        colors.append(color)                                 # this line will add the color (input) to the list(colors): kaya yung empty list kanina, may input na
    return colors


while True:  # I used While loop kasi sanay akong gamitin ito sa java hehe. This is for continuous input taking (magpprompt ng tanong after session)
    try:     # Start of Error Handling - Expected error- maling color, maling spelling, or maling band (not int)
        print("Nominal Resistance Color Coding Calculator")
        band = int(input("How many bands does the resistor have? (4/5): "))  # prompt: user will enter the band (limited to 4 and 5)
        if band == 4:                                                        # if stmt- galing sa user ung value (band)
            print('4 band resistor')                                         # Title
            c1, c2, c3, c4 = get_cband_input(4)  # this is the data gathered from the for-loop(4) (when the color got append to the list)
            # since unnamed sila, dito nilagyan ng variable name =  c1, c2, c3, c4 respectively
            calculator = NominalResistorCalculator(c1, c2, c3, c4)
            # An instance of the NominalResistorCalculator class is created with the provided color band inputs.
            nominal_resistance, tolerance_value = calculator.calculate_nominal_resistance()
            # The calculate_nominal_resistance() method is called on the calculator object, and the resulting nominal resistance and tolerance values are assigned to variables.
            print("Nominal Resistance and Tolerance: {} Ω ± {}%".format(nominal_resistance, tolerance_value))
            # The script then prints the calculated nominal resistance and tolerance values in a formatted string.
            resistor_color.calculate_limits(nominal_resistance, tolerance_value)
            # function call for Calculation of limits from resistor_color.py

        elif band == 5:                             # This line prompts that when the user states that the resistor is 5 bands, the this will run
            print('5 band resistor')                # Title
            c1, c2, c3, c4, c5 = get_cband_input(5) # this is the data gathered from the for-loop(5) (when the color got append to the list)
            calculator = NominalResistorCalculator(c1, c2, c3, c4, c5)
            # An instance of the NominalResistorCalculator class is created with the provided color band inputs.
            nominal_resistance, tolerance_value = calculator.calculate_nominal_resistance()
            # The calculate_nominal_resistance() method is called on the calculator object, and the resulting nominal resistance and tolerance values are assigned to variables.
            print("Nominal Resistance and Tolerance: {} Ω ± {}%".format(nominal_resistance, tolerance_value))
            # The script then prints the calculated nominal resistance and tolerance values in a formatted string.
            resistor_color.calculate_limits(nominal_resistance, tolerance_value)
            # function call for Calculation of limits from resistor_color.py
        else:  # If wala sa nabanggit ang niinput ni user
            print("Invalid number of bands.")
    except ValueError as e:  # Value error means na naglagay ka ng val pero mali (may value - almost the same (spelling) pero mali parin
        print(e)
    # loop to continue or exit|| this is the other half of while loop, if false na ang while loop (input = no) then mageend na and code
    end = input("Do you want to continue? (yes/no): ").lower()
    if end != 'yes':   # if not yes (means no == end)
        print("This is the end of the code. Thank you.")
        break   # formally exit the loop
