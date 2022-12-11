#https://www.codewars.com/kata/58528e9e22555d8d33000163

def minutes_to_midnight(d):
    return str(1440 - (d.hour*60 + round((d.minute*60 + d.second)/ 60))) + " minutes"