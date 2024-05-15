#!/usr/bin/python3
def minimum_operations(n):
    list_of_factors = []
    while n > 1:
        for j in range(2, n + 1):
            if n % j == 0:
                list_of_factors.append(j)
                n = int(n / j)
                break
    return sum(list_of_factors)
