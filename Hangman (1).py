#Hangman Game
from hangman_words import word_list
import random
import hangman_art
print(hangman_art.logo)

choosen_word = random.choice(word_list)
#print(choosen_word)

word_length = len(choosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

lives = 6

while not end_of_game:
#Guess a letter and assign the answer to a variable to variable
  guess = input("Guess a letter : ").lower()

  #Check if entered letter is already guessed
  if guess in display:
     print(f"You've already guessed {guess}")

  
#Check if the letter guessed is in the choosen_word
  for position in range(0,word_length):
    letter = choosen_word[position]
    if letter == guess:
        display[position] = letter
  #print(display)

  if guess not in choosen_word:
    lives -= 1
    print(f"You've guessed a wrong letter and you lose a life")
    print(f"You have {lives} remaining")
    from hangman_art import stages
    print(stages[lives])
    if lives == 0:
       end_of_game = True
       print("You Lose.")
       print(f"The answer was {choosen_word}")

  #Join all the elements in the list and turn it into a string
  print(f"{' '.join(display)}")

  #Check if the user has got all the letters
  if "_" not in display:
      end_of_game = True
      print("You Win.")