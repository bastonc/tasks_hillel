from faker import Faker


def shuffle_words(amount: int) -> list:
    if amount < 1000:
        fake = Faker()
        words = [fake._unique_proxy.word() for _ in range(amount)]
        for word in words:
            yield word
    else:
        raise ValueError("Count must be < 10000")


if __name__ == "__main__":
    dataset = shuffle_words(900)
    for word in dataset:
        print(word)
