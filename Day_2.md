# Collaborative Document Day 2

2025-03-18-ds-cr-TU-Delft

Welcome to The Workshop Collaborative Document.

This Document is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents.

----------------------------------------------------------------------------


This is the Document for today: https://edu.nl/gw98c

Collaborative Document day 1: https://edu.nl/qfvt9

Collaborative Document day 2: https://edu.nl/gw98c


##  🫱🏽‍🫲🏻 Code of Conduct

Participants are expected to follow these guidelines:
* Use welcoming and inclusive language.
* Be respectful of different viewpoints and experiences.
* Gracefully accept constructive criticism.
* Focus on what is best for the community.
* Show courtesy and respect towards other community members.

 If you feel that the code of conduct is breached, please talk to one of the instructors (if the complaint is for one of the participants) or send an email to training@esciencecenter.nl (if the complaint is for one of the instructors).
 
## ⚖️ License

All content is publicly available under the Creative Commons Attribution License: [creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/).

## 🙋Getting help

To ask a question, just raise your hand.

If you need help from a helper, place a pink post-it note on your laptop lid. A helper will come to assist you as soon as possible.

## 🖥 Workshop website

[link](https://esciencecenter-digital-skills.github.io/2025-03-18-ds-cr-TU-Delft)

🛠 Setup

[Day 1](https://carpentries-incubator.github.io/collaborative-git-and-github-lesson/#software-setup)
[Day 2](https://carpentries-incubator.github.io/good-practices-lesson/#software-setup)


## 👩‍🏫👩‍💻🎓 Instructors

Lucas Esclapez, Olga Lyashevska

## 🧑‍🙋 Helpers

~~Heather Andrews~~, Carlos Utrilla Guerrero, Leila Inigo de la Cruz, Raul Ortiz, ~~Yasel Quintero, Selin Kubilay~~

## 👩‍💻👩‍💼👨‍🔬🧑‍🔬🧑‍🚀🧙‍♂️🔧 Roll Call
Name/ pronouns (optional) / job, role / social media (twitter, github, ...) / background or interests (optional) / city

## 🗓️ Agenda
|  Time | Topic                                  |
| -----:|:-------------------------------------- |
|  9:30 | Welcome and icebreaker                 |
| 09:45 | Writing modular code                   |
| 10:45 | Writing modular code                   |
| 11:30 | Coffee break                           |
| 11:45 | Documentation                          |
| 12:30 | Lunch Break                            |
| 13:30 | Introduction to testing                |
| 14:15 | Coffee break                           |
| 14:30 | Introduction to Continuous Integration |
| 15:15 | Coffee break                           |
| 15:30 | Introduction to Continuous Integration |
| 16:30 | END                                    |

## 🏢 Location logistics
Ask Paula

## 🎓 Certificate of attendance
If you attend the full workshop you can request a certificate of attendance by emailing to training@esciencecenter.nl.
Please request your certificate within 8 months after the workshop, as we will delete all personal identifyable information after this period.

🍦 Icebreaker

Mood checker!

| Name     | Your mood in 3 words     |                                          |
| -------- | ------------------------ | ---------------------------------------- |
| Giulia   |  Too many things on my head                         |                                          |
| Lili     | Fun, informative, pumped |                                          |
| Max      | Interested!              |                                          |
| Pedro    | Tired not tired           |                                          |
| Veerle   | Tired but interested     |                                          |                                        |
| Andres   | Tired but good, sleepy   |                                          |
| Tamara   | Hoping to learn          |                                          |
| Tarun    |                          |                                          |
| Frederik | Energized, ready         |                                          |
| Sadaf    | Excited,  try to be fast |                                          |
| Lorenzo | sleepy but excited and ready | 
| Moji    | tired, excited               |                                          |     |     |
| Shaina  | Ready to learn               | 
| Alessio | Let's go :)                  |                   | Lucas | Tired but ready for teaching   | 
| Sajjad  | Uphappy with house neighbors |                                          |     |     |
| Ben    | Tired, curious, interested |
| Wessel | Happy, partly asleep |
| Laura  | sleepy, frustrated with data fitting, irritable               |
|  Leila      |  tired but looking forward!                   |
|    Jing    |       Tired, but learned a lot.              |
|        |                     |


## 🔧 Exercises

## 🧠 Collaborative Notes

Introductory presentation about what is modularity , you can find it [here](https://esciencecenter-digital-skills.github.io/digital-skills-slides/modules/good-practices-lesson/modular-code-slides) 


### Developing Modular Code

Software can be built from smaller blocks/elements that are self-contained and independent. Each element has a specific task. This makes it easier to understand and debug the code. 

#### What are these blocks/elements (going from small to big)? 
- functions
- classes
- modules
- libraries/packages

#### Why write modular code? 
- Increase robustness of your code
    - When code is well-written, it can be tested
    - Keeps the code-base organised and bug-free
- Easier to maintain
    - Readable and understandable
    - Modules can be debugged separately
    - Modules only need to be improved/optimised once
- Allow reusability
    - A module can live independently of its original context
    - Can be used in multiple projects
- Facilitate scalability
- Create opportunity for innovation
    - Easier to add new features
- To save time:
    - Although there is an initial time investment, you save time in the future


#### What is a good module?
A good module performs limited and clearly defined tasks
Name your module something clear:
- be descriptive and clear
- focus on human intelligibility
- follow language specific conventions
- avoid abbreviations

Your code should be readable
- More readable code does not mean shorter code. 

#### Pure vs Impure functions
Impure functions fo not always give the same answer or affects code outside of the function - known as side effects. 
- Don't reassign variables and pay attention to global variables

#### Identifying opportunities for modularisation

- Readable code: Code is read more than it is written or someone outside of the project cannot understand what the code does.
- Repetition: If you find that you are copy-pasting code to make slight changed
    - Don't Repeat Yourself (DRY), place reused code into a function
    - Identify functions by their action
- Nested code: for example for loops within for loops etc
    - You can split these into multiple functions. For example, into the separate actions. 
- Let tests help you: If you can easily write a test for your function, then it is probably good. 
    - Is the input/output clear?

 


- Tools to check the cognitive complexity of a code: SonarCloud (safer for open source projects since it will store your code in their sonarcloud server) 
    - If you have commercial partners , check the policy at your university 
- Cognitive complexity should be less than 15(related to how many nested code we have in one block), to be OK. If it has more than 15 you should modularize the code

## Exercise

**Refactor the code by extracting functions without altering its functionality.**

- What functions did you create?
- What strategies did you use to identify them?
- Share your answers in the collaborative document.

```python=
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
```
## Participants answers 

 - You can add a function to check for valid temperature along with unit.

```python= 
# Define valid temperature ranges for each unit
VALID_RANGES = {
    "F": (-459.67, float('inf')),
    "C": (-273.15, float('inf')),
    "K": (0, float('inf'))
}

def is_valid_temperature(temperature, unit):
    if unit in VALID_RANGES:
        min_temp, max_temp = VALID_RANGES[unit]
        return min_temp <= temperature <= max_temp
    return False

def is_valid_unit(unit):
    return unit in VALID_RANGES

def convert_temperature(temperature, unit):
    '''
    Convert a temperature from one unit to all other units.
    The valid units are Fahrenheit (F), Celsius (C), and Kelvin (K).
    '''
    if not is_valid_unit(unit):
        return "Invalid unit"
    
    if not is_valid_temperature(temperature, unit):
        return "Invalid temperature"

    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        # Convert Celsius to Kelvin
        kelvin = temperature + 273.15
        return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * (9 / 5)) + 32
        return celsius, fahrenheit
    else:
        return "Invalid unit"

def main():
    # test temperatures to convert
    temperatures = [
        (100, "F"),
        (0, "C"),
        (273.15, "K"),
        (-500, "F"),  # Invalid temperature
        (100, "X")    # Invalid unit
    ]

    for temp, unit in temperatures:
        result = convert_temperature(temp, unit)
        print(f"Converting {temp}°{unit}: {result}")

if __name__ == "__main__":
    main()
```


```python= 
def convert_fahrenheit_to_celsius(temperature):
    return (temperature - 32) * (5 / 9)

def convert_celsius_to_fahrenheit(temperature):
    return (temperature * (9 / 5)) + 32

def convert_celsius_to_kelvin(temperature):
    return temperature + 273.15

def convert_kelvin_to_celsius(temperature):
    return temperature - 273.15

def convert_temperature(temperature, unit):
    # Check whether temperature is valid and convert to celsius
    if unit == "F":
        if temperature < -459.67:
            return "Invalid temperature"
        else:
            celsius = convert_fahrenheit_to_celsius(temperature)
    elif unit == "C":
        if temperature < -273.15:
            return "Invalid temperature"
        else:
            celsius = temperature
    elif unit == "K":
        if temperature < 0:
            return "Invalid temperature"
        else:
            celsius = convert_kelvin_to_celsius(temperature)
    
    # Converto to fahrenheit and kelvin
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    kelvin     = convert_celsius_to_kelvin(celsius)
    
    return celsius, fahrenheit, kelvin
```
```python=
def convert_temperature(temperature,unit_in,unit_out):
    """
    Converts a temperature value from one unit to another.

    Parameters:
        temperature (float): The temperature value to be converted.
        unit_in (str): The unit of the input temperature. Must be one of 'C' (Celsius), 'F' (Fahrenheit), or 'K' (Kelvin).
        unit_out (str): The unit of the output temperature. Must be one of 'C' (Celsius), 'F' (Fahrenheit), or 'K' (Kelvin).

    Returns:
        float or str: The converted temperature in the desired unit, or a string "Invalid temperature" if the input temperature is below absolute zero.

    Raises:
        KeyError: If `unit_in` or `unit_out` is not a valid temperature unit.
    """
    scale_to_C = {'C':1.0,'F':5/9,'K':1.0}
    bias_to_C = {'C':0.0,'F':-32.0,'K':-273.15}
    T_limit = {'C':-273.15,'F':-459.67,'K':0.0}
    
    if not check_unit_validity(unit_in) or not check_unit_validity(unit_out):
        return "Invalid unit"    
    if temperature < T_limit[unit_in]:
        return "Invalid temperature"
    T_C=(temperature+bias_to_C[unit_in])*scale_to_C[unit_in]
    T_out=T_C/scale_to_C[unit_out]-bias_to_C[unit_out]
    return T_out



def check_unit_validity(unit):
    if unit in ['C','F','K']:
        return True
    else:
        return False

def convert_temperature(unit_in, temp):
    C=0
    K=0
    F=0

    if unit_in == "C":
        C = temp
        K = temp + 273.15
        F = temp * 9/5 + 32

    elif unit_in == "K":
        K = temp
        C = temp - 273.15
        F = C * 9/5 + 32

    elif unit_in == "F":
        F = temp
        C = (temp - 32) * 5/9
        K = C + 273.15
    
    if K < 0:
        return "Invalid temperature"
    
    return C, K, F
#################################################################


def _celsius_to_kelvin(celsius):
    if celsius < -273.15:
        return None
    return celsius + 273.15

def _celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return None
    return celsius * 9/5 + 32

def _kelvin_to_celsius(kelvin):
    if kelvin < 0:
        return None
    return kelvin - 273.15

def _kelvin_to_fahrenheit(kelvin):
    if kelvin < 0:
        return None
    return (kelvin - 273.15) * 9/5 + 32

def _fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        return None
    return (fahrenheit - 32) * 5/9

def _fahrenheit_to_kelvin(fahrenheit):
    if fahrenheit < -459.67:
        return None
    return (fahrenheit - 32) * 5/9 + 273.15

def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius & Kelvin
        celsius = _fahrenheit_to_celsius(temperature)
        kelvin = _fahrenheit_to_kelvin(temperature)
        if celsius is None or kelvin is None:
            return None, None, "Invalid temperature"
        return [celsius, kelvin], ["C", "K"], f"{temperature} F = {celsius:.2f} C = {kelvin:.2f} K"
    elif unit == "C":
        # Convert Celsius to Fahrenheit & Kelvin
        fahrenheit = _celsius_to_fahrenheit(temperature)
        kelvin = _celsius_to_kelvin(temperature)
        if fahrenheit is None or kelvin is None:
            return None, None, "Invalid temperature"
        return [fahrenheit, kelvin], ["F", "K"], f"{temperature} C = {fahrenheit:.2f} F = {kelvin:.2f} K"
    elif unit == "K":
        # Convert Kelvin to Celsius & Fahrenheit
        celsius = _kelvin_to_celsius(temperature)
        fahrenheit = _kelvin_to_fahrenheit(temperature)
        if celsius is None or fahrenheit is None:
            return None, None, "Invalid temperature"
        return [celsius, fahrenheit], ["C", "F"], f"{temperature} K = {celsius:.2f} C = {fahrenheit:.2f} F"
    else:
        return None, None, "Invalid unit"
    
temperature = 350
unit = "K"

print(convert_temperature(temperature, unit))

temperature, units, message = convert_temperature(temperature, unit)

temperature = -500
unit = "C"

print(convert_temperature(temperature, unit))

temperature, units, message = convert_temperature(temperature, unit)
```
```
def check_validity(celsius, kelvin, fahrenheit):
    if celsius < -273.15 or kelvin < 0 or fahrenheit < -459.67:
            return  True
    else:
            return False        
      

def convert_temperature(temperature, unit):
    
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        
        check = check_validity(celsius, kelvin, temperature)
        
        if check:
            return "Invalid temperature"
    
        else:
            return celsius, kelvin
        
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        kelvin = temperature + 273.15
        
        check = check_validity(temperature , kelvin, fahrenheit)
        
        if check:
            return "Invalid temperature"
        else:
            return fahrenheit, kelvin
        
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * (9 / 5)) + 32
        
        check = check_validity(temperature , kelvin, fahrenheit)
        
        if check:
           return "Invalid temperature"
        return celsius, fahrenheit
    else:
        return "Invalid unit"
```
    




```python=
def is_valid_temperature(temperature, unit):
    if unit == "F":
        if temperature < -459.67:
            return False, "Invalid temperature"
        else:
            return True, None
    elif unit == "C":
        if temperature < -273.15:
            return False, "Invalid temperature"
        else:
            return True, None
    elif unit == "K":
        if temperature < 0:
            return False, "Invalid temperature"
        else:
            return True, None
    else:
        return False, "Invalid unit"
    
class Temperature:
    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit
        if self.unit == "F":
            self.fahrenheit = self.temperature
            self.celsius = (self.temperature - 32) * (5 / 9)
            self.kelvin = self.celsius + 273.15
        
        elif self.unit == "C":
            self.celsius = self.temperature
            self.fahrenheit = self.celsius * (9 / 5) + 32
            self.kelvin = self.celsius + 273.15
        
        elif self.unit == "K":
            self.kelvin = self.temperature
            self.celsius = self.kelvin - 273.15
            self.fahrenheit = self.celsius * (9 / 5) + 32
    
    def get_celsius(self):
        return self.celsius
    
    def get_fahrenheit(self):
        return self.fahrenheit
    
    def get_kelvin(self):
        return self.kelvin

def convert_temperature(temperature, unit):
    temp = Temperature(temperature, unit)
    if not is_valid_temperature(temperature, unit)[0]:
        return is_valid_temperature(temperature, unit)[1]
    if unit == "F":
        return temp.get_celsius(), temp.get_kelvin()
    elif unit == "C":
        return temp.get_fahrenheit(), temp.get_kelvin()
    elif unit == "K":
        return temp.get_fahrenheit(), temp.get_celsius()
    else:
        return "Invalid unit"
    
def test_answer():
    assert convert_temperature(100, "F") == (37.77777777777778, 310.92777777777775)
    assert convert_temperature(100, "C") == (212.0, 373.15)
    assert convert_temperature(100, "K") == (-279.66999999999996, -173.14999999999998)
    assert convert_temperature(100, "X") == "Invalid unit"
    assert convert_temperature(-500, "F") == "Invalid temperature"
    print("All tests passed")

test_answer()
```

```python=
# Dictionary providing the absolute temperature threshold for each temperature unit type
min_temperatur_threshold_dict = {
    "C": -273.15,
    "K": 0,
    "F": -459.67
}

def temperature_is_invalid(temperature_value: float, unit: str) -> [float, str]:
    """
    Checks if provided temperature is below absolute zero. An absolute value threshold is provided for
    each temperature unit type (C, K, F).

    args:
        temperature_value (float)
        unit - units the provided temperature is in (C, K, F)

    returns:
        bool (True if temperature is invalid, False if it is valid)
    """
        
    if temperature_value < min_temperatur_threshold_dict[unit]:
            # Invalid temperature, below absolute zero
            return True
    else:
        return False
    

def convert_farenheit_to_celsius(farenheit_temperature: float):
    convertet_temperature = temperature_is_invalid()
    return (farenheit_temperature - 32) * (5 / 9)

def convert_celsius_to_farenheit(celsius_temperature: float):
    return (celsius_temperature * (9 / 5)) + 32

def convert_celcius_to_kelvin(celsius_temperature: float):
    return celsius_temperature + 273.15

def convert_kelvin_to_celsius(kelvin_temperature: float):
    return kelvin_temperature - 273.15


def convert_temperature(temperature: float, incoming_unit: str) -> [[float, float], str]:
    """
    Converts temperature from specified incoming unit into the other two tempeature unit options (between
    Celcius, Kelvin and Farenheit). 

    If temperature is below abslute temperature value, instead returns an error message
    """

    # Checks if temperature is above absolute temperature
    if temperature_is_invalid(temperature_value=temperature, unit=incoming_unit):
        return "Invalid temperature"

    elif incoming_unit == "F":
        celsius = convert_farenheit_to_celsius(temperature)
        kelvin = convert_celcius_to_kelvin(celsius)
        return celsius, kelvin

    elif incoming_unit == "C":
        kelvin = convert_celcius_to_kelvin(temperature)
        fahrenheit = convert_celsius_to_farenheit(temperature)
        return fahrenheit, kelvin
        
    elif incoming_unit == "K":
        celsius = convert_kelvin_to_celsius(temperature)
        fahrenheit = convert_celsius_to_farenheit(celsius)
        return fahrenheit, kelvin
        
    else:
        return "Invalid temperature unit provided"


def main() -> None:
    output = convert_temperature(temperature=100, incoming_unit="C")
    print(output)

    output = convert_temperature(temperature=-1000, incoming_unit="C")
    print(output)

if __name__ == "__main__":
    main()

```
```python
def Fahrenheit_to_C_and_K(T):
    celsius = (T - 32) * (5 / 9)
    kelvin = celsius + 273.15

    if celsius < -273.15:
        return "Temperature below absolute zero, invalid"
    else:
        return celsius, kelvin

def Celsius_to_K_F(T):
    if T < -273.15:
        return "Temperature below absolute zero, invalid"

    else:
        kelvin = T + 273.15
        fahrenheit = (T * (9 / 5)) + 32

        return kelvin, fahrenheit


def Kelvin_to_C_F(T):
    if T < 0:
        return "Temperature below absolute zero, invalid"

    else:

        celsius = T - 273.15
        fahrenheit = (celsius * (9 / 5)) + 32

        return celsius, fahrenheit

def convert_temperature(temperature, unit):
    if unit == "F":
         celsius, kelvin = Fahrenheit_to_C_and_K(temperature)
         return celsius, kelvin

    elif unit == "C":
        kelvin, fahrenheit = Celsius_to_K_F(temperature)
        return  kelvin, fahrenheit

    elif unit == "K":
        celsius, fahrenheit = Kelvin_to_C_F(temperature)
        return celsius, fahrenheit

    else:
        return "Invalid unit"
```

```python=

#-----------------------------------------------
def convert_temperature(temperature, unit):
    if (check_invalid(temperature, unit)):
        return 0
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        # Convert Fahrenheit to Kelvin
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        # Convert Celsius to Kelvin
        kelvin = temperature + 273.15
        return fahrenheit, kelvin
    else:
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        # Convert Kelvin to Fahrenheit
        fahrenheit = (celsius * (9 / 5)) + 32
        return celsius, fahrenheit

def check_invalid(temperature, unit):
    #Function to check if the given temperature and unit are valid
    if unit == 'C' and temperature < -273.15:
        #Invalid in Celsius
        print("Invalid temperature")
        return 1
    elif unit == 'F' and temperature < -459.64:
        #Invalid in Fahrenheit
        print("Invalid temperature")
        return 1
    elif unit =='K' and temperature < 0:
        #Invalid in Kelvin
        print("Invalid temperature")
        return 1
    elif unit!='C' and unit!='F' and unit!='K':
        #Invalid unit
        print("Invalid unit")
        return 1
    return 0
```

```python

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
```
Look for a model answer in [here](https://carpentries-incubator.github.io/good-practices-lesson/2-modular-code.html)


### Documentation

Documentation helps others, including your future self, understand what your code is doing. 

#### Types of documentation:
- <b>README files</b>: this is what is immediately displayed on the landing page of your repository. It is one of the first things people will see. A good README file includes the following:
    - Motivation: What is the purpose of this software
    - Authors and how to reach them 
    - Installation guide
    - Links to tutorials/examples etc
    - Table of contents
    - DOI reference: citation information
    - Licence
    - Sample input/output
    - Contribution guidelines
    - Badges: a unified way to present condensed pieces of information about your projects. A badge consists of a small image and a URL that the image points to. For example: code coverage, pypi link, DOI. 
    - good example: https://github.com/pandas-dev/pandas

- <b>In-code documentation</b>: Makes code more understandable and explains decisions were made. 
    - Comments: You shouldn't use comments when the code is already self-explanatory or to replace good coding practices. Also do not use it replace version control or keeping old code. 
    - Docstrings: a specific kind of comment that describes a function/class. It becomes available as part of the code (shows up when using "help"). Can be used to generate API documentation. There are different conventions for docstrings. Choose one and stick to it. 
- <b>API documentation</b>: Application Programming Interface: it works as a reference for every function in the code, describing what goes in and what goes out. This is generally only for projects that are little bit larger with multiple users. 
- <b>Tutorials</b>: Examples, typical use cases etc (e.g. "Getting Started")

### Exercise : Examples of good and bad documentation


This is well documented with multiple examples and clear explanation of how their code works : https://amrex-combustion.github.io/PeleLMeX/manual/html/Model.html



This project has great documentation. Has a quick start guide for installing/building and running locally, begginer and advanced guides, description of architecture and classes with visual figures, practical examples, and an entire reference open source textbook for the theory behind the source code: https://openmdao.org/newdocs/versions/latest/getting_started/getting_started.html



Doc strings, clarly defined variable types as input to functions, jupiter notebooks tutorials, wikis, requirements, 

examples with figures, explanation on how to change parameters

Giving units  of input/output, clear description what it does, some examples how to use 

Good documentation: Numpy documentation, clearly indicates input and output variables, description of what the code does and useful examples.

Less good documentation: My own documentation in docstrings. Documentation takes up more space in the files than code. Makes code much more difficult to find/read.

Clear labeling structure, experience with PDMs/PLMs with automatic version control and labeling. (background in mechanical design/consumer products, limited coding experience but feel this applies to collaboration in ME design)

Clear changelogs, differences between versions (especially if functionality of a module changes!).

Matlab documentation, clearly defined input/output. live/edditatble examples in editor.

MATLAB Reservoir Simulation Toolbox (https://www.sintef.no/projectweb/mrst/) was so perfect that I learned most of my knowledge of reservoir simulation from this repository. They have two nice books describing their code snippets. 

My colaborators code was not documented well, it had comments but no overview of how it works together-  I had to use it while they were away travelling for a month. 


## Exercises

#### Bird Cloud GNN link
- https://github.com/point-cloud-radar/bird-cloud-gnn


#### Draft or improve a README for one of your recent projects 

Try to draft a brief README or review a README which you have written for one of your projects.
You can work individually, but you could also discuss whether anything can be improved on your neighbour's README file(s).
Think about the user (which can be a future you) of your project, what does this user need to know to use or contribute to the project? And how do you make your project attractive to use or contribute to?

#### Add a badge
Add a badge to your README file. This comes down to simply adding a link to an image on top of your README file.

You can pick from:

- [A simple static badge](https://shields.io/badges). You can decide what it says and what color it is.
- [The howfairis badge](https://app.howfairis.com). It indicates whether a project is in line with the
[FAIR software recommendations.](https://fair-software.eu/)
- [A badge reporting test coverage](https://coveralls.io/) (we will discuss testing and continuous integration in upcoming episodes)
- [A badge linking to a publication in Zenodo](https://tutorials.inbo.be/tutorials/git_zenodo/)
- [A badge showing the license](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba)

#### (optional) Make your writing bold and clear
Try the https://hemingwayapp.com/ to analyse your README file and make your writing bold and clear.

 
### Citation
It is easy to correctly cite a paper: all the necessary information (metadata) can be found on the title page or the article website.

Software and datasets have no title page, the relevant information is often less obvious. To get credit for your work, you should provide citation information for your software.

A good way to add citation information is by including a [CITATION.cff](https://citation-file-format.github.io/) file (Citation File Format) in the root of your repository. This plain text file, written in YAML format, contains all the necessary citation details in a structured manner.

Platforms like GitHub, Zenodo, and Zotero reuse the citation metadata you provide. GitHub, for example, automatically renders the file on the repository landing page and provides a BibTeX snippet which users can simply copy!

#### Minimal example for a CITATION.cff file

```yaml
authors:
- family-names: Doe
given-names: John
cff-version: 1.2.0
message: "If you use this software, please cite it using the metadata from this file."
title: "My research software"
```
We can also include other important information of software such as version, release date, DOI, license, keywords.

#### How to create a CITATION.cff file?

You can use the [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/) tool to create a citation file.

### Exercise: Create a CITATION.cff using cffinit
1. Follow [these steps to create a CITATION file with cffinit](https://book.the-turing-way.org/communication/citable/citable-cffinit).
1. Rename the created file to `CITATION.cff` and add it to the root folder of your repository.
1. Push your changes to `main` and check your repository in GitHub. What has happened?

## In-code documentation

In-code documentation makes code more understandable and explains decisions we made.

### When not to use:
- When the code is self-explanatory
- To replace good variable/function names
- To replace version control
- To keep old (zombie) code around

### Readable code vs commented code
```python
# convert from degrees celsius to fahrenheit
def convert(d):
return d * 5 / 9 + 32
```

vs

```python
def celsius_to_fahrenheit(degrees):
return degrees * 5 / 9 + 32
```



## Exercise: Writing good in-code comments

Let's take a look at two example comments:

**Comment A**

```python
# now we check if temperature is below -50
if temperature < -50:
print("ERROR: temperature is too low")
```

**Comment B**

```python
# we regard temperatures below -50 degrees as measurement errors
if temperature < -50:
print("ERROR: temperature is too low")
```

```python

def fahrenheit_to_celsius(temp_f: float) -> float:
    """
    Converts a temperature in Fahrenheit to Celsius.

    Args:
        temp_f: The temperature in Fahrenheit.

    Returns:
        The temperature in Celsius.
    """

    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c

```
- write this function in a python file
- type help(name of the function) in an ipython terminal




**Which of these comments is more useful? Can you explain why?**


## Exercise: Identify a proper docstring

Which of the following options is the correct function with a proper docstring?

**Option A**

```python
def check_unit_validity(unit: str) -> bool:
"""
Checks if a unit is valid.

Args:
unit: The unit to check. Must be "C", "F", or "K".

Returns:
True if the unit is valid, False otherwise.
"""
if not unit in ["C", "F", "K"]:
return False
return True
```

**Option B**

```python
def check_unit_validity(unit):
"""
Checks if a unit is valid.

Args:
unit (str): The unit to check. Must be "C", "F", or "K".

Returns:
bool: True if the unit is valid, False otherwise.
"""
if not unit in ["C", "F", "K"]:
return False
return True
```

**Option C**

```python
def check_unit_validity(unit: str) -> bool:
"""
Validates the unit.

Parameters:
unit (str): The unit to check.

Returns:
bool: True if the unit is valid, False otherwise.
"""
if not unit in ["C", "F", "K"]:
return False
return True
```

## MKdocs installation

Using conda: https://carpentries-incubator.github.io/good-practices-lesson/index.html

Using pip in git Bash, Unix terminal:

```bash

python -m pip install mkdocs mkdocstrings

``` 

### MKdocs documentation

- Go to a folder of your project in your working directory

```bash=

mkdocs new . 
ls # you should see mkdocs.yml and docs/
nano mkdocs.yml
```
```yaml=
site_name: Temperature conversion

theme:
    name: "mkdocs"

nav: 
    - Overview: index.md 

plugins: 
    - mkdocstrings

```

```bash=
mkdocs build
mkdocs serve
```
### API documentation

```bash=

nano api.md

```
Fill in the api.md the following: 

```bash=
:::NAME OF YOUR PYTHON SCRIPT
```

```bash
nano mkdocs.yml 

```

fill the following:

```yaml=
site_name: Temperature conversion

theme:
    name: "mkdocs"

nav: 
    - Overview: index.md 
    - API: api.md

plugins: 
    - mkdocstrings

```

```bash

mkdocs build
mkdocs serve

```

## Testing

- Why:
    - preserve functionality
        - detect new errors early
        - avoid unexpected outputs
    - help users
        - verify correct installation
        - ensure reproducibility
    - enable developers
        - manage complexity
        - simplify refactoring
        - facilitate collaboration
- Test types:
    - Exceptions in the codebase
        - intended to handle "expected" problems
        - sound an alarm as soon as the problem arises
        - provide clear feedback to the user
    - Unit testing
        - smallest possible unit
        - no dependency on outside code but not always the case, example if you use a numpy function inside your function
        - replace them wtih mocks, stubs , etc 
    - Integration testing
        - Test interactions between units
        - Can be on small scales , systems wide
- Testing frameworks for unit test
    - Pytest,Junit(Java)

- Testing metrics
    - Coverage 
        - Proportion of code that is executed during testing
        - Target >=80%
    - Ratio
        - Lines of code:lines of test
        - Target 1:3
    - Metrics can be misleading

## Pytest example

```bash=
mkdir pytest-example
cd pytest-example

nano example.py 

```
write inside the file: 
```python=

def add(a, b):
   return a + b
 
 
def test_add():  # Special name!
    assert add(2, 3) == 5  # What's `assert`? 
    assert add('space', 'ship') == 'spaceship'

```
```bash=

pytest example.py

```

- Pytest expects that the test functions start with `test_`

- Now make it failed but switching the `+` in the `add` function by a `-` and run again `pytest example.py` in the terminal

### Take away

- Use pure functions when possible
- Testing does not have to be hard
    - pytest for python
    - Test often
    - Test functionalities
- Aim for a balance between unit and integration tests
- Testing removes the dread of refactoring



## Test-Driven Development: FizzBuzz Function (15 min)

The function `fizz_buzz()` takes an integer argument and returns it, BUT:

- Fails on zero or negative numbers.
- Instead returns "Fizz" on multiples of 3.
- Instead returns "Buzz" on multiples of 5.
- Instead returns "FizzBuzz" on multiples of 3 and 5.

Create an empty function `fizz_buzz()` and go through the conditions listed above, one by one:

1. Write a test for the condition.
2. Edit the `fizz_buzz()` function until the test passes.

Then discuss together the different solutions.

### Solution for FizzBuzz:

```python
import pytest

def fizz_buzz(input):
    if input <= 0:
        raise ValueError('Negative or zero input not allowed')
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input

def test_fizz_buzz():
    with pytest.raises(ValueError):
        fizz_buzz(0)
    with pytest.raises(ValueError):
        fizz_buzz(-2)
    assert fizz_buzz(1) == 1
    assert fizz_buzz(3) == 'Fizz'
    assert fizz_buzz(4) == 4
    assert fizz_buzz(5) == 'Buzz'
    assert fizz_buzz(6) == 'Fizz'
    assert fizz_buzz(10) == 'Buzz'
    assert fizz_buzz(15) == 'FizzBuzz'
    
```

## CI 

- Motivation

    - how to implement automatic testing each time we push changes to the repository? 
- What else?
    - Building and compiling
    - Code, Documentation
    - Deploying (Pypi)
    - Just like these slides
    - Code analysis 
    
- Hands-On (Demo)

 
    - Use the `Python Application` available workflow from Github

### Exercise CI

### Exercise: Full-cycle collaborative workflow

The exercise takes 30-40 minutes.

In this exercise, everybody will:

- A. Set up automated tests with GitHub Actions
- B. Make test fail / find a bug in their repository
- C. Open an issue in their repository
- D. Then each one will clone the repo of one of their exercise partners, fix the bug, and open a pull request (GitHub)
- E. Everybody then merges their co-worker’s change


#### Step 1: Create a new repository on GitHub

- Select a different repository name than your colleagues (otherwise forking the same name will be strange)
- Before you create the repository, select “Initialize this repository with a README” (otherwise you try to clone an empty repo).
- Share the repository URL with your exercise group via shared document or chat

#### Step 2: Clone your own repository, add code, commit, and push

Clone the repository.

Add a file `example.py` containing:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # do not change this line until prompted to do so.
```

Write a test function `def test_add()` for `add` to check that this function is working properly. Do NOT add a test function for `subtract` (yet).
Run pytest to ensure it works 

Then stage the file (`git add <filename>`), commit (`git commit -m "some commit message"`),
and push the changes (`git push`).


#### Step 3: Enable automated testing

In this step we will enable GitHub Actions.
- Select "Actions" from your GitHub repository page. You get to a page "Get started with GitHub Actions". 
- Select the button for "Set up this workflow" under Python Application.

![](fig/ci-python-application-workflow.png)
Select “Python application” as the starter workflow.

GitHub creates the following file for you in the subfolder `.github/workflows`:


```yaml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
```



Commit the change by pressing the "Start Commit" button.

#### Step 4: Verify that tests have been automatically run

Observe in the repository how the test succeeds. While the test is executing, the repository has a yellow marker.
This is replaced with a green check mark, once the test succeeds.

![](fig/ci-tests-succeed-screenshot.png)

Green check means passed.

Also browse the "Actions" tab and look at the steps there and their output.

#### Step 5: Add a test which reveals a problem

After you committed the workflow file, your GitHub repository will be ahead of your local cloned repository. Update your local cloned repository:

```
$ git pull origin main
```

Next uncomment add a test function `test_subtract` for to check that the `subtract` function can subtract two numbers from each other, and push it to your remote repository.
Verify that the test suite now fails on the “Actions” tab (GitHub).


#### Step 6: Open an issue on GitHub
Open a new issue in your repository about the broken test (click the “Issues” button on GitHub and write a title for the issue). The plan is that your colleague will fix the issue through a pull request

#### Step 7: Fork and clone the repository of your colleague

Fork the repository using the GitHub web interface. 
Make sure you clone the fork after you have forked it. Do not clone your colleague’s repository directly.


#### Step 8: Fix the broken test

Fix the function now and run pytest to check that it works.
Then push to _your fork_. Check whether the action now also passes.

#### Step 9: Open a pull request (GitHub)

Then before accepting the pull request from your colleague, observe how GitHub Actions automatically tested the code.

If you forgot to reference the issue number in the commit message, you can still add it to the pull request: 
`my pull request title, closes #NUMBEROFTHEISSUE`

#### Step 10

Observe how accepting the pull request automatically closes the issue (provided the commit message or the pull request contained the correct issue number).

Discuss whether this is a useful feature. And if it is, why do you think is it useful?

### Exercice available here:
https://carpentries-incubator.github.io/good-practices-lesson/5-ci.html

### Deploying documentation using Github pages

- GitHub pages can be setup inside your GitHub repository
- It automatically deploys your MkDocs or Sphinx-generated documentation. Or in other words it creates a website for you that renders your documentation.

### Exercise: Deploy documentation to GitHub Pages

(If not done already) lets commit our changes to the main branch and push our changes to GitHub

```bash
git add mkdocs.yml
git add docs/
git add site/
git commit -m "Add documentation"
git push origin main
```
We can then deploy our documentation to gh-pages with mkdocs, this will:
- Push the documentation to a gh-pages branch of your repository (& create it if it does not exist)
- It will also include uncommitted changes and untracked files, which could cause problems later

<b>! Important ! Make sure there are no uncommitted changes and that your main branch is clean before running the following command! </b>

In the terminal run:
```bash
mkdocs gh-deploy
```
The output should give you some information on where the documentation can be found, click on the generated link to view the documentation! You can then also copy the link to add to the "about" section of your repository so that users can find the documentation easily. 

https://lyashevska.github.io/temperature_conversion_api_demo/api/

## ❓ Questions?



## 📢 Feedback 

### what went well

good pace, multiple helpers around


### what to improve


### Post workshop-survey

Please fill out the [post-workshop survey](https://www.surveymonkey.com/r/KLFDNBW)



## 📚 Resources

[Cognitive complexity check tool](https://www.sonarsource.com/products/sonarcloud/)
    - Beware of whether it keeps your data/code and might cause intelectual property issues
[CFFINIT](https://citation-file-format.github.io/cff-initializer-javascript/#/)

- [Pure vs Impure functions](https://www.freecodecamp.org/news/pure-function-vs-impure-function/)
- [Slides on Modular Code](https://esciencecenter-digital-skills.github.io/digital-skills-slides/modules/good-practices-lesson/modular-code-slides#/26/0/2)
- [Generating badges for your code](https://shields.io/)
- [Choosing a docstrings style](https://joshdimella.com/blog/python-docstring-formats-best-practices)
- [Read the docs (deployment platform for documentation)](https://about.readthedocs.com/)

- [Installation instruction for conda, pytest, mkdocs, ...](https://carpentries-incubator.github.io/good-practices-lesson/index.html#software-setup)

- [MKDocs for documentation](https://www.mkdocs.org/)