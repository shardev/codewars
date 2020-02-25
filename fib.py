def fibonacci(n):
    fib = []
    fib.append(0)
    fib.append(1)

    if n > -1 and n < 2:
        return fib[n]

    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]

def productFib(prod):
    i = 2
    while(prod > fibonacci(i-1) * fibonacci(i-2)) : i += 1
    
    if fibonacci(i-1) * fibonacci(i-2) == prod: return [fibonacci(i-2), fibonacci(i-1), True]
    else: return [fibonacci(i-2), fibonacci(i-1), False]