# radint = radnom integer which is to get integer from the input
import random

number = random.randint(1, 10)
print(number)

# shuffle is to shuffle the listing 
import random

cards = ["jack", "King", "Queen"]
random.shuffle(cards)
for card in cards:
    print(card)