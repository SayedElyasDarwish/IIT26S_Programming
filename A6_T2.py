def writeFile(filename: str, content: str) -> None:
    filehandle = open(filename, 'w', encoding="UTF-8")
    filehandle.write(content)
    filehandle.close()
    return None

def main() -> None:
    print("Program starting.")
    FirstName = input("Insert first name: ")
    LastName = input("Insert last name: ")
    Content = "{}\n{}\n".format(FirstName, LastName)
    Filename = input("Insert filename: ")
    writeFile(Filename, Content)
    print("Program ending.")
    return None

main()


