import re # imports module that enables a function to utilize regex
source = open("textfile.txt") # opens text document that from its saved location
readfile = source.read() #enables program/code to read the text file
result = re.findall(r"\w*at\b", readfile) #uses regex to find all words that end with at
#Below is a function that determines if a string variable has more than 3 letters
def word_length(word):
    if len(word)>3:
        return True
    else:
        return False
def regex_filter(word):
    if type(word) != str:
        raise TypeError("The argument is not a string") #returns a type error if variable is not a string
    final_result= filter(word_length, result) #uses word_length function to filter the regex function so as to enable only the words with more than 3 letters to be returned
    return final_result
regex_filter(readfile)
