from random import choice

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    joke = []  # создаем пустой список
    for _ in range(n):
        joke.append('{} {} {}'.format(choice(NOUNS), choice(ADVERBS), choice(ADJECTIVES)))  # форматируем строку с
        # помощью метода format и подставляем аргументы
    return joke


print(get_jokes(2))
