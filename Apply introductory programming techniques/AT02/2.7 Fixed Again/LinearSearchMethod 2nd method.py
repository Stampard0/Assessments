fruitlist = ["mango", "watermelon", "apple", "orange", "grape", "banana"]
def linear_search(search_term, index = -1): #this is defining the linear_search & what to search for
    for x in fruitlist: #for every element in 'fruitlist' array
        if(x == str(search_term)): #compare element value to search parameter
            print(search_term, fruitlist.index(search_term)) #using index() makes it return the index of what you search
        elif(x != str(search_term)): #this only will happen if the search_term is not in fruitlist
            print(search_term) #I am only making it print -1 just so it doesn't bring back a error

linear_search("watermelon")
linear_search("pineapple")
