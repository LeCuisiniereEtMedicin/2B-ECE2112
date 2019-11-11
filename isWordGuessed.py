def isWordGuessed(secretWord, lettersGuessed):
    secretWord = secretWord.lower()
    secretWord = list(secretWord) 
    secretWord.sort()
    lettersGuessed.sort()
    secretWord = list(dict.fromkeys(secretWord))
    lettersGuessed = list(dict.fromkeys(lettersGuessed))
    if secretWord == lettersGuessed:
        return 1
    else:
        return 0