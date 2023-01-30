fruitlist = ["mango", "watermelon", "apple", "orange", "grape", "banana"]
def linear_search(search_term): #this is defining the linear_search & what to search for
    for x in fruitlist: #for every element in 'fruitlist' array
        if(x == str(search_term)): #compare element value to search parameter
            return True #return True because term has been found
    return False #if the for loop ends , return False

print(linear_search("watermelon"))
print(linear_search("pineapple"))
