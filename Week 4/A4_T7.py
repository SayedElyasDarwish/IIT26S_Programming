print("Program starting.")
print()
print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    text = str(number)
    result = 1
    line = ""

    for digit in text:
        result = result * int(digit)
        if line == "":
            line = digit
        else:
            line = line + " * " + digit

    print(f"{line} = {result}")
    number = result
    steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")
