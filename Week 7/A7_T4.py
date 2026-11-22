from dataclasses import dataclass


@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float


print("Program starting.")
filename = input("Insert filename: ")
print(f'Reading file "{filename}".')
timestamps: list[TIMESTAMP] = []
with open(filename, encoding="utf-8") as file:
    for line in file.readlines()[1:]:
        if line.strip() == "":
            continue
        c = line.rstrip().split(";")
        timestamps.append(TIMESTAMP(c[0], c[1], float(c[2]), float(c[3])))
print("Electricity usage:")
for t in timestamps:
    total = t.price * t.consumption
    print(f" - {t.weekday} {t.hour}, price {t.price:.2f}, consumption {t.consumption:.2f} kWh, total {total:.2f} €")
print("Program ending.")