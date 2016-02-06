from random import randint
from random import shuffle
import random

def main():
    print("This game gives you a scrambled word and you have to guess it right in one try!")
    print("If your guess is right, you get a point and you move on to next word, else you quit!")
    choice = input("Ready to play? Y/N: ")
    decision(choice)

def start_game():
    pts = 0
    game(pts)

def game(pts):
    word_list = ['Alphabet','Backpack','Barbecue','Cappuccino','Chocolates','Diamond','Electricity','Freeway','Gemstone','Hieroglyph','Kaleidoscope','Library','Microscope','Necklace','Pendulum','Pyramid','Restaurant','Satellite','Tapestry','Vacuum','Wheelchair']
    ran = randint(0,21)
    word = word_list[ran].lower()
    jumble(word)
    word1 = jumble(word)
    print("Here is your word!",word1)
    guess = input("Make a guess: ").lower()
    if guess == word:
        print("Wow! You're right!")
        pts+=1
        print("You scored {} points".format(pts))
        game(pts)
        
    else:
        print("That's not right! Better luck next time")
        choice = input("Do you want to play again? y/n: ")
        decision(choice)
            
def decision(choice):
    if choice == 'y' or choice == 'Y':
        start_game()
    elif choice == 'n' or choice == 'N':
        exit()
    else:
        print("Please type in your choice: ")

        
def jumble(word):
     l = list(word)
     random.shuffle(l)
     new = ''.join(l)
     
     return new


    
main()
        
    
