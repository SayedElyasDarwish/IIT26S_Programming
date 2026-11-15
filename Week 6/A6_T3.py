print("Program starting.")
print("This program can copy a file.")
source = input("Insert source filename: ")
destination = input("Insert destination filename: ")

print(f"Reading file '{source}' content.")
file = open(source, 'r', encoding="UTF-8")
content = ''
row = file.readline()
while row != '':
    content += row
    row = file.readline()
file.close()
print("File content ready in memory.")

print(f"Writing content into file '{destination}'.")
file = open(destination, 'w', encoding="UTF-8")
file.write(content)
file.close()

print("Copying operation complete.")
print("Program ending.")