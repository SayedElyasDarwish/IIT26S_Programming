print("Program starting.")
print("Insert two integers.")
NumOne = int(input("Insert first integer: "))
NumTwo = int(input("Insert second integer: "))

print("Comparing inserted integers.")
if(NumOne == NumTwo):
    print("Integers are the same.")
elif(NumOne > NumTwo):
    print("First integer is greater.")
else:
    print("Second integer is greater.")

print()
print("Adding integers together")
Sum = NumOne + NumTwo
print(f"{NumOne} + {NumTwo} = {Sum}")

print()
print("Checking the parity of the sum...")
if(Sum % 2 == 0):
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")

    
    
    