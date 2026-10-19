def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return -1

def main():
    print("Program starting.")
    count = 0
    choice = -1
    while choice != 0:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print("Current count -", count)
        elif choice == 2:
            count = count + 1
        elif choice == 3:
            count = 0
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
        print()
    print("Program ending.")
    return None

main()