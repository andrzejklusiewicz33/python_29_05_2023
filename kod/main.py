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
#
# import random
# print(random.random())
# print(random.randint(1,100))

#3. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)

#
# import random
# l1=[]
# l2=[]
# for x in range(10):
#     l1.append(random.randint(1,10))
#     l2.append(random.randint(1, 10))
#
# print(l1)
# print(l2)

#
# import random
# l1=[]
# l2=[]
# for _ in range(10):
#     l1.append(random.randint(1,10))
#     l2.append(random.randint(1, 10))
#
# print(l1)
# print(l2)


# import random
# l1=[]
# l2=[]
# for _ in range(10):
#     l1.append(random.randint(1,10))
#     l2.append(random.randint(1, 10))
#
# print(l1)
# print(l2)
# suma=[*l1,*l2]
# print(suma)

# import random
# l1=[]
# l2=[]
# for _ in range(10):
#     l1.append(random.randint(1,10))
#     l2.append(random.randint(1, 10))
#
# print(l1)
# print(l2)
# l1.extend(l2)
# print(l1)

#przerwa do 11:46
#
# lista=[
#     [1,2],
#     [3,4],
#     ['lubię','pierogi']
# ]
#
# for e in lista:
#     print(e)
#
# print('---------------------')
# print(lista)
# print(lista[2])
# podlista=lista[2]
# print(podlista[1])
# print(lista[2][1])

# lista=[]
# podlista=[1,2,3]
# lista.append(podlista)
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     podlista=[x,x*100]
#     lista.append(podlista)
#
# print(lista)
# for e in lista:
#     print(e)

#4. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#
# lista=[]
# for x in range(1,11):
#     podlista=[x,pow(2,x)]
#     lista.append(podlista)
# print(lista)
# for e in lista:
#     print(e)

#
# lista=[]
# for x in range(1,11):
#     lista.append(  [x,pow(2,x)] )
# print(lista)
# for e in lista:
#     print(e)

#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# for e in lista:
#     print(e)


#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11)]
# print(lista)
#
# lista=[x*1000 for x in range(1,11)]
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# lista=[x for x in range(1,11) if x%2==0]
# print(lista)


#
# lista=[]
# for x in range(1,11):
#     if x%2==0:
#         lista.append(x)
# print(lista)
#
# print( [x for x in range(1,11) if x%2==0] )

# lista=[x*1000 for x in range(1,11) if x%2==0]
# print(lista)
#
# lista=[f'element {x}' for x in range(1,11) if x%2==0]
# print(lista)
#
# import random
# lista=[random.randint(1,100) for _ in range(1,11)]
# print(lista)
# print([random.randint(1,100) for _ in range(1,11)])

#5. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2

# lista=[pow(2,x) for x in range(1,11)]
# print(lista)

# lista=[pow(2,x) for x in range(1,11)]
# print(lista)
# for e in lista:
#     print(e)
#
# for e in [pow(2,x) for x in range(1,11)]: print(e)

#6.  Korzystając z list składanych wygeneruj listę 10 elementow której każdy element
# również będzie listą. Pierwszy element tej podlisty to numer potegi, a drugi to wartosc
# tej potegi dla liczby 2

# lista=[
#     [1,2],
#     [2,4],
#     [3,8]
# ]
#
# lista=[]
# for x in range(1,11):
#     podlista=[x,pow(2,x)]
#     lista.append(podlista)
#
# for e in lista:
#     print(e)


# lista=[]
# for x in range(1,11):
#     lista.append( [x,pow(2,x)] )
#
# for e in lista:
#     print(e)
#
# lista=[[x,pow(2,x)] for x in range(1,11)]
#
# for e in lista:
#     print(e)
#
# for e in [[x,pow(2,x)] for x in range(1,11)]: print(e)

# dane=[2,4,1,7,56,3,1,23,4,33,44,11111]
# nieparzyste=[x*1000 for x in dane]
# print(nieparzyste)
#
# dane=[2,4,1,7,56,3,1,23,4,33,44,11111]
# nieparzyste=[x for x in dane if x%2==1]
# print(nieparzyste)
# przetworzone_nieparzyste=[x*1000 for x in dane if x%2==1]
# print(przetworzone_nieparzyste)

# def fun(x):
#     return x*1000
#
# dane=[2,4,1,7,56,3,1,23,4,33,44,11111]
# przetworzone_nieparzyste=[fun(x) for x in dane if fun(x)>1000]
# print(przetworzone_nieparzyste)
#

#Wygeneruj listę 20 elementów losowych liczbowych w zakresie 1-100
#Stwórz dwie nowe listy. Do jednej skopiuj elementy wieksze od 50,
#a do drugiej mniejsze bądź równe 50. Wszystkie trzy listy wydrukuj.

#przetworzone_nieparzyste=[x*1000 for x in dane if x%2==1]

# import random
# losowe=[random.randint(1,100) for _ in range(20)]
# print(losowe)
# male=[x for x in losowe if x<=50]
# duze=[x for x in losowe if x>50]
# print('male=',male)
# print('duze=',duze)

# linia="2;Arnold;Boczek;1.65;120"
# print(linia)
# lista=linia.split(';')
# print(lista)

#
# for linia in open('data.csv',encoding='utf-8'):
#     print(linia.strip().split(';'))
#
# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[2])

#
# print('hajs '*1000)

#
# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista)
#     print(lista[2].upper())
#     wzrost=lista[3]
#     print(float(wzrost)*2)

#8. Napisz program który z pliku data.csv
# wyświetli powiekszone imiona i nazwiska oraz wzrost i masę

# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])

#Przerwa obiadowa 13:20

#9. Korzystajac z list skladanych zaladuj do listy zawartosc pliku data.csv
# w taki sposób   by linie oczyścic z bialych znaków i rozbić na listy.
# Każdy z elementów listy sam   powinien byc listą.
# Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy   linia po linii.
#
# wynik=[]
# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     wynik.append(lista)
#
# for w in wynik:
#     print(w)
#
# print(wynik)

wynik=[linia for linia in open('data.csv',encoding='utf-8')]
for w in wynik:
    print(w)
