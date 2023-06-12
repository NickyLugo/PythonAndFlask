#
my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string)) # Es la longitud del contenido de la variable

print(my_string+" "+my_other_string)

my_new_line_string = "Éste es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tÉste es un string con tabulación"
print(my_tab_string)

#Formateo
name = "Nicky"
surname = "Lugo"
age = 36
print("Mi nombre es: {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es: %s %s y mi edad es %d" %(name, surname, age))

# %s = string, %d = integer
# inferencia de datos con "f"

print(f"Mi nombre es: {name} {surname} y mi edad es {age}")

# String interpolation /f-STrings(Python 3.6+)
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} / {b} = {a / b:.2f}') # delimita a solo 2 decimales
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)
print(f)

# Division

language_slice = language [1:3]
print(language_slice)

language_slice_dos = language [1:]
print(language_slice_dos)

language_slice_tres = language [-2] # El segundo emmpezando por el último
print(language_slice_tres)

print("Ejemplo con salto: 2, 4, 6 desde Python")
language_slice_cuatro = language [0:6:2] # del 0 : al 6: con saltos de 2
print(language_slice_cuatro)

print("Ejemplo con salto: 3, 6 desde Python")
language_slice_cinco = language [0:6:3] # del 0 : al 6: con saltos de 3
print(language_slice_cinco)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

reversed_language_dos = language[1::-3]
print(reversed_language_dos)


# Métodos o funciones del sistema
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("PY"))
print(language.startswith("py"))

print(language.startswith("Py")) # Empieza con ..
print(language)

