# Write a function convert_temp(temp, from_scale, to_scale) converting temperature from one scale to another. Return converted temp value.
#
# Round converted temp value to an integer(!).
#
# Reading: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
#
# possible scale inputs:
#     "C"  for Celsius
#     "F"  for Fahrenheit
#     "K"  for Kelvin
#     "R"  for Rankine
#     "De" for Delisle
#     "N"  for Newton
#     "Re" for Réaumur
#     "Ro" for Rømer
# temp is a number, from_scale and to_scale are strings.
#
# convert_temp(   100, "C",  "F") # => 212
# convert_temp(    40, "Re", "C") # => 50
# convert_temp(    60, "De", "F") # => 140
# convert_temp(373.15, "K",  "N") # => 33
# convert_temp(   666, "K",  "K") # => 666

def convert_temp(temp, from_scale, to_scale):
    # Convert from 'from_scale' to Celsius (C)
    if from_scale == "C":
        celsius = temp
    elif from_scale == "F":
        celsius = (temp - 32) / 1.8
    elif from_scale == "K":
        celsius = temp - 273.15
    elif from_scale == "R":
        celsius = (temp - 491.67) / 1.8
    elif from_scale == "De":
        celsius = 100 - temp / 1.5
    elif from_scale == "N":
        celsius = temp / 0.33
    elif from_scale == "Re":
        celsius = temp / 0.8
    elif from_scale == "Ro":
        celsius = (temp - 7.5) / 0.525
    else:
        raise ValueError(f"Unknown scale: {from_scale}")

    # Convert from Celsius (C) to 'to_scale'
    if to_scale == "C":
        result = celsius
    elif to_scale == "F":
        result = celsius * 1.8 + 32
    elif to_scale == "K":
        result = celsius + 273.15
    elif to_scale == "R":
        result = (celsius + 273.15) * 1.8
    elif to_scale == "De":
        result = (100 - celsius) * 1.5
    elif to_scale == "N":
        result = celsius * 0.33
    elif to_scale == "Re":
        result = celsius * 0.8
    elif to_scale == "Ro":
        result = celsius * 0.525 + 7.5
    else:
        raise ValueError(f"Unknown scale: {to_scale}")

    return round(result)
