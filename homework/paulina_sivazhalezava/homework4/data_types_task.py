my_dict = {'tuple': ('cat1', 'cat2', 'cat3', 'cat4', 'cat5'),
           'list': [4, 5, 3, 4, 8],
           'dict': {'dog1': 'Rex', 'dog2': 'Suslik', 'dog3': 'Aku', 'dog4': 'Hunter', 'dog5': 'Volchok'},
           'set': {1.1, 1.2, 1.3, 1.4, 1.5}}

print('last element of tuple :', my_dict['tuple'][-1])
my_dict['list'].append(10)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 1
my_dict['dict'].__delitem__('dog3')
my_dict['set'].add(1.6)
my_dict['set'].remove(1.3)

print(my_dict)
