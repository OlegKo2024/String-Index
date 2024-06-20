print("20.06.2024")
example = 'University'
print(example[0]) # первый символ строки
print(example[-1]) # пследний символ строки

count = len(example)
mid = count // 2
print(example[mid:]) # вторая половина строки, но как чтобы только нечетное нужен % и логические функции похоже

print(example[::-1]) # слово наоборот

print(example[1::2]) # каждый второй символ строки