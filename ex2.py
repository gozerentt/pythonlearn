slova=""

while len(slova) < 3:
    slova=input("Введите слова:")
    slovas=slova.split(" ")

    if len(slovas) < 3:
        print("Вы ввели меньше 3 слов")

while 'a' in slova:
    num = slova.find('a')
    slova[:num] = 'f'

print(slova)
