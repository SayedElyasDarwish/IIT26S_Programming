print("Program starting.")

Feed = input("Insert fahrenheits: ")
Fahrenheit = float(Feed)

Celsius = round((Fahrenheit - 32) / 1.8, 1)

print(f"{Fahrenheit}°F is {Celsius}°C")

print("Program ending.")