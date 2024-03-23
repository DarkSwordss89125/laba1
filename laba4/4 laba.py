#кеширование
def decorator(zamikanie):
    cache = {}
    def func(n):
        def fibonacci(n):
            if n in cache:
                return cache[n]
            result = zamikanie(n)
            cache[n] = result
            return result
        return fibonacci(n)
    return func

@decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(fibonacci(n))


#замыкание
def decorator(zamikanie):
    def func(n):
        def fibonacci(n):
            return zamikanie(n)
        return fibonacci(n)
    return func

@decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(fibonacci(n))
