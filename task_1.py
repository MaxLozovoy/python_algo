"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if not el % 2]



nums = [1, 2, 3, 4, 5]

print(func_1(nums))
print(func_2(nums))
time_1 = timeit("func_1(nums)", globals=globals(), number=100000)
print(f'Время выполенения func_1: {time_1}')

time_2 = timeit("func_2(nums)", globals=globals(), number=100000)
print(f'Время выполенения func_1: {time_2}')


#timeit("func_1(nums_arr)", "from __main__ import func_1, nums_arr", number=1000)