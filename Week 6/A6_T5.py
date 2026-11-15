SEPARATOR = ";"


def readValues(filename: str) -> str:
    values = ""
    file = open(filename, "r", encoding="UTF-8")
    row = file.readline()
    while row != "":
        row = row.strip()
        if row != "":
            if values != "":
                values += SEPARATOR
            values += row
        row = file.readline()
    file.close()
    return values


def analyseNumbers(values: str) -> str:
    count = 0
    total = 0
    greatest = 0
    if values != "":
        number_list = values.split(SEPARATOR)
        greatest = int(number_list[0])
        for item in number_list:
            number = int(item)
            count += 1
            total += number
            if number > greatest:
                greatest = number
    average = 0.0
    if count > 0:
        average = total / count
    results = "{}{}{}{}{}{}{:.2f}".format(count, SEPARATOR, total, SEPARATOR, greatest, SEPARATOR, average)
    return results


def displayResults(filename: str, results: str) -> None:
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print()
    print("#### Number analysis - END ####")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    results = analyseNumbers(values)
    displayResults(filename, results)
    print("Program ending.")


main()

