#кеширование
def decorator(zamikanie):  
    cache = {}
    def func(n):
        def fibonacci(n):
            if n in cache:
                return cache[n]
            result = zamikanie(n)
            cache[n] = result
            print(cache)
            return result
        return fibonacci(n)
    return func

@decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(2))
print(fibonacci(n))
print()


#замыкание
def fib():
    a = 0
    b = 1
    def fibonacci():
        nonlocal a
        nonlocal b
        a,b=b,a+b
        return b
    return fibonacci

result=fib()
print(result())
print(result())
print(result())
print(result())
print(result())
print(result())
