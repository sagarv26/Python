# opens the file file.txt in read mode
fileptr = open("D:\\Learnings\\git.txt", "r")

if fileptr:
    print("file is opened successfully")

# stores all the data of the file into the variable content
content = fileptr.read();

# prints the type of the data stored in the file
print("Type of content of File")
print(type(content))

# prints the content of the file
print("Content: ")
print(content)
