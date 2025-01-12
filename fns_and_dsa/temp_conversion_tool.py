# define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(c):
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature():
    while True:
        temp_input = input("enter the temperature to convert: ").strip()
        try:
            return float(temp_input)
        except ValueError:
            print("invalid temperature. please enter a numeric value.")

def get_unit():
    while True:
        unit = input("is this temperature in celsius or fahrenheit? (c/f): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("invalid unit. please enter 'c' for celsius or 'f' for fahrenheit.")

def main():
    temperature = get_temperature()
    unit = get_unit()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°c is {converted_temp:.14f}°f")
    else:
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°f is {converted_temp:.14f}°c")

if __name__ == "__main__":
    main()
