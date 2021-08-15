"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""

def getCount(s):
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") 
    