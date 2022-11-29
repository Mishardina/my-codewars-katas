#https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    hex_r = "0x{:02x}".format(0 if r < 0 else 255 if r > 255 else r)[2:].upper()
    hex_g = "0x{:02x}".format(0 if g < 0 else 255 if g > 255 else g)[2:].upper()
    hex_b = "0x{:02x}".format(0 if b < 0 else 255 if b > 255 else b)[2:].upper()
    
    return hex_r + hex_g + hex_b