#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]