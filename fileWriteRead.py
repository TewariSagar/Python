#this DOC contains the documentation to actually open a file, write to it and read it at the same place. This can be done using w+ attribute

newfile = open("newfile.txt", 'w+')
newfile.write("this is the data that was appended using the w+ attribte\n");
newfile.seek(0)
newfile.read()
newfile.close()
