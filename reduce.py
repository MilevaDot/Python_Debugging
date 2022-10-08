### Reduce es una función de order superior
# Vamos a resolver un problema de dos maneras distintas.
# Queremos obtener el producto de los elementos de my_list.
my_list = [2, 2, 2, 2, 2]

# Primero con un for normal.
# mult = 1
# for i in my_list:
#     mult = mult * i
# print(mult)

# Ahora con reduce.

from functools import reduce
mult_reduce = reduce(lambda a,b: a*b, my_list)
print(mult_reduce)