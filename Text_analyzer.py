'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# | USER |   PASSWORD  |
# -----------------------
# | bob  |     123     |
# | ann  |    pass123  |
# | mike | password123 |
# | liz  |    pass123  |

separator = "-" *50
acces = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}

username = input("USERNAME: ")
password = input("PASSWORD: ")

if password != acces.get(username):
    print("unregistered user, terminating the program..")
    quit()
else:
    print(separator)
    print(f"Welcome to the app, {username}.")
    print("We have 3 texts to be analyzed")
    print(separator)

choice_text = int(input("Enter a number btw. 1 and 3 to select: "))

text = TEXTS[choice_text - 1]
print(separator)
print(f"YOUR CHOSEN TEXT: {text}")
print(separator)



words = list()
title_words = 0
upper_words = 0
lower_words = 0
numbers = 0
sum_numbers = []

for word in text.split():
    words.append(word.strip(".,:;"))

for categorize in words:
    if categorize.istitle():
        title_words += 1
    elif categorize.isupper():
        upper_words += 1
    elif categorize.islower():
        lower_words += 1
    else:
        categorize.isnumeric()
        sum_numbers.append(int(categorize))
        numbers += 1



print(f"There are {len(words)} words in the selected text.")
print(f"There are {(title_words)} titlecase words.")
print(f"There are {upper_words} uppercase words.")
print(f"There are {lower_words} lowercase words.")
print(f"There are {numbers} numeric strings.")
print(sum(sum_numbers))
print(separator)


length = dict()


for word_word in words:
    if len(word_word) not in length:
        length.setdefault(len(word_word), 1)
    else:
        length[len(word_word)] += 1

lengths = sorted(length.items())
title = "LEN|  OCCURRENCES  |NR"
# sep = "|"
print(title)
import pprint
for i, couple in lengths:
    graph = "*" * int(couple)
    print(f"{i:>3}| {graph:13} |{couple}",
          sep="\n"
          )
