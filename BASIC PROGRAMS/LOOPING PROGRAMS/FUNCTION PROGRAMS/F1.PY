# PROGRAM TO CHECK THE NUMBER IS PREFECT SQR OR NOT
def solve(n):
   if n == 0 or n == 1:
      return True
   start = 2
   stop = n // 2
   while start <= stop:
      temp = range(start, stop + 1)

   k = temp[len(temp) // 2]
   k_squared = k * k 

   if k_squared == n:
      return True

   if k_squared > n:
      start = temp[0]
      stop = k - 1
   else:
      start = k + 1
      stop = temp[-1]

   return False

n = 121
print(solve(n))