#https://www.codewars.com/kata/5a19226646d843de9000007d

def count_consonants(text):
    consonants = ("a", "e", "i", "o", "u")
    chars = ''.join(x for x in text if x.isalpha())
    chars = chars.lower()
    chars = set(chars)
    i = 0
    for char in chars:
        if char not in consonants:
            i += 1
    return i