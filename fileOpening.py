#file opening and file reading is covered in this document
#creating a txt file and reading it.
#there are certain modes => r for reading, w for writing, a for appending at the end of the file
#by default python opens the file for reading

myFile = open("sample.txt", "r")


#mode() funtion is used to know the attribute of the file handling
print myFile.mode

#we can read the entire file as a single string separated by \
print myFile.read()

#after we read the entire file the curson is at the end of the file but now if we want to open first five characters of the file

myFile.seek(0)
print myFile.read(5)

#read the file line by line

print myFile.readline()
myFile.seek(0)

#readlines returns a list of lines in the file

print myFile.readlines()

