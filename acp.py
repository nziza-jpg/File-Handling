# Open the file in write mode
file_write = open('john_banda.txt', 'w')

# Write the introduction
file_write.write("Name: John Banda\n")
file_write.write("Class: 8\n")
file_write.write("Favorite Subject: English\n")  

file_write.close()

#append
file_append = open('john_banda.txt', 'a')
file_append.write("Least Favourite Subject: Math\n")
file_append.close()
