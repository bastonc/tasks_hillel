# https://www.codeabbey.com/index/task_view/card-names


def find_name(*args):
    result_list = []
    cards = [int(x) for x in args]
    suits = ('Clubs', 'Spades', 'Diamonds', 'Hearts')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
    for card in cards:
        suit_number = int(card / 13)
        suit = suits[suit_number]
        rank_number = card % 13
        rank = ranks[rank_number]
        result_list.append(f"{rank}-of-{suit}")
    return " ".join(result_list)


if __name__ == "__main__":
    assert(find_name(25, 32, 51, 20, 6) == "Ace-of-Spades 8-of-Diamonds Ace-of-Hearts 9-of-Spades 8-of-Clubs")
    print("Success")
