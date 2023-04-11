# STRUCTURE DE DONNEES LES BASE
# Listes
username_list = ['donald', 'frank', 'samuel']
username_list[0] = 'Programmmeur'
print(username_list)

print(username_list[0])

print(username_list[2])

# Les Tuples

username_tuples = ('donald', 'frank', 'samuel')
print(username_tuples)
print(username_tuples[0])
print(username_tuples[2])

# Ensembles

username_set = {'donald', 'donald', 'frank','samuel'}
username_set = set(['donald', 'donald'])
print(username_set)
print(username_set)
username_set.add('programmeur')
username_set.remove('donald')
print(username_set)

# Dictionnaires

user_data = {
    0: ['donald', 23],
    1: ['frank', 24]
}

print(user_data)
user_data[0] = ['donald programmeur', 23]
print(user_data[0])
print(user_data)


ensenble_num = set([1,3,4,5,6,7,8,8])
for element in ensenble_num:
    print(element)

dict_element = dict()
dict_element['name'] = 'donald'
dict_element['age'] = 23
for key, value in dict_element.items():
    print(key, value)

