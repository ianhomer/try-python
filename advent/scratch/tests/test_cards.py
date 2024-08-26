from .. import Cards
import os


def test_cards():
    cards = Cards(os.path.dirname(__file__) + "/test_cards.txt")
    assert cards.count() == 5
    assert cards.total() == 6
