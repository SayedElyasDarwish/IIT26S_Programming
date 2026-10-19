DELIMITER = ","

def collectWords():
    words = ""
    word = input("Insert word(empty stops): ")
    while word != "":
        words = words + word + DELIMITER
        word = input("Insert word(empty stops): ")
    return words

def analyseWords(words):
    wordList = words.split(DELIMITER)
    wordList.pop()
    count = len(wordList)
    chars = 0
    for word in wordList:
        chars = chars + len(word)
    if count > 0:
        Avg = chars / count
    else:
        Avg = 0
    print("- {} Words".format(count))
    print("- {} Characters".format(chars))
    print("- {:.2f} Average word length".format(Avg))

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main()