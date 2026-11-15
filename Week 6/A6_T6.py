# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def collectRows() -> str:
    print("Collecting plain text rows for ciphering.")
    text = ""
    row = input("Insert row(empty stops): ")
    while row != "":
        text += row + "\n"
        row = input("Insert row(empty stops): ")
    return text


def cipherText(text: str) -> str:
    ciphered = ""
    for character in text:
        if character in LOWER_ALPHABETS:
            index = (LOWER_ALPHABETS.index(character) + 13) % 26
            ciphered += LOWER_ALPHABETS[index]
        elif character in UPPER_ALPHABETS:
            index = (UPPER_ALPHABETS.index(character) + 13) % 26
            ciphered += UPPER_ALPHABETS[index]
        else:
            ciphered += character
    return ciphered


def askChoice() -> str:
    print()
    print("Choose what to do with the ciphered text.")
    print("1 - Show the ciphered text")
    print("2 - Save the ciphered text")
    choice = input("Your choice: ")
    while choice != "1" and choice != "2":
        print("Invalid choice.")
        choice = input("Your choice: ")
    return choice


def showText(ciphered: str) -> None:
    print()
    print("#### Ciphered text ####")
    print(ciphered, end="")
    print()
    print("#### Ciphered text ####")


def saveText(ciphered: str) -> None:
    filename = input("Insert filename to save: ")
    file = open(filename, "w", encoding="UTF-8")
    file.write(ciphered)
    file.close()
    print("Ciphered text saved!")


def main() -> None:
    print("Program starting.")
    print()
    text = collectRows()
    ciphered = cipherText(text)
    choice = askChoice()
    if choice == "1":
        showText(ciphered)
    else:
        saveText(ciphered)
    print("Program ending.")


main()
