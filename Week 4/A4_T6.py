print("Program starting.")

number = int(input("Insert a positive integer: "))

text = str(number)
steps = 0

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    text += " -> " + str(number)
    steps += 1

print(text)
print(f"Sequence had {steps} total steps.")
print()
print("Program ending.")
