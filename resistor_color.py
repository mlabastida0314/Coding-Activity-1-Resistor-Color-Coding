#  resistor_color.py
# This .py contains dictionaries and math computation for limit value of the resistor

# Dictionaries
# this contains the key values of the user input
# the syntax of this is key:value where the key comes from the user (c1,c2,c3,c4,c5) and the value is stored here
color_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
                  'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
# thus when this dictionary is used, it is either accessed by its key or index.
# As you can see I used a "**" double asterisks (exponent operator) to indicate as power. Since, the zeros can take up much space in lines
# I decided to shorten it up a bit using it as an arithmetic operator
multiplier = {'black': 1, 'brown': 10, 'red': 100, 'orange': 10**3, 'yellow': 10**4, 'green': 10**5,
                  'blue': 10**6, 'violet': 10**7, 'grey': 10**8, 'white': 10**9}
# in this line, I didn't use the int value of the percentages because I decided that I'll just convert it down below
# para hindi ako maguluhan sa pag access ng variable from Nominal Resistance and for limits
tolerance_dict = {'brown': '1%', 'red': '2%', 'green': "0.5%", 'blue': '0.25%',
                 'violet': '0.1%', 'gold': '5%', 'silver': '10%', 'none': '20%'}
# basically, The goal here is to make the dictionary as accessible to other functions/methods

# This method is used for calculating limits. This line takes a parameter of nominal and tolerance which is located in the Nominal_Resistance_Calculator
def calculate_limits(nominal_resistance, tolerance_value):
    # The line below Calculate the tolerance multiplier since naka exponent yung multiplier sa dictionary, need ko pang kunin yung galing sa Nonimal_Resistance
    # para masolve or makuha, instead na direct nalang (if idrect naman may convertion parin since percentage yon)
    tolerance_multiplier = 1 + (tolerance_value / 100) if tolerance_value else 1
    # for minimum limit
    min_limit = nominal_resistance / tolerance_multiplier
    # for maximum limit
    max_limit = nominal_resistance * tolerance_multiplier
    # the .2f in this code is para 2 decimal places lang ang makuha, since possible na maraming decimals after mag divide or multiply
    resistance_str = f"{nominal_resistance:.2f} Ω"        # the variable name have str because I want to convert it to string thus kaya gumamit ng fstring (f)
    min_limit_str = f"{min_limit:.2f} Ω"
    max_limit_str = f"{max_limit:.2f} Ω"
    # This prints the min and max limits of the resistor
    # so every time na icacall natin ang function na ito, The result will show because of the line below
    print(f"Limits: Min: {min_limit_str} - Max: {max_limit_str}")
    return min_limit, max_limit