from advent.scratch.cards import Cards
import os

print("hello")

cards = Cards(os.path.dirname(__file__) + "/advent/scratch/cards.txt")
print(f"You scored {cards.total()}")
