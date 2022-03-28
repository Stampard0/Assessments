user_input = input("Please Tell me your body temperature: ")

if(float(user_input) <= 37):
    print("Below normal body temperature")
elif(float(user_input) > 37) and (float(user_input) <= 38):
    print("Normal body temperature")
elif(float(user_input) > 38) and (float(user_input) <= 39):
    print("Is a Fever")
elif(float(user_input) > 39) and (float(user_input) <= 40):
    print("Is a High Fever")
elif(float(user_input) > 40) and (float(user_input) <= 41):
    print("Is a Very High Fever")
else:
    print("Is a Serious Emergency")
