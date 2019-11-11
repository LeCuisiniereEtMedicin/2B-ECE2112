def getAvailableLetters(lettersGuessed):
    #MAKE A STRING OF THE ALPHABET
    allletters = 'abcdefghijklmnopqrstuvwxyz'
    #CONVERT FROM STRING TO LIST COZ IM LAZY TO TYPE
    allletters = list(allletters)
    #SERVES AS OUTPUT
    display = []
    #OUTPUT HAS NOW THE ALPHABET
    display.extend(allletters)
    #COMPARE EACH ELEMENT IF THERES A MATCH
    for i in range(len(lettersGuessed)):
        for j in range(len(allletters)):
            if allletters[j] == lettersGuessed[i]:
                #DELETES THE MATCHING LETTER FROM THE DISPLAY
                display.remove(lettersGuessed[i]) 
    return(''.join(display))