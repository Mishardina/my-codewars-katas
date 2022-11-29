#https://www.codewars.com/kata/57a386117cb1f31890000039

def parse_float(string):
    try:
        val = float(string)
        return val
    except:
        return None