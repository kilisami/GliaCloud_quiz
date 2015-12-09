def comb(n, r):
  stack = []
  stack.append((n, r))
  combinations = 0

  while len(stack):
    n, r = stack.pop()
    if r == 0:
      combinations += 1
    elif n < r:
      combinations += 0 #or just replace this line with `pass`
    else:
      stack.append((n-1, r))
      stack.append((n-1, r-1))

  return combinations  

def main():
  
    print "C(40,10) :" 
    print comb(40 , 10)
    print "C(990,33) :"
    print comb(990 , 33) 


if __name__ == '__main__':
  main()