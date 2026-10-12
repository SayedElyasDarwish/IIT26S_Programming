def frameWord(PWord):
    print("*" * (len(PWord) + 4))
    print(f"* {PWord}*")
    print("*" * (len(PWord) + 4))
    return None

def main():
    print("program starting.")
    word= input("insert word: ")
    frameWord(word)
    print("Program ending.")
    return None


main()
