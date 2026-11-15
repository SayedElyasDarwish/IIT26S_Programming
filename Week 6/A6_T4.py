def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")

    print(f'Reading names from "{filename}".')
    names = ""
    file = open(filename, "r", encoding="UTF-8")
    row = file.readline()
    while row != "":
        row = row.strip()
        if row != "":
            if names != "":
                names += ";"
            names += row
        row = file.readline()
    file.close()

    print("Analysing names...")
    name_list = []
    if names != "":
        name_list = names.split(";")

    count = len(name_list)
    shortest = 0
    longest = 0
    average = 0.0
    if count > 0:
        shortest = len(name_list[0])
        longest = len(name_list[0])
        total = 0
        for name in name_list:
            length = len(name)
            total += length
            if length < shortest:
                shortest = length
            if length > longest:
                longest = length
        average = total / count

    report = "#### REPORT BEGIN ####\n"
    report += "Name count - {}\n".format(count)
    report += "Shortest name - {} chars\n".format(shortest)
    report += "Longest name - {} chars\n".format(longest)
    report += "Average name - {:.2f} chars\n".format(average)
    report += "#### REPORT END ####"

    print("Analysis complete!")
    print(report)
    print("Program ending.")


main()
