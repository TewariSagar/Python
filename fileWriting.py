#the 'w' atttribute is only for writing to a file but if the file doesnt exist it creates the file. If the file already exists it just overwrites it

#newfile.txt doesn't exist so this file will be created in the PWD
newfile = open("newfile.txt","w")

newfile.write("I like python\ndo you?\nthis is a bad way of writing\n")
#we need the close method for the file changes to be saved
newfile.close()

#append in the existing file to add some new lines of text

