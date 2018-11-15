# -*- encoding: utf-8 -*-

print('Введите любые цифры:')
string = input()
integers = string.split()
int_array = []
for i in integers:
	if (i.isdigit()):
		int_array.append(int(i))
	next

minimum = int(min(int_array))
maximum = int(max(int_array))
arr = list(range(minimum,maximum+1))
new_array = list(set(arr) - set(int_array))
print('users list ' + str(int_array))
print('range min to max from users list ' + str(arr))
print('array without users number ' + str(new_array))
print('min from new array ' + str(min(new_array)))