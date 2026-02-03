# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "./1_ps2/words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """

    if len(letters_guessed) == 0:
        return False
    if (len(secret_word)== 0):
        return True
    
    for char in secret_word:
        if char not in letters_guessed:
            return False
    
    return True
    


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    tmp = ""
    for char in secret_word:
        if char not in letters_guessed:
            tmp += "*"
        else:
            tmp += char
    return tmp


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letras = string.ascii_lowercase
    temp = ""
    for char in letras:
        if char not in letters_guessed:
            temp += char
    return temp



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to Hangman!")
    print(f"A palavra secreta tem {len(secret_word)} letras")
    number_guess = 10
    letters_guessed = []
    letras_validas = string.ascii_lowercase + "!"
    total_score = 0
    vowels = "aeiou"


    while number_guess > 0:
        print("--------------")
        print(f"Você tem {number_guess} tentativas sobrando")
        letras_disp = get_available_letters(letters_guessed)
        print(f"Letras disponíveis: {letras_disp}")
        guess = input("Por favor advinhe uma letra: ").lower()

        while guess not in letras_validas:
            print("Insira uma letra do alfabeto.")
            guess = input("Por favor advinhe uma letra que faça parte do alfabeto: ")

        if guess == "!" and with_help:
            if  number_guess < 3:
                print(f"A ajuda custa 3 pontos e você tem {number_guess} ponto(s) restantes.")
                continue
            guess = escolher_letra(secret_word, letras_disp)
            print(f"Letra revelada: {guess}")
            number_guess -= 3



        
        if guess in letters_guessed:
            print(f"A letra: {guess} já foi chutada: { get_word_progress(secret_word, letters_guessed)} ")
            continue
        else:
            if guess == "!":
                continue
            letters_guessed += guess

        if guess in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        elif guess in vowels:
            print(f"Não é a letra: { get_word_progress(secret_word, letters_guessed)} ")
            print(f"A letra ({guess}) é uma vogal. Perde 2 pontos")
            number_guess -=2
        else:
            print(f"Não é a letra: { get_word_progress(secret_word, letters_guessed)} ")
            print(f"A letra ({guess}) é uma consoante. Perde 1 ponto")
            number_guess -= 1

        if has_player_won(secret_word, letters_guessed):
            print(f"Parábens você ganhou em {10 - number_guess} tentativas")
            numero_letras_unicas = letras_unicas(secret_word)
            total_score = ((number_guess) + 4 * numero_letras_unicas) + (3*len(secret_word))
            print(numero_letras_unicas)
            print(f"Sua pontuação para esse jogo é: {total_score}")
            return
    print(f"Desculpe, você está sem tentativas. A palavra era: {secret_word} ")


def escolher_letra(secret_word, letras_disp):
    choose_from = ""
    for c in secret_word:
        if c in letras_disp:
            choose_from+= c

    new = random.randint(0, len(choose_from)-1)
    revelead_letter = choose_from[new]

    return revelead_letter

def letras_unicas(secret_word):
    count = 0
    temp = ""
    for c in secret_word:
        if c not in temp:
            count += 1
        temp += c
    return count


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    secret_word = "wildcard"
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

