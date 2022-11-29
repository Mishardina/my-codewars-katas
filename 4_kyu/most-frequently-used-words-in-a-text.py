#https://www.codewars.com/kata/51e056fe544cf36c410000fb

def top_3_words(text):
    print(text)
    text = text.lower()
    
    for i in range(len(text)):
        if not(text[i] >='a' and text[i] <= 'z' or text[i] == '\'' or text[i] == ' '):
            text = text[:i] + ' ' + text[i+1:]

    text = text.split()
    
    text = [word for word in text if list(set(word)) != ['\'']]    
    
    counts_dict = dict.fromkeys(set(text), 1)
    
    for word in text:
        counts_dict[word] += 1
        
    most_freq_words = []
    for i in range(len(counts_dict.keys())):
        if i > 2:
            break
        max = 0
        curr_key = None
        for key in counts_dict.keys():
            if counts_dict[key] > max:
                max = counts_dict[key]
                curr_key = key
        most_freq_words.append(curr_key)
        del counts_dict[curr_key]
                
    return most_freq_words