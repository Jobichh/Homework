immutable_var = 1, 3, True, 'string'
print(immutable_var)
#не можем изменить так как,кортеж неизменяемая структура, кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3,4]
mutable_list.append('Modified')
print(mutable_list)