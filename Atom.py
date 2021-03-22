# goes through each number
# keeps re-evaluating the same fib() several times...not efficient


def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


print(fib(12))
