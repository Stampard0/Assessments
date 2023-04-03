fruitlist = ["mango", "watermelon", "apple", "orange", "grape", "banana"]
def linear_search(search_term): #this is defining the linear_search & what to search for
    for x in fruitlist: #for every element in 'fruitlist' array
        if(x == str(search_term)): #compare element value to search parameter
            f = fruitlist.index(search_term) #using index() makes it return the index of what you search.
            return print(str(search_term), f)
        elif(x != str(search_term)): #this only will happen if the search_term is not in fruitlist
            print(str(search_term), -1) #I am only making it print -1 just so it doesn't bring back a error

linear_search("watermelon")
linear_search("pineapple")
