filePtr = open("D:\\Test.txt", "a")

# appending the content to the file
filePtr.write("Python is the modern day language. It makes things so simple.\n")

# closing the opened file
filePtr.close()


# Read and Write into File
inputFile = open("D:\\Learnings\\git.txt", "r")
outputFile = open("D:\\Test.txt", "a")

content = inputFile.read();
outputFile.write(content)
