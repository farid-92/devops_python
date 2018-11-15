# -*- encoding: utf-8 -*-

print('Введите слова через пробел')
string = input()
string = string.split()
dictionary = {}
for x in string:
	if x in dictionary:
		dictionary[x] += 1
	else:
		dictionary[x] = 1

maximum = max(dictionary.values())

for key, value in dictionary.items():
	if( value < maximum):
		break
	print(str(value) + ' : ' + key)