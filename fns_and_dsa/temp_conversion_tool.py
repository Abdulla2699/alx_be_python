fahrenheit_to_celsius_factor = 5 / 9
celsius_to_fahrenheit_factor = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

def convert_to_fahrenheit(celsius):
    return (celsius * celsius_to_fahrenheit_factor) + 32

def main():
    try:
        temperature_input = input("enter the temperature to convert: ").strip()
        
        try:
            temperature = float(temperature_input)
        except ValueError:
            raise ValueError("invalid temperature. please enter a numeric value.")
        
        unit = input("is this temperature in celsius or fahrenheit? (c/f): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°c is {converted_temp:.14f}°f")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°f is {converted_temp:.14f}°c")
        else:
            raise ValueError("invalid unit. please enter 'c' for celsius or 'f' for fahrenheit.")
    except ValueError as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
