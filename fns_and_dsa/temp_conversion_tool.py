# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature_input = input("Enter the temperature to convert: ").strip()
        
        try:
            temperature = float(temperature_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.10f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.10f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
