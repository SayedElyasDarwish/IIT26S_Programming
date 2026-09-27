print("Program starting.")
print("Estimate how many minutes you spent on programming...")
print()

T1 = int(input("A1_T1: "))
T2 = int(input("A1_T2: "))
T3 = int(input("A1_T3: "))
T4 = int(input("A1_T4: "))
T5 = int(input("A1_T5: "))
T6 = int(input("A1_T6: "))
T7 = int(input("A1_T7: "))

Sum = T1 + T2 + T3 + T4 + T5 + T6 + T7
Average = round(Sum / 7, 2)
AverageInt = round(Average)

print()
print(f"In total you spent {Sum} minutes on programming.")
print(f"Average per task was {Average} min and same rounded to the nearest integer {AverageInt} min.")
print()
print("Program ending.")