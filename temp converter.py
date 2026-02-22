def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def convert_temperature():
    while True:
        print("\n===== Temperature Converter =====")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        print("4. Exit")

        try:
            choice = int(input("Choose input scale (1-4): "))

            if choice == 4:
                print("Thank you for using the converter 👋")
                break

            temp = float(input("Enter temperature value: "))

            if choice == 1:
                print(f"Fahrenheit: {celsius_to_fahrenheit(temp):.2f} °F")
                print(f"Kelvin: {celsius_to_kelvin(temp):.2f} K")

            elif choice == 2:
                print(f"Celsius: {fahrenheit_to_celsius(temp):.2f} °C")
                print(f"Kelvin: {fahrenheit_to_kelvin(temp):.2f} K")

            elif choice == 3:
                print(f"Celsius: {kelvin_to_celsius(temp):.2f} °C")
                print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.2f} °F")

            else:
                print("Invalid choice! Please select 1-4.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")


# Run program
convert_temperature()
