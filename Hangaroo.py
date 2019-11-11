def Hangaroo():
    #Intro to the game
    print("WELCOME TO HANGAROO!!!")
    print()
    secretWord = []
    #This is the string of all available letters converted to string
    alphab = 'abcdefghijklmnopqrstuvwxyz'
    alphab = list(alphab)
    #terminator for later
    null = []
    print("Enter a WORD to be guessed by your friend: ")
    while secretWord == null:
        #let the player input a word to be guessed
        secretWord = input(" ")
        print()
        secretWord = secretWord.lower()
        #Convert string to list
        secretWord = list(secretWord)
        #repeat input if non alphabet
        for i in range(len(secretWord)):
            if secretWord[i] not in alphab:
                secretWord = []
                break
        if secretWord == null:
            print("Enter alphabet characters only: ")
            continue
    print()
    print("LET'S START THE GAME!")
    print("YOU HAVE 8 LIVES")
    #Empty list of available letters
    availableL = []
    #Fill availableL with the alphabet
    availableL.extend(alphab)
    #Empty list of guessed letters
    guessedL = []
    #Empty list of answer
    answer = []
    #Fill answer with the secretWord
    answer.extend(secretWord)
    #Change all letters to underscores
    for l in range(len(answer)):
        answer[l] = '_'
    #Lives counter
    life = 8
    #Terminator if code answer is complete
    counter = 0
    #Everything works as long as player has lives
    while life > 0 and counter < len(answer):
        #Input of Guesses
        guess = input("Guess a LETTER: ")
        #Change input cases to lowercase to match everything
        guess = guess.lower()
        
        #In case more than 1 input
        if len(guess) != 1:
            print("Enter one LETTER: ")
            continue
        #In case of repeated stuff
        if guess in guessedL and guess not in availableL:
            print("You already entered this letter, enter another: ")
            continue
        #In case of non alphabet stuff
        if guess not in alphab:
            print("Do not enter a non-alphabet character! Enter again: ")
            continue
        #start to compare
        for i in range(len(secretWord)):
            if secretWord[i] == guess:
                counter = counter + 1
                answer[i] = guess
        #Print the output
        print()
        print(' '.join(answer))
        print()
        #Subtract life if wrong answer
        if guess not in answer:
            life = life - 1
            print("Oh no, there's no ",guess," in the word")
        #We subtract guess from the available letters
        for i in range(len(alphab)):
            if alphab[i] == guess:
                availableL.remove(guess)
        #Add guessed letters to guessedL
        guessedL.extend(guess)
        
        if counter == len(answer):
            print("YOU GUESSED THE WORD!!! HANGAROO LIVES!!!")
            break
        #status update
        print("So far, ")
        print("You still have ",life," live/s")
        print("You still have the following letters available: ")
        print()
        print(' '.join(availableL))
        print()
        print("You have guessed the following letters already: ")
        print()
        print(' '.join(guessedL))
    print()
    if life == 0:
        print("YOU KILLED HANGAROO! Try again next time")
        
            
                
    
    