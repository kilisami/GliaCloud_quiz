def multiples_3_5(n):
	multi_three = []
	multi_five =[]
	multi_fifteen = []
	i = 3
	while i < n :
		multi_three.append(i)
		i = i + 3
	j = 5
	while j < n :
		multi_five.append(j)
		j = j + 5	
	k = 15
	while k < n :
		multi_fifteen.append(k)
		k = k + 15	
	print sum(multi_three) + sum(multi_five) - sum(multi_fifteen)


def main():
	multiples_3_5(1000)

if __name__ == '__main__':
	main()