import random
import os


def getData(filepath):
    words = []
    with open (filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = getData(filepath="./files/data.txt")
    word = random.choice(data)
    word_list = [letter for letter in word]
    word_set = set(word_list)
    hits = []
    while(True):
        os.system("clear")
        print("ADIVINA LA PALABRA")

        #printing the current state of word
        for letter in word_list:
            #print (letter)
            if letter in hits:
                print(letter + " ", end="")
            else:
                print("- ", end="")
        print()
        #Inputing the shot
        shot = input("Ingresa una letra: ").strip().upper()
        assert shot.isalpha(), "Solo puedes ingresar letras"

        if shot in word_list and shot not in hits:
            hits.append(shot)

        #Ending the game winning or "." character
        if len(hits) == len(word_set):
            print("GANASTE!!")
            break
        

if __name__ == '__main__':
    run()