# -*- encoding: utf-8 -*-

print('Введите любой текст через пробел:')
string = input()
string = list(set(string.split(' ')))
string = ' '.join(string)
print(string)
