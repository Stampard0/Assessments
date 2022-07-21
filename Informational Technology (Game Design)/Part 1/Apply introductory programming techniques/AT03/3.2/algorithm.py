def linear_search(search_term, operator): #this is defining the linear_search with a search_term
    for x in operator: #for every element in 'operater' array
        if(x == str(search_term)): #compare element value to search parameter
            return(operator.index(search_term)) #using index() makes it return the index of what you search
    return -1
while(True):
    operater = ("Windows 10", "Linux Mint", "Mac OS 11", "Android Oreo", "Android Pie", "Android 11", "iOS 14")
    print(type(operater)) #this prints the type of data structure being used
    user_input = input("Enter a Operating System: \n") #this is getting an input from the user
    print(linear_search(user_input, operater))
