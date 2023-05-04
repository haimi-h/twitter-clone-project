def approximate_e(n):
    factorial_number: int = 1
    Sum_of_factorials = 0
    for i in range(1, n + 1):
        factorial_number = factorial_number * i
        Sum_of_factorials += 1 / factorial_number
    print(Sum_of_factorials)


approximate_e(3)
print(approximate_e(3))