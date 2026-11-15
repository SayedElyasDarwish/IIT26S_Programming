# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

SEPARATOR = ";"
PROGRESS_FILE = "player_progress.txt"
PROGRESS_HEADER = "current_location;next_location;passphrase"
START_ROW = "0;1;qvfpvcyvar"

PLACES = [
    "home",
    "Galba's palace",
    "Otho's palace",
    "Vitellius' palace",
    "Vespasian's palace",
]


def rot13(text: str) -> str:
    result = ""
    for character in text:
        if character in LOWER_ALPHABETS:
            result += LOWER_ALPHABETS[(LOWER_ALPHABETS.index(character) + 13) % 26]
        elif character in UPPER_ALPHABETS:
            result += UPPER_ALPHABETS[(UPPER_ALPHABETS.index(character) + 13) % 26]
        else:
            result += character
    return result


def readRows(filename: str) -> list:
    rows = []
    file = open(filename, "r", encoding="UTF-8")
    row = file.readline()
    while row != "":
        row = row.strip()
        if row != "":
            rows.append(row)
        row = file.readline()
    file.close()
    return rows


def writeRows(filename: str, rows: list) -> None:
    file = open(filename, "w", encoding="UTF-8")
    for row in rows:
        file.write(row + "\n")
    file.close()


def initProgress() -> None:
    try:
        file = open(PROGRESS_FILE, "r", encoding="UTF-8")
        file.close()
    except FileNotFoundError:
        writeRows(PROGRESS_FILE, [PROGRESS_HEADER, START_ROW])


def readLastProgress() -> str:
    rows = readRows(PROGRESS_FILE)
    return rows[-1]


def appendProgress(line: str) -> None:
    rows = readRows(PROGRESS_FILE)
    rows.append(line)
    writeRows(PROGRESS_FILE, rows)


def readMessage(filename: str) -> str:
    file = open(filename, "r", encoding="UTF-8")
    content = file.read()
    file.close()
    return content


def saveText(filename: str, text: str) -> None:
    file = open(filename, "w", encoding="UTF-8")
    file.write(text)
    file.close()


def travel() -> None:
    initProgress()
    progress = readLastProgress()
    parts = progress.split(SEPARATOR)
    current_id = int(parts[0])
    next_id = int(parts[1])
    ciphered_pass = parts[2]
    plain_pass = rot13(ciphered_pass)

    print(f"Currently at {PLACES[current_id]}.")
    print(f"Travelling to {PLACES[next_id]}...")
    print(f"...Arriving to the {PLACES[next_id]}.")
    print("Passing the guard at the entrance.")
    print(f'"{plain_pass.capitalize()}!"')
    print("Looking for the message in the palace...")

    ciphered_message = readMessage(f"{next_id}_{ciphered_pass}.gkg")
    first_line = ciphered_message.split("\n")[0]
    print("Ah, there it is! Seems cryptic.")

    appendProgress(first_line)
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    plain_message = rot13(ciphered_message)
    saveText(f"{next_id}-{plain_pass}.txt", plain_message)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")


def main() -> None:
    print("Travel starting.")
    travel()
    print("Travel ending.")


main()
