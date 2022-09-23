import random
pokusy = 7

words = ["brouk", "lahev", "okurka", "stonožka", "prdel"]

r = random.randint(0, len(words) - 1)

chosen_word = words[r]

letters_list = []
pomlcka_list = []
for letter in chosen_word:
    letters_list.append(letter)

for letter in chosen_word:
    pomlcka_list.append(" _ ")

print(letters_list)

print("Welcome to HANGMAN")
lenght = len(chosen_word)
print(f"slovo které hádáte má {lenght} znaků")




while pokusy > 0 and " _ " in pomlcka_list:
    print(pomlcka_list)
    tip = input("tipněte písmeno: ")
    if tip in letters_list:
        print("ano je tam")
        count_index = 0
        for pismeno in letters_list:
            if pismeno == tip:
                pomlcka_list[count_index] = pismeno
                count_index += 1
            else:
                count_index += 1
    else:
        print("není tam")
        pokusy = pokusy - 1

if " _ " in pomlcka_list:
    print("je nám líto, jste looser...")
else:
    print(pomlcka_list)
    print("Gratulace")