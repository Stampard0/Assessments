output_string = open("Python.txt", "w") #the w stands for write. using write over rights what was already there
output_string.write("""Python has been an important part of Google since the beginning, and remains so as the system grows and evolves.

"Today dozens of Google engineers use Python, and we're looking for more people with skills in this language." said Peter Norvig, director of search quality at Google, Inc.""")
output_string.close()#it is good practice to close the file

input_string = open("Python.txt", "r") #the r stands for read
print(input_string.read()) #this prints what it has read in the txt file
input_string.close() #it is good practice to close the file
