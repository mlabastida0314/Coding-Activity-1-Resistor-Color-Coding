# main.py
from Resistor_Color_Codes import color_codes, multipliers, tolerances
from Resistor_Nominal_Resistance_Calculator import ResistorNominalResistanceCalculator
from Resistor_Limit_Value_Calculator import ResistorLimitValueCalculator

while True:
    try:
        print("Nominal Resistance Color Coding Calculator")
        bands_input = (input("How many bands does the resistor have? (4 or 5 bands): "))
        band = int(bands_input)

        if band == 4:
            print('4 Band Resistor')
            color_band1 = input("Enter the first color band: ").lower()
            color_band2 = input("Enter the second color band: ").lower()
            color_band3 = input("Enter the multiplier color band: ").lower()
            color_band4 = input("Enter the tolerance color band: ").lower()

            if color_band1 not in color_codes or color_band2 not in color_codes or \
                    color_band3 not in multipliers or color_band4 not in tolerances:
                raise KeyError("Invalid color band/s entered.")

            resistor_calculator = ResistorNominalResistanceCalculator(color_band1, color_band2, color_band3, color_band4)
            result = resistor_calculator.calculate_nominal_resistance()
            if result is not None:
                nominal_resistance, tolerance_value = result
                print("Nominal Resistance and Tolerance: {} Ω ± {}%".format(nominal_resistance, tolerance_value))
            else:
                print("Error: In calculating the nominal resistance.")

            limit_value_calculator = ResistorLimitValueCalculator()
            result = limit_value_calculator.calculate_limits(color_band1, color_band2, color_band3, color_band4)
            min_limit_values, max_limit_values = result
            print("Limit Values, Minimum and Maximum: {} Ω - {} Ω".format(min_limit_values, max_limit_values))

        elif band == 5:
            print('5 Band Resistor')
            color_band1 = input("Enter the first color band: ").lower()
            color_band2 = input("Enter the second color band: ").lower()
            color_band3 = input("Enter the third color band: ").lower()
            color_band4 = input("Enter the multiplier color band: ").lower()
            color_band5 = input("Enter the tolerance color band: ").lower()

            if color_band1 not in color_codes or color_band2 not in color_codes or color_band3 not in color_codes or \
                    color_band4 not in multipliers or color_band5 not in tolerances:
                raise KeyError("Invalid color band/s entered.")

            resistor_calculator = ResistorNominalResistanceCalculator(color_band1, color_band2, color_band3, color_band4, color_band5)
            result = resistor_calculator.calculate_nominal_resistance()
            if result is not None:
                nominal_resistance, tolerance_value = result
                print("Nominal Resistance and Tolerance: {} Ω ± {}%".format(nominal_resistance, tolerance_value))
            else:
                print("Error: In calculating the nominal resistance.")

            limit_value_calculator = ResistorLimitValueCalculator()
            result = limit_value_calculator.calculate_limits(color_band1, color_band2, color_band3, color_band4, color_band5)
            min_limit_values, max_limit_values = result
            print("Limit Values, Minimum and Maximum: {} Ω - {} Ω".format(min_limit_values, max_limit_values))

        else:
            print("Error: Invalid number of bands.")

    except ValueError:
        print("Error: Please enter a valid integer (4 or 5) for the number of bands.")

    except KeyError as e:
        print(f"Error: {e}. Please enter valid color bands.")

    end = input("Do you want to continue? (yes or no): ").lower()
    if end != 'yes':
        print("This is the end of the code. Thank you.")
        break
