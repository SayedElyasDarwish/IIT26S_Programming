def main():
    print("Program starting.")
    Word = ""
    while True:
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            Word = input("Insert word: ")
        elif choice == "2":
            print('Current word - "' + Word + '"')
        elif choice == "3":
            print('Word reversed - "' + Word[::-1] + '"')
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print("Unknown option.")
        print()

    print("Program ending.")


if __name__ == "__main__":
    main()
    