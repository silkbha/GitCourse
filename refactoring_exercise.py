""" Code refactoring exercise.
"""


def celsius_to_kelvin(value):
    return value + 273.15

def kelvin_to_celsius(value):
    return value - 273.15

def celsius_to_fahrenheit(value):
    return (value * (9 / 5)) + 32

def fahrenheit_to_celsius(value):
    return (value - 32) * (5/9)

def fahrenheit_to_kelvin(value):
    celsius = fahrenheit_to_celsius(value)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(value):
    celsius = kelvin_to_celsius(value)
    return celsius_to_fahrenheit(celsius)


def check_validity(value,unit):
    """
    """
    # Check unit string validity
    if unit == "C":
        kelvin = celsius_to_kelvin(value)
    elif unit == "F":
        kelvin = fahrenheit_to_kelvin(value)
    elif unit == "K":
        kelvin = value
    else:
        raise ValueError("Invalid unit")
    # Check temperature value validity
    if kelvin < 0:
        raise ValueError("Invalid temperature: below absolute zero")
    

def convert_temperature(value, input_unit, output_unit):
    """
    """
    check_validity(value, unit)
    
    if input_unit == output_unit:
        return value
    
    # Convert
    if input_unit == "C":
        kelvin      = celsius_to_kelvin(value)
        fahrenheit  = celsius_to_fahrenheit(value)
    elif input_unit == "F":
        celsius     = fahrenheit_to_celsius(value)
        kelvin      = fahrenheit_to_kelvin(value)    
    else: # input_unit == "K"
        celsius     = kelvin_to_celsius(value)
        fahrenheit  = kelvin_to_fahrenheit(value)
    
    # Output
    if output_unit == "C":
        return celsius
    elif output_unit == "F":
        return fahrenheit
    else: # output_unit == "K"
        return kelvin


#################################################################################
# ORIGINAL
#################################################################################

def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                fahrenheit = (celsius * (9 / 5)) + 32
                if fahrenheit < -459.67:
                    # Invalid temperature, below absolute zero
                    return "Invalid temperature"
                else:
                    return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return celsius, fahrenheit
    else:
        return "Invalid unit"
