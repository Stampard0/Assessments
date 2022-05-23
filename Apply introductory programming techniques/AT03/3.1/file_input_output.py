f = open("Python.txt", "w") #the w stands for write. using write over rights what was already there
f.write("""Python has been an important part of Google since the beginning, and remains so as the system grows and evolves.

"Today dozens of Google engineers use Python, and we're looking for more people with skills in this language." said Peter Norvig, director of search quality at Google, Inc.""")
f.close()#it is good practice to close the file

f = open("Python.txt", "r") #the r stands for read
print(f.read()) #this prints what it has read in the txt file
f.close() #it is good practice to close the file
