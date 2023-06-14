### --- Lists (Arrays)--- ###

my_list = list()
my_other_list = []

print(len(my_list))
my_list= [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Nick', 'Moure']

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # in reverse the 1st from right to left
print(my_other_list[-3]) # in reverse the 3rd from right to left

#print(my_other_list[4]) # straight way the 4th doesn't exist --IndexError: out of range--
#print(my_other_list[-5]) # in reverse the 5th doesn't exist --IndexError: out of range--

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple() 

print(my_other_list.count())