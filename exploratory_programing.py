import re # imports module that enables a function to utilize regex
source = open("textfile.txt")
readfile = source.read()
result = re.findall(r"\w*at\b", readfile)
def word_length(word):
    if len(word)>3:
        return True
    else:
        return False
def regex_filter(word):
    if type(word) != str:
        raise TypeError("The argument is not a string")
    final_result= filter(word_length, result)
    return final_result
regex_filter(readfile)
