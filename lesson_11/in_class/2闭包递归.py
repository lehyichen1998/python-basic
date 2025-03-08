def factorial(num):
    if num == 1:
        return 1 * 1
    result = num * factorial(num - 1)
    return result


print(factorial(5))
