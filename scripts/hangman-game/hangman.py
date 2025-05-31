
import random, sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]
 
 
CATEGORY = 'Pokemon'

#WORDS = 'PIKACHU BULBASAUR IVYSAUR VENUSAUR CHARMANDER CHARMELEON CHARIZARD SQUIRTLE WARTORTLE BLASTOISE CATERPIE METAPOD BUTTERFREE WEEDLE KAKUNA BEEDRILL PIDGEY PIDGEOTTO PIDGEOT RATTATA TATICATE EKANS ARBOK RAICHU JIGGLYPUFF WIGGLYPUFF MEOWTH PSYDUCK MACHOP MACHAMP SLOWPOKE SLOWBRO ONIX MAGIKARP DITTO EEVEE SNORLAX ZAPDOS MEW MEWTWO LUGIA LUCARIO'.split()

fire_type = ['CHARMANDER', 'CHARIZARD', 'NINETAILS', 'ARCANINE', 'MAGMAR', 'FLAREON',]
water_type = ['SQUIRTLE', 'BLASTOISE', 'STARYU', 'KRABBY', 'HORSEA', 'STARMIE', 'GYARADOS']
electric_type = ['PIKACHU', 'JOLTEON', 'VOLTORB', 'ELECTRODE']
grass_type = ['BULBASAUR', 'IVYSAUR', 'VENUSAUR', 'LEAFEON']
legendary_type = ['ARTICUNO', 'ZAPDOS', 'MOLTRES', 'MEWTWO', 'LUGIA', 'MEW', 'ENTEI']              

pokemon_list = fire_type + water_type + electric_type + grass_type + legendary_type


def sub_cat(secretWord):
    if secretWord in fire_type:
        return 'Fire Type'
    elif secretWord in water_type:
        return 'Water Type'
    elif secretWord in electric_type:
        return 'Electric Type'
    elif secretWord in grass_type:
        return 'Grass Type'
    elif secretWord in legendary_type:
        return 'Legendary Type'
    else:
        return 'Unknown Type'

def main():
    print('Pokemon Hangman, by Jhonatan Martinez')
    missedLetters = []
    correctLetters = []
    secretWord = random.choice(pokemon_list) #The word that has to be guessed

    while True:
        drawHangman(missedLetters, correctLetters, secretWord)

        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters.append(guess) #adds the correct guess to correctLetters

            foundAllLetters = True
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    foundAllLetters = False
                    break

            if foundAllLetters:
                print('Yes! You have caught: ', secretWord)
                print('You have won!')
                play_again = input('Do you want to play again? (Y/N)').lower()
                if play_again == 'y':
                    main()
                    
                else:
                    return
                

        else:
            missedLetters.append(guess)

            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('The secret Pokemon has escaped!')
                print('The pokemon was "{}"'.format(secretWord))
                play_again = input('Do you want to play again? (Y/N)').lower()
                if play_again == 'y':
                    main()
    
                else:
                    return
            
def drawHangman(missedLetters, correctLetters, secretWord):

    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print('Hint:', sub_cat(secretWord))
    print()


    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    blanks=['_'] * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed): #This function makes sure the player entered a single letter they havent guessed before

    while True: #Keep asking until the player enters a valid letter
        print('Guess a letter.')
        guess=input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You tried that letter already.')
        elif not guess.isalpha():
            print('Enter LETTER! only.')
        else:
            return guess


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()



    
    
                    

    

            
