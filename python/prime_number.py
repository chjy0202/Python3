def prime(n):
  primes = []
  a = [True] * (n - 1)
    
  for i in range(2, n + 1):
    if a[i - 2] == True:
      primes.append(i)
      for j in range(i * 2, n + 1, i):
        a[j - 2] = False
  return primes