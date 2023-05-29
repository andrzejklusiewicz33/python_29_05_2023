#test
# import time
#
# def fun():
#     data=[1,2,3,4,5]
#     time.sleep(5)
#     return data

# def fun():
#     data=[1,2,3,4,5]
#     for x in range(5):
#         time.sleep(1)
#         yield data[x]
#     #time.sleep(5)
#     #return data


#przerwa do XX:XX

#D3.js
#FastAPI

# for e in fun():
#     print(e)

#print('whatever')

#przerwa do 10:16

# lista=[]
# krotka=()
# slownik={}
# print(type(lista))
# print(type(krotka))
# print(type(slownik))

#lista=[]
#lista=list()
#
# for x in range(1,11):
#     print(x)

#lista=['pomarańcza','cytryna','arbuz','banan']
# print(lista)
# print(lista[0])
# print(lista[3])
# print(lista[0:3])
# print(lista[0:3:2])
# lista=['pomarańcza','cytryna','arbuz','banan']
# for element in lista:
#     print(element)

#
# lista=['pomarańcza','cytryna','arbuz','banan']
# lista.append('dodane')
# lista.insert(0,'pierwszy')
# lista[1]='podmienione'
# for element in lista:
#     print(element)

#lista=[1,2,3,4]
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)

# lista=['1','4','3','2','11','22','whatever']
# lista.sort()
# print(lista)

#print(pow(2,10))

#1. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

# lista=[]
#
# for x in range(1,11):
#     print(x)
#
# print(pow(2,10))
#
# for e in lista:
#     print(e)
#
# lista=[]
# for x in range(1,11):
#     lista.append(pow(2,x))
#
# for e in lista:
#     print(e)

# lista=[1,2,3,4]
# for x in range(1,11):
#     print(x)
#
# lista=[1,2,3,4]
# for x in lista:
#     print(x)

#
# for x in (1,2,3,4):
#     print(x)

#2. Stwórz listę zawierającą 100 elementów tekstowych o zawartości "ELEMENT NUMER X"
#Następnie przeiteruj po liście i wyświetl jej zwaartość element po elemencie.
# x=10
# print(f"element numer {x}")

#zwierze='koza'
#print("moje ulubione zwierze to: "+zwierze)

# x=33
# print(type(x))
# #print('moja ulubiona liczba to '+x)
#
# x=str(33)
# print(type(x))
# print('moja ulubiona liczba to '+x)

#
# x=33
# print('moja ulubiona liczba to '+str(x))


# x=33
# wiek=36
# print('moja ulubiona liczba to '+str(x)+" Mc'Donalds. Mam "+str(wiek)+" lat")
#
# x=33
# wiek=36
# print('moja ulubiona liczba {}. Mam {} lat'.format(x,wiek))

# x=33
# wiek=36
# cos=1111
# print('moja ulubiona liczba {}. Mam {} lat'.format(x,wiek,cos))
#
# x=33
# wiek=36
# print(f"Moja ulubiona liczba to {x}. Mam {wiek} lat")
#
# lista=[]
# for x in range(1,101):
#     print("element numer "+x)

#
# lista=[]
# for x in range(1,101):
#     print("element numer "+str(x))

#
# lista=[]
# for x in range(1,101):
#     print("element numer {}".format(x))

#
# lista=[]
# for x in range(1,101):
#     print(f"element numer {x}")


# lista=[]
# for x in range(1,101):
#     lista.append(f"element numer {x}")
# print(lista)
# for l in lista:
#     print(l)


# class Car:
#     id=None
#     mark=None
#     model=None
#
#     def __init__(self,i,ma,mo):
#         self.id=id
#         self.mark=ma
#         self.model=mo
#
#     def __str__(self):
#         return str(self.__dict__)
#
# lista=[1,"Renault","Kadjar"]
# print(lista)
# print(*lista)
#
# car=Car(lista[0],lista[1],lista[2])
# print(car)

#
# car=Car(*lista)
# print(car)
#
# def fun(arg1,arg2,arg3):
#     print(f'arg1={arg1}, arg2={arg2}, arg3={arg3}')
#
# lista=[1,2,3]
# #fun(1,2,3)
# fun(*lista)
#
# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# #fuuuuu version
# lista_suma=[]
# for l in lista1:
#     lista_suma.append(l)
# for l in lista2:
#     lista_suma.append(l)
# print(lista_suma)

#
# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista_suma=[lista1,lista2]
# print(lista_suma)
# for e in lista_suma:
#     print(e)
#
#
# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista_suma=[*lista1,*lista2]
# print(lista_suma)
# for e in lista_suma:
#     print(e)



# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista1.extend(lista2)
# print(lista1)
# for e in lista1:
#     print(e)
# lista2.clear()

# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista1.append(lista2)
# print(lista1)
# for e in lista1:
#     print(e)

# lista1=[1,2,3,4]
# lista2=[5,6,7,8]
# lista1.extend(lista2)
# print(lista1)
# for e in lista1:
#     print(e)
#
# lista1=[1,2,3,4]
# lista2=lista1 #przez wskaźnik
# lista1.clear()
# print('lista 1=',lista1)
# print('lista 2=',lista2)

#
# lista1=[1,2,3,4]
# lista2=lista1.copy()
# lista1.clear()
# print('lista 1=',lista1)
# print('lista 2=',lista2)
#
# x=1
# y=x
# x=0
# print(x,y)

#lista=[]

import random
print(random.random())
print(random.randint(1,100))

#3. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)
