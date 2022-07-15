# list - упорядоченная изменяемая последовательность

some_lis: list = ['some str', 241, []]

# На русском правильно говорить - список.

# второй вариант - передать функции list в качестве аргумента любую последовательность
some_list0: list = list('some string')  # => ['s', 'o', 'm', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']

# Операции со списками
some_list1 = ['some str', 1111, 67.39]
some_list2 = ['other str', 2222, 34.943]

result1 = some_list1.append(some_list2)  # Добавляет аргумент в конец массива.

some_list1.extend(some_list2)  # Расширяет первый массив,
# Добавляя туда элементы массива переданного в качестве аргумента.
# При этом этот метод ничего не возвращает. Он всего лишь меняет текущий объект.
index = 2
new_element = 'new str'
some_list1.insert(index, new_element)  # Вставляет элемент(Второй аргумент) по индексу(Первый аргумент).
# При этом, все элементы смещаются в право.

some_list1.remove('new str')  # Удаляет первый попавшийся элемент со значением переданным в качестве аргумента

last_elem = some_list1.pop()  # Удаляет последний элемент последовательности, возвращая его.

some_list1.clear()  # Очищает список. Удаляет все элементы.


some_list1.sort(reverse=True)  # Сортирует список.
# Если передать параметр reverse=True - сортирует его в обратном порядке.

some_list1.sort(key=len)  # Сортирует список. по длине элементов

z = ['a', 'aaz', 'w', 'b', 'aaaaa']
z.sort()  # сортировка будет по символам юникода первым буквам потом вторым.

some_list1.reverse()  # Просто переворачивает список

# Копирование

x = [53, 68, ["А", "В", "С"]]

x1 = x  # присвоение еще одной ссылки
x2 = x[:]  # Копия (создается при срезе)

x2 = x[1:2:3]

x3 = x.copy()  # Копия (через метод copy())
# Копируются не объекты а ссылки на сами объекты
help([].copy)  # shallow(поверхостное)
shallow = [1, 2, 3, ['A', 'B']]
shallow_copy = shallow[:]  # shallow.copy()
shallow_copy[3].append('C')
# deepcopy
from copy import deepcopy
shallow = [1, 2, 3, ['A', 'B']]
shallow_copy = deepcopy(shallow)
shallow_copy[3].append('C')







