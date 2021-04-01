# функция для подсчета суммы

def my_sum(arr):

    x = 0
    for i in arr:
        x += i
    return x


print(my_sum([1, 2, 3]))

# функция для подсчета суммы с рекурсией

def my_sum_rec(arr):
    if not arr:
        return 0
    else:
        return arr[0] + my_sum(arr[1:])

print(my_sum_rec([1, 2, 3]))

# функция поиска максимального элемента
def max_numb(arr):

    max_num = 0
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num

print(max_numb([1, 2, 3, 4, 6, 7, 99, 88, 999]))

