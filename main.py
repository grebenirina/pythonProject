#1. Найти максимальную цифру введенного натурального числа.
number = int(input("Введите число: "))
max = 0
while number > 0:
    ostatok = number % 10
    if ostatok > max:
        max = ostatok
    number = number // 10
print("Наибольшая цифра = ", max)

#2. Дана строка, в которой имеется текст в скобках. Удалить часть
#текста, заключенного в скобки.
str = input("Введите строку: ")
a = -1
b = -1
i = 0
while i < len(str):
    if str[i]=="(":
        a=i
    if str[i]==")":
        b=i+1
    i=i+1
if a == -1 or b == -1 or a > b:
    print("Нет текста в скобках.")
else:
    str1 = str[:a]
    str2 = str[b:]
    print(str1 + str2)

#3. Найдите наименьший четный элемент списка. Если такого нет, то
#выведите первый элемент. Преобразовать список так, чтобы сначала
#шли нулевые элементы, а затем все остальные.
spisok = []
kolich = int(input("Сколько элементов будет в вашем списке: "))
print("Введите ", kolich, "элементов: ")
for i in range(0, kolich):
    new_el = int(input())
    spisok.append(new_el)
print("Полученный список: ", spisok)
max = spisok[0]
for i in range(1, len(spisok)):
    if spisok[i] > max:
        max = spisok[i]
min_chet = max
kol_chet = 0
for i in range(0, len(spisok)):
    if spisok[i] % 2 == 0:
        kol_chet = kol_chet + 1
        if spisok[i] < min_chet:
            min_chet = spisok[i]
if kol_chet == 1:
    print("В списке один четный элемент равный ", min_chet)
elif kol_chet == 0:
    print("В списке нет четных элементов.")
else:
    print("Наименьший четный элемент: ", min_chet)

#4. Создайте словарь из строки ' Follow your heart' следующим
#образом: в качестве ключей возьмите символы строки, а значениями
#пусть будут числа, соответствующие количеству вхождений данной
#буквы в строку.
str = ' Follow your heart'
slovar = {}
for i in range(0, len(str)):
    kol = 0
    for k in range(0, len(str)):
        if str[i] == str[k]:
            kol = kol + 1
    slovar.update({str[i]:kol})
print("Словарь из строки ' Follow your heart':\n", slovar)

# 5. Реализуйте программу «Магазин игрушек», которая будет
# включать в себя шесть пунктов меню. У вас есть словарь, где ключ –
# название игрушки. Значение – список, который содержит состав
# игрушки, цену и кол-во (шт),которое есть в магазине.
# 1. Просмотр описания: название – описание
# 2. Просмотр цены: название – цена.
# 3. Просмотр количества: название – количество.
# 4. Всю информацию.
# 5. Покупка
# В пункте «Покупка» необходимо совершить покупку, с
# клавиатуры вводите название игрушки и его кол-во, n – выход из
# программы. Посчитать цену выбранных товаров и сколько товаров
# осталось в изначальном списке.
# 6. До свидания
magazin = {
    'машинка':['пластик', 20, 5],
    'кукла':['пластик', 25, 3],
    'мишка':['плюш', 40, 10],
    'монополия':['бумага', 50, 4],
    'мячик':['резина', 30, 10],
    'юла':['пластик', 15, 6]
}

print("Наличие магазина:")
for key in magazin:
    print(key)
choice = int(input(
    "Меню:\n"
    "1. Просмотр описания\n"
    "2. Просмотр цены\n"
    "3. Просмотр количества\n"
    "4. Всю информацию\n"
    "5. Покупка\n"
    "6. До свидания\n"
    "Ваш выбор: "))
while True:
    if choice == 1:
        igrushka = input("Введите игрушку, описание которой хотите посмотреть: ")
        if igrushka in magazin:
            print("Материал: ", magazin[igrushka][0])
        else:
            print("Данной игрушки нет в наличии")
        choice = int(input("Ваш выбор: "))
    elif choice == 2:
        igrushka = input("Введите игрушку, цену которой хотите посмотреть: ")
        if igrushka in magazin:
            print("Цена: ", magazin[igrushka][1])
        else:
            print("Данной игрушки нет в наличии")
        choice = int(input("Ваш выбор: "))
    elif choice == 3:
        igrushka = input("Введите игрушку, количество которой хотите посмотреть: ")
        if igrushka in magazin:
            print("Описание: ", magazin[igrushka][2])
        else:
            print("Данной игрушки нет в наличии")
        choice = int(input("Ваш выбор: "))
    elif choice == 4:
        igrushka = input("Введите игрушку, информацию о которой хотите посмотреть: ")
        if igrushka in magazin:
            print("материал: ", magazin[igrushka][0])
            print("цена: ", magazin[igrushka][1])
            print("количество: ", magazin[igrushka][2])
        else:
            print("Данной игрушки нет в наличии")
        choice = int(input("Ваш выбор: "))
    elif choice == 5:
        summa = 0
        while True:
            igrushka = input("Какую игрушку хотите приобрести? ")
            if igrushka in magazin:
                print(f"В наличие {magazin[igrushka][2]} шт.")
                skolko = int(input("Какое количество вы хотите приобрести: "))
                summa = summa + magazin[igrushka][1] * skolko
                magazin[igrushka][2] = magazin[igrushka][2] - skolko
                ch = int(input("Хотите приобрести еще игрушку?\n1.да\n2.нет: "))
                if ch == 2:
                    break
            else:
                print("Данной игрушки нет в наличии")
        print(f"Итого : {summa} руб.")
        choice = int(input("Ваш выбор: "))
    elif choice == 6:
        print("До свидания!")
        break
    else:
        print("неверное значение")
        choice = int(input("Ваш выбор: "))

# 6. Даны два кортежа. Создайте третий кортеж, который будет
# включать в себя элементы первого и второго.
tuple1 = ('mama', 'papa')
tuple2 = ('brat', 'sestra')
tuple3 = sum((tuple1, tuple2), ())
print("Первый кортеж: ", tuple1)
print("Второй кортеж: ", tuple2)
print("Полученный кортеж: ", tuple3)