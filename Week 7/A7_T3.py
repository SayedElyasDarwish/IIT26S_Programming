WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")
print("Program starting.")
filename = input("Insert filename: ")
print(f'Reading file "{filename}".')
rows: list[str] = []
with open(filename, encoding="utf-8") as file:
    for line in file.readlines()[1:]:
        if line.strip() != "":
            rows.append(line.rstrip())
print("Analysing timestamps.")
print("Displaying results.")
print("### Timestamp analysis ###")
for day in WEEKDAYS:
    count = sum(1 for row in rows if row.startswith(day))
    print(f" - {day} {count} stamps")
print("### Timestamp analysis ###")
print("Program ending.")