FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp = input("Enter the temperature to convert: ")

    try:
        float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{float(temp)}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temp)
        print(f"{float(temp)}°F is {result}°C")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
