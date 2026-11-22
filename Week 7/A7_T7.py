ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

filename = input("Insert config(filename): ")
rotors: list[str] = []
reflector = ""
with open(filename, encoding="utf-8") as file:
    for line in file:
        name, _, value = line.strip().partition(":")
        if name.startswith("Rotor"):
            rotors.append(value)
        elif name == "Reflector":
            reflector = value
input("Insert plugs (y/n)?: ")
print("No extra plugs inserted.")
print("Enigma initialized.")
while True:
    row = input("\nInsert row (empty stops): ")
    if row == "":
        break
    positions: list[int] = [0, 0, 0]
    converted = ""
    for char in row.upper():
        if char not in ABC:
            converted += char
            continue
        # rotate: rotor 1 every key, carry to the next rotor
        positions[0] += 1
        for i in range(3):
            if positions[i] == 26:
                positions[i] = 0
                if i < 2:
                    positions[i + 1] += 1
        letter = ABC.index(char)
        for i in range(3):
            letter = (rotors[i].index(ABC[(letter + positions[i]) % 26]) - positions[i]) % 26
        letter = ABC.index(reflector[letter])
        for i in (2, 1, 0):
            letter = (ABC.index(rotors[i][(letter + positions[i]) % 26]) - positions[i]) % 26
        print(f'Character "{char}" illuminated as "{ABC[letter]}"')
        converted += ABC[letter]
    print(f'Converted row - "{converted}".')
print("\nEnigma closing.")