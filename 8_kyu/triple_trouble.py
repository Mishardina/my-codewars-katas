#https://www.codewars.com/kata/5704aea738428f4d30000914

def triple_trouble(one, two, three):
    final_str = []
    for i in range(0, len(one)):
        final_str += one[i] + two[i] + three[i]
    return ''.join(final_str)