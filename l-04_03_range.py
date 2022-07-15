# функция range - позволяет генерировать последовательности.
# При этом, она ленива. Она вычисляет последовательность только когда ее используют.

start: int = 0
stop: int = 10
step: int = 2

# пример:
some_range: range = range(10)  # генерирует последовательность из 10 чисел, начиная с 0, до 9 и с шагом 1

# Т.к тип range ленив, Что бы сгенерировать последовательность, например, можно воспользоваться преобразовнием типов
some_range: tuple = tuple(some_range)

# от 1 до 19 с шагом 5
some_range1 = tuple(range(1, 20, 5))  # => (1, 6, 11, 16)

# от 0 до 9 с шагом 3
some_range2 =  tuple(range(0, 9, 3))  # => (0, 3, 6)

# от 5 до -5 с шагом -1
some_range3 =  tuple(range(5, -5, -1))  # => (5, 4, 3, 2, 1, 0, -1, -2, -3, -4)

# cyмма арифметической прогрессии
sum(range(1, 10))

# колличество элементов
len(range(5, 15, 5))

a, b, c = range(5,8)

r = range(1,20)

r[3]
# range объект итерируемый iterable объект предоставляющий возможность поочередного прохода по своим элементам.

# Сравнение размеров
from sys import getsizeof
list_size: int = getsizeof(list(range(0, 10000)))
tuple_size: int = getsizeof(list(range(0, 10000)))

# cool video explain slicing https://www.youtube.com/watch?v=ajrtAuDg3yw