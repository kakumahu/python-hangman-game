from random import choice # allows me to randomly import files
from string import ascii_uppercase

words = ["coding","stacktrek","list","loops","tuple","co-op"]

print("Welcome to Hangman!")
print("Try and guess the word by providing letters")

#find a way to filter out the words that python cant understand (those that have spaces and -)
def get_valid_word(words):
    word = choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word: #if there is a word that contains these
        word = choice(words) #it will continue choosing a word until it doesnt

    return word.upper() # returns the random word to the function
# now that we have a way to get words
# we need a way to keep track of the letters

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(ascii_uppercase)
    used_letters = set()  #letters that have been used are stored here

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0: #while the
        # we need to see what letters are used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: #if the guessed letter is in the alphabet that you havent used
            used_letters.add(user_letter) # gets added to used letter set
            if user_letter in word_letters: # if the guessed letter is in the word
                word_letters.remove(user_letter) #it gets removed
                print('')

            else:
                lives -= 1  # takes away a life if wrongp
                print('Your letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters: #checks if the letter is alread in used letters
            print('You have already used that letter. Guess another letter.')

        else:
            print('That is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print(f'YAY! You guessed the word {word} !!') #another way of writing this 

   # def countdown():
    #  t = 5
    #  while t:
     #     mins, secs = divmod(t, 5)
    #      timeformat = '{:02d}:{:02d}'.format(mins, secs)
   #       print(timeformat, end='\r')
  #        time.sleep(1)
 #         t -= 1
#      print('You ran out of time! Get Hanged!')

    
#

if __name__ == '__main__':
    hangman()