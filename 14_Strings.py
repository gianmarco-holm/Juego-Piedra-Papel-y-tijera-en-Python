text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''
#Longitud de caracteres
size = len(text)
print(size)

print(text)
#Convierte todo en mayuscula
print(text.upper())
#Convierte todo en minuscula
print(text.lower())
#Conteo de palabras o letra
print(text.count('a'))
#Transforma las letras min a may y alrevez
print(text.swapcase())
#Devuelve un boolean si el texto comienza con la palabra
print(text.startswith('Ella'))
#Devuelve un boolean si el texto termina con la palabra
print(text.endswith('Rust'))
#reemplaza las palabras
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
#Convierte en mayuscula la primera letra
print(text_2.capitalize())
#Convierte en titulo el texto
print(text_2.title())
#Devuelve en boolean si es un digito
print(text_2.isdigit())
print("398".isdigit())