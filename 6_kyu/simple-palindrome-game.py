#https://www.codewars.com/kata/5a26af968882f3523100003d

def solve(str1, str2):
    return 2 - any(str1.count(c) > 1 and c not in str2 for c in str1)