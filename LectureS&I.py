name = 'Oleg' # переменная name со строкой Oleg
print('Hello, '+ name +'!') # строка, переменная, строка
print('Hello, ''Oleg''!') # три строки 'Hello, ' и 'Oleg' и '!'
print('Hello, ' + 'Oleg' + '!')
print('Hello, ' *5 + 'Hello') # операция умножения
print('Hello, ' *5,'Hello') # операция умножения
print(name[0], name[-1]) # начинается с 0 слева и с -1 справа
print(name[0:2], name[-1]) # двоеточие разделяет начало и конец. Последний элемент среза строки обозначает до, не вкл.
print(name[0:3]) # с нулевого по третий символ
print(name[0:3:2]) # с нулевого по третий индекс с шагом два
print(name[0:3:2]) # квадратные скобки могут принимать три значения: первое обязательно и два интервал и шаг не обязательно
print(name[-1:4:2]) # справа не работает
print(name[0:2]) # Ol
print(name[:4:2]) # Oe от 0 до 4
print(name[1:])
print(name[:])
print(name[0:], name[:-1])
print(name[::-1]) # пропуская начало и конец и иду справа с шагом 1
