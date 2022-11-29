#https://www.codewars.com/kata/56a4872cbb65f3a610000026

def max_rot(n):
    num_as_list = [int(a) for a in str(n)]
    rotated_list = num_as_list
    
    max = int(''.join(str(num) for num in rotated_list))
    
    for i in range(0, len(num_as_list)):
        rotated_list = num_as_list[:i] + num_as_list[i+1:] + [num_as_list[i]]
        rotated_num = int(''.join(str(num) for num in rotated_list))
        if rotated_num > max:
            max = rotated_num
        num_as_list = rotated_list
        
    return max