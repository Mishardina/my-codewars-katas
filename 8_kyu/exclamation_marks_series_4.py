#https://www.codewars.com/kata/57faf12b21c84b5ba30001b0

def remove(s):
    return ''.join([symb for symb in s if symb != '!'] + ['!'])