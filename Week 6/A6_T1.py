def readFile(Filename: str) -> str:
    Filehandler = open(Filename, 'r', encoding="UTF-8")
    Content = ''
    Row = Filehandler.readline()
    while Row != '':
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content

def main ():
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename)
    print(f'#### START "{Filename}" ####')
    print(FileContent)
    print(f'#### END "{Filename}" ####')
    print("Program ending.")
    return None
main()

        