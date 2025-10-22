import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        el_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнена за {el_time:.4f} секунд")
        return result
    return wrapper

@timing_decorator
def example_function():
    time.sleep(2)
    print("Функция выполнена")

example_function()