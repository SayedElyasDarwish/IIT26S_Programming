def main() -> None:
    print("Program starting.")
    text: str = input("Insert comma separated integers: ")
    parts: list[str] = text.split(",")
    numbers: list[int] = []

    for part in parts:
        try:
            numbers.append(int(part.strip()))
        except ValueError:
            print(f"Invalid value: {part.strip()}")

    if len(numbers) == 0:
        print("No integers to analyze.")
    else:
        total: int = sum(numbers)
        parity: str = "even" if total % 2 == 0 else "odd"
        print(f"There are {len(numbers)} integers in the list.")
        print(f"Sum of the integers is {total} and it's {parity}")

    print("Program ending.")


if __name__ == "__main__":
    main()