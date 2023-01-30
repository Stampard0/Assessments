fruitlist = ["mango", "watermelon", "apple", "orange", "grape", "banana"]
def linear_search(search_term, index = -1): #this is defining the linear_search with a search_term & a default index
    #(Setting a default parrameter makes it not return a error)
    for x in fruitlist: #for every element in 'fruitlist' array
        if(x == str(search_term)): #compare element value to search parameter
            return (search_term, fruitlist.index(search_term)) #using index() makes it return the index of what you search.

print(linear_search("watermelon"))
print(linear_search("pineapple"))
