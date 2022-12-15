# Write here the code challenge solution
import re as r


def Repeated_Word(s:str) -> str:
    """
    This function receives a string as an input, and it returns the first 
    repated word in the string as output, otherwise it return None
    """

    s =  r.sub("\s+"," ", s)

    words = s.split(' ')
    seen = {}

    for word in words:
        if (seen.get(word) == None):
            seen[word] = 1
        else:
            return word
    
    return None

 
test1 = "ASAC                      is a       department          at LTUC. ASAC teaches programming in LTUC."
test2 = "I am learning programming at ASAC."

print(Repeated_Word(test1))
print(Repeated_Word(test2))