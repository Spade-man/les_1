import time
import os
import psutil

# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
def timer_decorator(f):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        f(*args, **kwargs)
        time_finish = time.time()

        print(f'Время исполнения функции {f.__name__}: {time_finish - time_start} сек.') #повзаимствоал такой вывод.  @ красиво!)
    return wrapper


# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
def memory_decorator(f):
    def wrapper_mem(*args, **kwargs):
        proc1 = psutil.Process(os.getpid()).memory_info().rss
        f(*args, **kwargs)
        proc2 = psutil.Process(os.getpid()).memory_info().rss

        print(f'Задействованный объем оперативной памяти для функции: '
              f'{(proc2 - proc1)/1000}  кБ ')
    return wrapper_mem


# 2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
# 4. Сравнить Задействованный объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.
@memory_decorator
@timer_decorator
def nat_list():
    return [i for i in range(1, 10000001)]

@memory_decorator
@timer_decorator
def nat_gen():
    for j in range(1, 10000001):
        yield j


nat_gen()
nat_list()

