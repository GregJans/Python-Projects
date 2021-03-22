# goes through each number
# keeps re-evaluating the same fib() several times...not efficient


def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


print(fib(12))


# tries to solve past problems by storing known fib()...makes it more efficient
# recursive approach
def mfib(n, memo):
    if memo[n] != null:  # not sure if pyton has null
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = mfib(n-1) + mfib(n-2)
        memo[n] = result
    return result


# will not actually work without memo...not sure how it works
print(mfib(5))


# NOTE: look up Bitwise opperators           https://www.geeksforgeeks.org/basic-operators-python/
