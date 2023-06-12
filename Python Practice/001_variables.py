#¿Cómo se crean variables en Python?
# Hay funciones en Python
'''
1: abs()
2: all()
3: any()
4: ascii()
5: bin()
6: bool()
7: breakpoint()
8: bytearray()
9: bytes()
10: callable()
11: chr()
12: classmethod()
13: compile()
14: complex()
15: delattr()
16: dict()
17: dir()
18: divmod()
19: enumerate()
20: eval()
21: exec()
22: filter()
23: float()
24: format()
25: frozenset()
26: getattr()
27: globals()
28: hasattr()
29: hash()
30: help()
31: hex()
32: id()
33: input()
34: int()
35: isinstance()
36: issubclass()
37: iter()
38: len()
39: list()
40: locals()
41: map()
42: max()
43: memoryview()
44: min()
45: next()
46: object()
47: oct()
48: open()
49: ord()
50: pow()
51: print()
52: property()
53. range()
54: repr()
55: reversed()
56: round()
57: set()
58: setattr()
59: slice()
60: sorted()
61: staticmethod()
62: str()
63: sum()
64: super()
65: tuple()
66: type()
67: vars()
68: zip()
69: __import__()

revisar cada una por separado.
'''
# 'len' gives me the number of characters including spaces as one
print('Hello world!')
print('Hello world! has: ')
print(len('Hello world!'))
print('characters.')

print('len shows the value in INT')
print(type(len('Hello world!')))
print('len + 2')
print(len('Hello world!')+2)
print('len / 2')
print(len('Hello world!')/2)

print('it converts numbers to string')
a = str(10)
print(a+' ahora si se puede concatenar con String')
b = str(len('Hello world!'))
print('Hello world has: '+b+' characters.')

# Variables
'''
a) A variable name must start with a letter or the underscore character
b) A variable name cannot start with a number
c) A variable name can only contain alpha-numeric and underscores (A-z, 0-9, and _)
d) Variable names are case-sensitive (firstname, Firstname, Firstname and FIRSTNAME are different variables)
e) We will use standard Python variable naming style which has been adopted by many Python developers.
Python developers use snake case (snake_case) variable naming convention.
'''
my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

print("")
print("Ejemplo:")
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

print(my_int_to_str_variable)

my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, str(my_int_variable), my_bool_variable)
print(my_string_variable, my_int_to_str_variable, my_bool_variable)

#Concatenación de cadenas
print(type(print("My cadena de texto"))) # es tipo: "NoneType"
print("Éste es el valor de: ", my_bool_variable)

#Funciones del sistema
int_variable_lenght = print(len(my_int_to_str_variable))
int_variable_lenght = print(len(my_string_variable))

#Variables en una sola línea
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35

print("My nombre es", name,", mi apellido es",surname,", mi edad es",age, ". Y mi alias es", alias, ".")

# Inputs
first_name = input('what is your name? ')
age = input('what is your age? ')

print(first_name)
print(age)

# Lista
lista_1 = [9,8,7]
lista_2 = lista_1

print(lista_2)
print("el primer dato de la lista es: ",str(lista_2[0]))