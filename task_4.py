"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""

"""
row = [1, -0.5, 0.25, -0.125]
n = int(input('Введите количество элементов:\n>>'))
print('Количество элементов: ', n, ', ', 'их сумма:', sum(row[:n]))
"""

def recur_method(i, numb, n_count, sum_elements):
    """Рекурсия"""
    if i == n_count:
        print(f"Количество элементов - {n_count}, их сумма - {sum_elements}")
    elif i < n_count:
        # i + 1 - это счетчик
        # numb / 2 * -1 - шаг последовательности
        # n_count - кол-во элементов которые надо сложить
        # sum_elements + numb - сумма элементов
        return recur_method(i + 1, numb / 2 * -1, n_count, sum_elements + numb)


n = int(input("Введите количество элементов:\n>> "))
# 1 по умолчанию начало последовательности
recur_method(0, 1, n, 0)
