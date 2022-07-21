user_input = input("Enter a phrase: \n") #prompts user for input #the \n means new line
print("Your phrase is: " + user_input) #this is an example of string #this also prints Your phrase is: + what the user put in
user_input = user_input.replace("agression", "aggression")
#^this is checking the spelling of the word put in then changing it to the correct spelling
user_input = user_input.replace("pixle", "pixel")
#^this is checking the spelling of the word put in then changing it to the correct spelling
user_input = user_input.replace("alot", "a lot")
#^this is checking the spelling of the word put in then changing it to the correct spelling
user_input = user_input.replace("adress", "address")
#^this is checking the spelling of the word put in then changing it to the correct spelling
print("The correct spelling is: " + user_input) #this prints the the corrected spelling of the phrase
