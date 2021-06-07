# take a string and decrease all costs in the string by 15%

import re

PRICE_VALUE_PAT = re.compile('^[0-9]+(\.[0-9]+)?$')
CURRENCY_SYMBOLS = {'$', 'Rs'}

def is_numeric(word):
    return bool(PRICE_VALUE_PAT.match(word))


def process(word, price_changer):
    for s in CURRENCY_SYMBOLS:
        if word.startswith(s):
            value = word.removeprefix(s)
            if is_numeric(value):
                price = round(price_changer(float(value)), 2)
                return f"{s}{price}"

    return word


def alter_prices(sentence, price_changer):
    words = map(lambda w: process(w, price_changer), sentence.split())
    return ' '.join(words)



sentence = "I spent $52.50 on $.Amazon this week 13.7"
print(alter_prices(sentence, lambda x: 0.85 * x))
# I spent $44.62 on $.Amazon this week 13.7
