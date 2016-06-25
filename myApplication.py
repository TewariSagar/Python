#the module is imported without the .py extension
#no matter how many times we import the module,, it will be executed only once
#python looks for the module in the current directory and all directories in the python path variable (i haven't set the PYTHONPATH variable)

import customModule

print "This is the print statement inside my application"
#print global var of module and call the function

print customModule.my_var
customModule.myFunction()
