def getGuessedWord (secretWord, lettersGuessed):
    #TRANSLATE FROM STRING TO LIST
    secretWord = list(secretWord)
    lettersGuessed = list(dict.fromkeys(lettersGuessed))
    #THIS LIST WILL SERVE AS OUTPUT
    display = []
    #WE MAKING IT SAME SIZE WITH SECRETWORD
    display.extend(secretWord)
    #WE CHANGING EACH ELEMENT TO '_' 
    for l in range(len(display)):
        display[l] = '_'
    #WE NOW COMPARE LETTERS
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if lettersGuessed[i] == secretWord[j]:
                display[j] = lettersGuessed[i]
                #IF LETTERGUESSED IS SAME WITH SECRETWORD
                #WE GONNA CHANGE THE '_' BACK TO THE ORIGINAL LETTER
    #THE MAIN OUTPUT FROM LIST TO STRING    
    return(' '.join(display))
    
    
   