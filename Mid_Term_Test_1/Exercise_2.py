def sum_of_divisors(n):
  divisors_sum = 1
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      divisors_sum += i
  return divisors_sum

def amicable(n):
  order = 1
  amicable_string = str(n)
  aux = n
  test = False
  while not test and order <= 10:
    n = sum_of_divisors(n)
    test = aux == n
    if not test:
      order += 1
      amicable_string += " " + str(n)
  return amicable_string, order, test

def sociable(n):
  amicable_string, order, test = amicable(n)
  if test:
    print(n, "is a sociable number of order", order, ".")
    print("Amicable string =", amicable_string)
  else:
    print(n, "is not a sociable number")

sociable(12496)