my_dict = {'Vlad': 1998, 'Igor': 1966, 'Olesya': 1990}
print(my_dict)
print(my_dict.get('Vlad'))
print(my_dict.get('Luba'))
my_dict.update({'Galya': 1970, 'luba': 2000})
a = my_dict.pop('Igor')
print(a)
print(my_dict)

my_set = {1, 3, 5, 'Urban', 1, 5}
print(my_set)
my_set.add(4)
my_set.add(6)
my_set.discard(1)
print(my_set)
