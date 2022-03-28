user_input = input("Please Tell me your body temperature: ")#this is asking for the user to give an input

if(float(user_input) <= 37): #this is the start of the if loop & is checking is the user_input is below or = 37
    print("Below normal body temperature")
elif(float(user_input) > 37) and (float(user_input) <= 38): #this is the continuation of the if loop.
    #It is checking if the user_input is more then 37 & below or = 38
    print("Normal body temperature")
elif(float(user_input) > 38) and (float(user_input) <= 39): #this checks if the user_input is more then 38 & below or = 39
    print("Is a Fever")
elif(float(user_input) > 39) and (float(user_input) <= 40): #this checks if the user_input is more then 39 & below or = 40
    print("Is a High Fever")
elif(float(user_input) > 40) and (float(user_input) <= 41): #this checks if the user_input is more then 40 & below or = 41
    print("Is a Very High Fever")
else: #this is the else statment which exicutes if all the if or elif statments come back as false.
    print("Is a Serious Emergency")
