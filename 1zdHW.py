 #Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
list_1 = list()
number = int(input('введите кол-во элементов первого массива')) #пользователь вводит число 
list_2 = list() 
number2 = int(input('введите кол-во элементов второго массива')) #пользователь вводит число 
for i in range(number): 
 n = int(input()) # пользователь вводит целое число
 list_1.append(n) # 
for i in range(number2): 
   n = int(input()) # пользователь вводит целое число
   list_2.append(n) # 
print(list_1)
print(list_2)
list_3 = list()
for i in list_1:
    if i in list_2 and i not in list_3:
            list_3.append(i)
print (list_3)
list_3.sort()
print (list_3)
