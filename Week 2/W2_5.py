print("Program starting.")
print()

Word = input("Insert a closed compound word: ")

Reversed = Word[::-1]
Length = len(Word)
LastChar = Word[-1]

print(f"The word you inserted is '{Word}' and in reverse it is '{Reversed}'.")
print(f"The inserted word length is {Length}")
print(f"Last character is '{LastChar}'")
print()

print("Take substring from the inserted word by inserting...")
Feed = input("1) Starting point: ")
Start = int(Feed)
Feed = input("2) Ending point: ")
End = int(Feed)
Feed = input("3) Step size: ")
Step = int(Feed)
print()

Sub = Word[Start:End:Step]
print(f"The word '{Word}' sliced to the defined substring is '{Sub}'.")
print("Program ending.")