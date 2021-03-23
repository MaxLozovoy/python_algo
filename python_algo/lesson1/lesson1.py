def fibo_recur(number):
    if number <= 1:
        return number
    return fibo_recur(number - 2) + fibo_recur(number - 1)


print(fibo_recur(5))
