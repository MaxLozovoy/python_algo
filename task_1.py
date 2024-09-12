"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time



n = 1000000



source_1 = list(range(1, n + 1))

# искомое значение
elem = 852500
dict_obj = {}
list_obj = []

def my_dict():

    keys = range(0, n)
    values = source_1
    for i in keys:
        dict_obj[i] = values[i]
    return dict_obj


def my_list(sourse_1):

    for i in source_1:
        list_obj.append(i)
    #list_obj = source_1 # при таком заполнеии списка, скорость даже при 10 млн ноль. такое возможно?
    return list_obj


# поиск элемента словаря по ключу 
# время выполнения этой функции всегда ноль
def search_in_dict():
    return dict_obj[elem]

"""
# поиск в словаре по значению
# эта функция медленнее поиска в списке
def search_in_dict():
    for key, value in dict_obj.items():
        if key == elem:
            return value
"""
"""
# поиск элемента по индексу
def search_in_list():
    return my_list(source_1)[elem]
"""
# поиск в списке по значению
def search_in_list():

    for i in list_obj:
        if i == elem:
            return i


# время заполнения словаря
start_time_my_dict = time.time()
my_dict()
result_speed_my_dict = time.time() - start_time_my_dict
print(f'Время заполнения словаря: {result_speed_my_dict}')

print()
# время заполнения списка
start_time_my_list = time.time()
my_list(source_1)
result_speed_my_list = time.time() - start_time_my_list
print(f'Время заполнения списка: {result_speed_my_list}')

print()
print('********************************************************')
print()

# время поиска по значению в словаре
start_time_search_in_dict = time.time()
search_in_dict()
result_search_in_dict = time.time() - start_time_search_in_dict
print(f'Время поиска значения по ключу в словаре: {result_search_in_dict}')

print()

# время поиска по значению в списке
start_time_search_in_list = time.time()
search_in_list()
result_search_in_list = time.time() - start_time_search_in_list
print(f'Время поиска значения в списке: {result_search_in_list}')

