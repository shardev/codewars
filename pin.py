def get_pins(observed):
    similars = {
        '1': ['2', '4'],
        '2': ['1', '3', '5'],
        '3': ['2', '6'], 
        '4': ['1', '5', '7'], 
        '5': ['2', '4', '6', '8'],
        '6': ['3', '5', '9'], 
        '7': ['4', '8'], 
        '8': ['5', '7', '9', '0'], 
        '9': ['6', '8'], 
        '0': ['8']    
        }
    pass # TODO: This is your job, detective! 


get_pins('8')  # ['5','7','8','9','0'])
get_pins('11') # ["11", "22", "44", "12", "21", "14", "41", "24", "42"])

get_pins('369') 
# [
        # "339","366","399","658","636","258","268","669","668","266","369","398",
        # "256","296","259","368","638","396","238","356","659","639","666","359",
        # "336","299","338","696","269","358","656","698","699","298","236","239"
# ]

369
3