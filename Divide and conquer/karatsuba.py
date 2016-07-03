"""
Karatsuba Multiplication
x.y = (10^n * ac + 10^n/2 (ad+bc) + bd)
"""
def karatsuba(x,y):

	n1 = len(str(x))
	n2 = len(str(y))

	if n1 <= 1 or  n2 <=1: 		#Base case
		return x * y

	n = max(n1,n2)
	div = int(n/2)
	
	a = (x / (10 ** div))
	c = (y / (10 ** div))
	b = (x % (10 ** div))
	d = (y % (10 ** div))

	return (karatsuba(a,c) * (10 ** n) + ((10 ** div) * (karatsuba(a+b,c+d) -a*c -b*d )) + karatsuba(b,d)) 


if __name__ == '__main__':

	x,y = map(int, raw_input().split())
	print (karatsuba(x,y))
