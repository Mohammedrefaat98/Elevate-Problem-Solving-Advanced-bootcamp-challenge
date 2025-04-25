def isPrime(n : int):
  if(n<2): return False
  if(n%2==0): return (n == 2)
  squareroot= (int)(n ** 0.5)
  for i in range(3,squareroot+1,2):
    if(n % i == 0): return False
  return True

def allprimenumbers(n,m):
  for i in range(n+1,m):
    if(isPrime(i)):
      print(i)
      
allprimenumbers(1,1000000)