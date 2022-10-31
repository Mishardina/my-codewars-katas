from itertools import permutations

def get_words(hash_of_letters):
    letters_list = []
    for key in hash_of_letters.keys():
        letters_list.extend(hash_of_letters[key]*key)
    print(letters_list)
    
    perms = list(set(permutations(letters_list)))
    print(perms)
    final_perms = []
    for elem in perms:
        final_perms.append(''.join(elem))        
    print(final_perms)
    return sorted(final_perms)