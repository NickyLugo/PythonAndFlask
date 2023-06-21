### --- Lists (Arrays)--- ###

my_list = list()
my_other_list = []

#Nuestra lista sirve para añadir elementos y por ahora esta vacía.
#El primer elemento es la posición cero "0"
print(len(my_list))
my_list= [35, 24, 62, 52, 30, 30, 17]

#Cuando ya tenemos elementos en la lista, podemos llamarlos a impresión.
#Vemos el largo de la lista, "len" cuenta los elementos en la lista
print(my_list)
print(len(my_list))


my_other_list = [35, 1.77, 'Nick', 'Moure']

print(type(my_list))
print(type(my_other_list))
print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # in reverse the 1st from right to left
print(my_other_list[-2]) # in reverse the 3rd from right to left

#print(my_other_list[4]) # straight way the 4th doesn't exist --IndexError: out of range--
#print(my_other_list[-5]) # in reverse the 5th doesn't exist --IndexError: out of range--

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple() 

#el método Count cuenta las veces que un elemento aparece dentro de la propia lista
print(my_other_list.count("Nick"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)
print(age)

my_other_list.append("PanaderiaBatalla")
print(my_other_list)
print(" ")

my_other_list.insert(1,"Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

# Pop elimina el último elemento por defecto y lo que retorna es el elemento en tipo: int
print(my_list.pop())

print(my_list.pop())
