name = "Rahul Sharad Dravid"
DOB = "11-01-1973"
runs = 10889
matches = 344
innings = 318
notout = 40
balls = 15284

print("Name: ", name)
print("DOB", DOB)
print("#" * 25)
print("His ODI Details: ")
print("Matches: ", matches)
print("Innings: ", innings)
print("Runs :", runs)
print("Avg: ", runs / (innings - notout))
print("SR: ", (runs / balls) * 100)
print("#" * 25)
print()

# Print with Formatter
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your",
                       "Own text here",
                       "Maybe a poem",
                       "Or a song about fear"
                       ))
