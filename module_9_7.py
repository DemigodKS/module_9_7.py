def is_prime(func):
    def simple(*args):
        k = 0
        result = func(*args)
        for i in range(2, result // 2):
            if  result % i == 0:
                k = k + 1
        if k <= 0:
            return (f"{result} - Простое")
        else:
            return (f"{result} - Составное")
        #return result
    return simple


@is_prime
def sum_three(*args):
    summ = 0
    for i in args:
        summ += i
    return summ

result = sum_three(1, 5, 9)
result2 = sum_three(1, 5, 5)

print(result)
print(result2)





