#https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    friends = []
    for person in x:
        if len(person) == 4:
            friends.append(person)
    return friends