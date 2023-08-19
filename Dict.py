Books = {"C" : "Dennis Ritchie", "C++" : "Stroustrup", "Java" : "Gosling", "Python" : "Guido"}
print(type(Books)) #display datatype of all dict
print(type(Books["C"])) #display datatype of specific element

language = Books.keys()
print(language)               #display or sort the dict_keys
print(type(language))  

author = Books.values()
print(author)                 #display or sort the dict_values
print(type(author))     

