person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

#Elimina el elemento
del person['last_name']
person.pop('age')

print(person)

#Devuelve los valores clave valor en forma de tuplas
print('items')
print(person.items())

#retorna una lista de las llaves
print('keys')
print(person.keys())

#retorna una lista de los valores
print('values')
print(person.values())