#https://www.codewars.com/kata/5631ac5139795b281d00007d

import re

class WordDictionary:
    def __init__(self):
        self.words = set()

    def add_word(self, word):
        self.words.add(word)

    def search(self, word):
        PATTERN = re.compile(word)
        return any(PATTERN.fullmatch(word) for word in self.words)