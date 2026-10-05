print("Program starting.")
print()

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
print()

ok = True

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    ok = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    ok = False

if ok:
    print("First loop - inspection with break:")
    text = ""
    for i in range(start, stop):
        if i == inspection:
            break
        text += str(i) + " "
    print(text.strip())

    print("Second loop - inspection with continue:")
    text = ""
    for i in range(start, stop):
        if i == inspection:
            continue
        text += str(i) + " "
    print(text.strip())
    print()

print("Program ending.")

