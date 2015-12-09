def big_prime(n):
	i = 2 
	
	while i * i <= n:
		if n % i :
			i = i + 1
		else :
			n = n / i
	return n

def main():
	print " the largest prime factor of the number 600851475143 : "
	print big_prime(600851475143)

if __name__ == '__main__':
	main()