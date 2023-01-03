import word
import stage_logos
import random
from colorama import Fore, Style
from yachalk import chalk

print(Fore.BLUE + Style.BRIGHT + stage_logos.logo)
print(chalk.bold("----------------------------welcome to hangman game ----------------------------"))
name = random.choice(word.word_list)
words = []
for letter in name:
    words.append("_")
game_is_on = True
life = 6

while game_is_on:
    p = ''
    guest = input(Fore.RED + Style.BRIGHT + "guess a  letter: ")
    if guest in words:
        print(Fore.YELLOW + "you already guessed this letter")
    elif guest in list(name):
        for i in range(len(list(name))):
            if list(name)[i] == guest:
                words[i] = guest
                for letter in words:
                    p += letter
                    if name == p:
                        print(Fore.GREEN + f'the word was \"{name}"\ and you got it correct')
                        game_is_on = False
                print(Fore.LIGHTWHITE_EX + p)

    else:
        life -= 1
        print(stage_logos.stages[life])
        print(
            Fore.LIGHTGREEN_EX + "you lost a life you have " + Fore.RED + f"{life} " + Fore.LIGHTGREEN_EX + "lifes lefts")
        if life == 0:
            print(f"the word was \"{name}\"")
            print(Fore.LIGHTGREEN_EX + "===================GAME OVER =================")
            game_is_on = False
