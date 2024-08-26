import re


def toInt(s: str):
    return int(s)


class Card:
    def __init__(self, line: str):
        self.__parse(line)

    def __parse(self, line: str):
        self.card = 0
        match = re.search("Card ([^:]*):([^|]*)\\|(.*)$", line)
        if match:
            self.number = int(match.group(1))
            self.winning = list(map(toInt, str(match.group(2)).split()))
            self.numbers = list(map(toInt, str(match.group(3)).split()))
        else:
            raise Exception(f"Card not valid {line}")

    def score(self):
        score = 0
        for winner in self.winning:
            if winner in self.numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        return score
