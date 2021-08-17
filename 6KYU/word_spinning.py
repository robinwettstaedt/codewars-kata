"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
"""

def spin_words(sentence):
    list_of_words = sentence.split(" ")
    
    for index, word in enumerate(list_of_words): 
        if len(word) >= 5:
            list_of_words[index] = word[::-1]
            
    return " ".join(list_of_words)


    