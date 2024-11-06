my_dict = {'Arina': 2005, 'Aleksey': 2003, 'Makar': 2003, 'Victoria': 1969}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Arina'])
print('Not existing value: ', my_dict.get('Gosha'))
my_dict.update({'Maksim': 2006, 'Maria': 1996})
a = my_dict.pop('Maksim')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)


my_set = {1, 1, 2, 3, 'Apple', 43.15, 'Apple'}
print('Set: ', my_set)
my_set.add(7)
my_set.add('Peach')
my_set.remove('Apple')
print('Modified set: ', my_set)