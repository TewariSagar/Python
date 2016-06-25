#we want to append the following text in the file newfile.txt
#Author - Sagar
#this method adds new data to the end of the file and doesnt overwrite the data as in the case of 'w'

newfile = open('newfile.txt','a')
newfile.write("\n\nAuthor - Sagar\n")
newfile.close()
