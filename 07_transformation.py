name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Nicolas" + " Molina")
print(10 + 20)
print("Nicolas" + "12")

age = 12
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 aÃ±os serÃ¡ {age}')

name = input('¿Cuál es tu nombre? => ')
print(name)
last_name = input('¿Cuál es tu apellido? => ')
print(last_name)
age = input('¿Cuál es tu edad? => ')
print(age)

template = f"Hola mi nombre es {name} {last_name}, tengo {age} años y en 10 años tendré " + str(
  int(age) + 10) + " años"
print(template)
ag2 = int(age)
template = f"Hola mi nombre es {name} {last_name}, tengo {age} años y en 10 años tendré {age+10} años"
print(template)
