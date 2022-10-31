def friend(x):
    friends = []
    for person in x:
        if len(person) == 4:
            friends.append(person)
    return friends