def main() -> None:
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = []
    while True:
        try:
            value = int(input("Insert positive integer(negative stops): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < 0:
            break
        numbers.append(value)

    print("Stopped collecting positive integers.")

    if len(numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, number in enumerate(numbers):
            print(f"- Index {index} => Ordinal {index + 1} => Integer {number}")

    print("Program ending.")


if __name__ == "__main__":
    main()