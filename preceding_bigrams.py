import re
import sys

def getWords(subject):
    return re.sub(r"\W", " ", subject).split()

def isDigit(ch):
    return ch.isdigit()

def isIdChar(ch):
    return 'A' <= ch <= 'Z' or '0' <= ch <= '9'

def maybeAccountId(word):
    return 7 < len(word) < 15 and all(isIdChar(ch) for ch in word) and any(isDigit(ch) for ch in word)

def getPrefixBiGram(index, items):
    start = max(0, index - 2)
    return " ".join(items[start : index]).strip().lower()

def getPrefixBiGrams(needle, haystack):
    indices = [i for i, x in enumerate(haystack) if x == needle]
    return list(map(lambda i: getPrefixBiGram(i, haystack), indices))

def process(data):
    truth, threadSubject = data.split(",")

    words = getWords(threadSubject)
    candidates = set(filter(maybeAccountId, words))

    for item in candidates:
        for biGram in getPrefixBiGrams(item, words):
            print(f"{item == truth},{biGram}")


def main():
    filepath = sys.argv[1]
    with open(filepath) as fp:
        for line in fp:
            data = line.strip()
            if data:
                process(data)

if __name__ == '__main__':
    main()
