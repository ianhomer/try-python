from .. import Card


def test_zero_points():
    card = Card("Card 1 : 1 2 | 3 4")
    assert card.number == 1
    assert card.score() == 0


def test_1_pointer():
    card = Card("Card 2 : 1 2 | 1 4")
    assert card.number == 2
    assert card.winning == [1, 2]
    assert card.numbers == [1, 4]
    assert card.score() == 1
