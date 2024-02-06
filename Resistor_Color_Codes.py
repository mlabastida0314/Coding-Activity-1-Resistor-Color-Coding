# resistor_color_code.py
#Color Codes, Multipliers, and Tolerance Dictionary

color_codes = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
               'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9, 'gold': 5}

multipliers = {'black': 1, 'brown': 10, 'red': 100, 'orange': 10**3,
               'yellow': 10**4, 'green': 10**5, 'blue': 10**6,
               'violet': 10**7, 'grey': 10**8, 'white': 10**9,
               'gold': 0.1, 'silver': 0.01}

tolerances = {'brown': '1', 'red': '2', 'green': "0.5", 'blue': '0.25',
              'violet': '0.1', 'gold': '5', 'silver': '10', 'none': '20'}

