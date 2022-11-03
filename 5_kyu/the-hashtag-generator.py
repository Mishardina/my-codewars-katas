def generate_hashtag(s):
    if not s:
        return False
    
    clear_str = " ".join(s.split())
    clear_str = clear_str.split()
    for i in range(len(clear_str)):
        clear_str[i] = clear_str[i].capitalize()
    hashtag = '#' + ''.join([str(word) for word in clear_str])
    
    if len(hashtag) > 140:
        return False
    else:
        return hashtag