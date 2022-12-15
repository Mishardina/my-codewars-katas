#https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

def fib(n):
    if n == 0:
        return 0
    if n < 0 and n%2 == 0:
        return -_fibonacci(-n)[0]
    if n > 0 or (n<0 and n%2 != 0):
        if n < 0:
            return _fibonacci(-n)[0]
        if n > 0:
            return _fibonacci(n)[0]

def _fibonacci(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fibonacci(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)