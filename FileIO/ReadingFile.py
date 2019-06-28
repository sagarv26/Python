# opens the file git.txt in read mode
filePtr = open("D:\\Learnings\\git.txt", "r")

if filePtr:
    print("file is opened successfully")

# stores all the data of the file into the variable content
content = filePtr.read();

# prints the type of the data stored in the file
print("Type of content of File")
print(type(content))

# prints the content of the file
print("Content: ")
print(content)


# running a for loop
filePtr = open("D:\\Learnings\\git.txt", "r")
print("Using For Loop: ")
for i in filePtr:
    print(i)  # i contains each line of the file
