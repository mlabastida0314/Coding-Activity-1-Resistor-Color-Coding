# main.py
from Resistor_Color_Codes import color_codes, multipliers, tolerances
from Resistor_Nominal_Resistance_Calculator import ResistorNominalResistanceCalculator
from Resistor_Limit_Value_Calculator import ResistorLimitValueCalculator

while True:
    try:
        print("Nominal Resistance Color Coding Calculator")
        band = int(input("How many bands does the resistor have? (4 or 5 bands): "))

        if band == 4:
            print('4 Band Resistor')
            color_band1 = input("Enter the first color band: ").lower()
            color_band2 = input("Enter the second color band: ").lower()
            color_band3 = input("Enter the multiplier color band: ").lower()
            color_band4 = input("Enter the tolerance color band: ").lower()

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
            print("Invalid number of bands.")

    except ValueError as e:
        print(e)

    end = input("Do you want to continue? (yes or no): ").lower()
    if end != 'yes':
        print("This is the end of the code. Thank you.")
        break
