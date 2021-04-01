"""
бинарный поиск в отсортированном списке
"""

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]


print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

"""
Упражнение 1.1
для отсортированного списка из 128 имен максимальное кол-во проверок 7

Упражнение 1.2
если список увеличивается вдвое - 8 проверок
"""