print("Program starting.")

Word1 = input("Insert first word: ")
Word2 = input("Insert second word: ")

Length1 = len(Word1)
Length2 = len(Word2)
Compound = Word1 + Word2

print(f"1st word is {Length1} characters long.")
print(f"2nd word is {Length2} characters long.")
print(f"Words together makes one closed compound '{Compound}'.")

print("Program ending.")