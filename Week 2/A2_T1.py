print("Program starting.")

Name = input("What is your name: ")
Feed = input("Enter a floating point number: ")
Number1 = float(Feed)
Feed = input("Enter second floating point number: ")
Number2 = float(Feed)

Product = round(Number1 * Number2, 2)

print(f"{Name} you gave numbers {Number1} and {Number2}")
print(f"Multiplying first and second number will result in product {Product}")

print("Program ending.")