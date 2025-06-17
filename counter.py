# program to count the number of lines in this file
# opening a file
file = open("A1.txt", "r")
Counter = 0


# Reading from file
Content = file.read()
#Splitting content into lines
# and storing them in a list
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)