from dataclasses import dataclass

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")


@dataclass
class TIMESTAMP:
    weekday: str
    consumption: float
    price: float


@dataclass
class DAY_USAGE:
    weekday: str
    usage: float = 0.0
    cost: float = 0.0


print("Program starting.")
filename = input("Insert filename: ")
print(f'Reading file "{filename}".')
timestamps: list[TIMESTAMP] = []
with open(filename, encoding="utf-8") as file:
    for line in file.readlines()[1:]:
        if line.strip() == "":
            continue
        c = line.rstrip().split(";")
        timestamps.append(TIMESTAMP(c[0], float(c[2]), float(c[3])))
print("Analysing timestamps.")
days: list[DAY_USAGE] = [DAY_USAGE(name) for name in WEEKDAYS]
for t in timestamps:
    for day in days:
        if t.weekday == day.weekday:
            day.usage += t.consumption
            day.cost += t.consumption * t.price
print("Displaying results.")
print("### Electricity consumption summary ###")
for day in days:
    print(f" - {day.weekday} usage {day.usage:.2f} kWh, cost {day.cost:.2f} €")
print("### Electricity consumption summary ###")
print("Program ending.")