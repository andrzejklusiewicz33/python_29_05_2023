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

# wynik=[linia.strip().split(';') for linia in open('data.csv',encoding='utf-8')]
# for w in wynik:
#     print(w)

#
# wynik=[linia.strip().split(';') for linia in open('data.csv',encoding='utf-8') if len(linia.strip())>0]
# for w in wynik:
#     #print(w,w[3])
#     print(w,len(w))

#10. Dla każdego wpisu w pliku data.csv wyświetl na konsoli dane o
# id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika

# wzrost=1.76
# masa=72
# bmi=round(masa/pow(wzrost,2),2)
# print(bmi)
#
# wzrost='1.76'
# masa='72'
# bmi=round(float(masa)/pow(float(wzrost),2),2)
# print(bmi)
#
# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     bmi=round(float(lista[4])/pow(float(lista[3]),2),2)
#     print(lista,bmi)
#
#
# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     bmi=round(float(lista[4])/pow(float(lista[3]),2),2)
#     print(*lista,bmi)



# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     bmi=round(float(lista[4])/pow(float(lista[3]),2),2)
#     lista.append(bmi)
#     print(lista)

# for linia in open('data.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     #bmi=round(float(lista[4])/pow(float(lista[3]),2),2)
#     #lista.append(bmi)
#     print(lista[3],type(lista[3]))
#
# def get_data():
#     return [linia.strip().split(';') for linia in open('data.csv',encoding='utf-8') if len(linia.strip())>0]
#
# for e in get_data():
#     print(e)

#
# def get_data():
#     return [linia.strip().split(';') for linia in open('data.csv',encoding='utf-8') if len(linia.strip())>0]
#
# data=get_data()
# for d in get_data():
#     print(*d,round(float(d[4])/pow(float(d[3]),2),2))
#

#SOLID
#DRY

# def bmi(w,m):
#     return round(float(m)/pow(float(w),2),4)

# def get_data():
#     return [linia.strip().split(';') for linia in open('data.csv',encoding='utf-8') if len(linia.strip())>0]
#
# data=get_data()
# for d in get_data():
#     print(*d,bmi(d[3],d[4]))

#Hermetyczne, generyczne i skalowalne
#
# def bmi(w,m):
#     return round(float(m)/pow(float(w),2),4)
# def get_data(file_name,div=';',enc='utf-8'):
#     return [linia.strip().split(div) for linia in open(file_name,encoding=enc) if len(linia.strip())>0]
#
# data=get_data('data.csv')
# for d in data:
#     print(d)


# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# print(lista.count(1))
# print(lista.index(7))
# print(len(lista))
# if 1111111 in lista:
#     print('jest')
# else:
#     print('nie ma')

# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# for e in lista:
#     print(e)
#
# for x in range(1,len(lista)):
#     print(lista[x])

#numpy, pandas

# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# print(len(lista),max(lista),min(lista),sum(lista),sum(lista)/len(lista))
#11.


#import matplotlib.pyplot
#
# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# lista.sort()
# print(lista)

#
# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# lista.sort()
# lista.reverse()
# print(lista)


# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# lista.sort(reverse=True)
# print(lista)
#
# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# posortowane=sorted(lista)
# print(posortowane)

#
# krotka=(5,2,7,1,3,4,9,1,1,1,1,3)
# posortowane=sorted(krotka)
# print(posortowane)

#
# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# posortowane=sorted(lista)
# print(posortowane)
# odwrocone=list(reversed(posortowane))
# print(odwrocone)


# lista=[5,2,7,1,3,4,9,1,1,1,1,3]
# posortowane=sorted(lista,reverse=True)
# print(posortowane)

#11. Wygeneruj listę 10 elementów o losowej wartości liczbowej, posortuj listę
# i wyświetl jej zawartość linia po linii
#
# import random
# losowe=[random.randint(1,10) for _ in range(10)]
# print(losowe)
# kopia_posortowana=sorted(losowe)
# print(kopia_posortowana)

#
# import random
# losowe=[random.randint(1,10) for _ in range(10)]
# print(losowe)
# kopia_posortowana=sorted(losowe)
# print(kopia_posortowana)

#
# import random
# losowe=[random.randint(1,10) for _ in range(10)]
# losowe.sort()
# print(losowe)

#
# import random
# losowe=[random.randint(1,10) for _ in range(10)]
# losowe.sort(reverse=True)
# print(losowe)

# def get_random_list(range_start,range_end,count):
#     import random
#     return [random.randint(range_start,range_end) for _ in range(count)]
#
# losowe=get_random_list(1,10,100)
# losowe.sort(reverse=True)
# print(losowe)

#przerwa do 14:40

# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
#
# lista.sort()
# print(lista)
#
# import operator
#
# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
#
# lista.sort(key=operator.itemgetter(1))
# print(lista)


#
# import operator
#
# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
#
# kopia=sorted(lista,key=operator.itemgetter(1))
# print(kopia)

# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self):
#         print('whatever')
#
# p=Person()
#
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         print('whatever')
#         self.first_name=fn
#         self.last_name=ln
#
#     def __str__(self):
#         return str(self.__dict__)
#
# p=Person('Andrzej','Klusiewicz')
# print(p)

#SQLAlchemy

# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         print('whatever')
#         self.first_name=fn
#         self.last_name=ln
#
#     def __str__(self):
#         return str(self.__dict__)
#
# p=Person('Andrzej','Klusiewicz')
# print(p)

#
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         print('whatever')
#         self.first_name=fn
#         self.last_name=ln
#
#     def __str__(self):
#         return str(self.__dict__)
#
# lista=[
#     Person('Andrzej','Klusiewicz'),
#     Person('Tomasz','Burczymucha'),
#     Person('Jan','Zieliński')
# ]
#
# kopia=sorted(lista)
# print(kopia)

#
# import operator
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#
#     def __str__(self):
#         return str(self.__dict__)
#
# lista=[
#     Person('Andrzej','Klusiewicz'),
#     Person('Tomasz','Burczymucha'),
#     Person('Jan','Zieliński')
# ]
#
# kopia=sorted(lista,key=operator.itemgetter(1)) #fuuuuuu to nie ma prawa zadziałać
# print(kopia)


#
# import operator
# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#
#     def __str__(self):
#         return str(self.__dict__)
#
# lista=[
#     Person('Andrzej','Klusiewicz'),
#     Person('Tomasz','Burczymucha'),
#     Person('Jan','Zieliński')
# ]
#
# kopia=sorted(lista,key=lambda x:x.last_name)
# for k in kopia:
#     print(k)
#
#
# import operator
# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
# lista.sort(key=operator.itemgetter(1))
# for k in lista:
#     print(k)


#
# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
# lista.sort(key=lambda e:e[1])
# for k in lista:
#     print(k)

#
# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
# lista.sort(key=lambda koza:koza[1])
# for k in lista:
#     print(k)

#12. Wczytaj do listy list wiersze z pliku data.csv.
# Dane posortuj po masie malejąco i wyswietl linia po linii na konsoli.

# def get_data(file_name,div=';',enc='utf-8'):
#     return [linia.strip().split(div) for linia in open(file_name,encoding=enc) if len(linia.strip())>0]
#
# result=get_data('data.csv')
#
# result.sort(key=lambda e:float(e[4]),reverse=True)
#
# for r in result:
#     print(r)

#
# import operator
# def get_data(file_name,div=';',enc='utf-8'):
#     return [linia.strip().split(div) for linia in open(file_name,encoding=enc) if len(linia.strip())>0]
#
# result=get_data('data.csv')
#
# result.sort(key=operator.itemgetter(4),reverse=True) #sortowanie alfabetyczne...
#
# for r in result:
#     print(r)

#
# import my_tools
# data=my_tools.get_data('data.csv')
# print(data)

#
# import my_tools as mt
# data=mt.get_data('data.csv')
# print(data)
#
# lista=['siała','baba','mak']
# if 'baba' in lista:
#     print('jest')
# else:
#     print('nie ma')


# lista=['siała','baba','mak']
# if 'ba' in lista:
#     print('jest')
# else:
#     print('nie ma')

# string='siała baba mak'
# if 'ba' in string:
#     print('jest')
# else:
#     print('nie ma')

# lista=['siała','baba','mak','bardzo lubię pierogi']
# for e in lista:
#     if 'ba' in e:
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')
#
# lista=['siała','baba','mak','bardzo lubię pierogi']
# print(type(lista))
# for e in lista:
#     if 'ba' in e:
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')

#
# krotka=('siała','baba','mak','bardzo lubię pierogi')
# print(type(krotka))
# for e in krotka:
#     if 'ba' in e:
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')
#
# cos='Andrzej Klusiewicz'
# print(cos)
# print(cos.lower())
# print(cos.upper())
#
# szukane='Ba'
# krotka=('siała','baba','mak','bardzo lubię pierogi')
# print(type(krotka))
# for e in krotka:
#     if szukane.lower() in e.lower():
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')
#
# szukane='Ba'
# krotka=('siała','baba','mak','bardzo lubię pierogi')
# print(type(krotka))
# for e in krotka:
#     if szukane.upper() in e.upper():
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')
#
# import os
# os.mkdir('d:\\nowy')
#
# import os
# for e in os.walk('e:\\'):
#     print(e[0],e[1],e[2])


# import os
# for e in os.walk('e:\\'):
#     print(f'wchodzę do {e[0]}')
#     katalogi=e[1]
#     print('katalogi w tym folderze:')
#     for k in katalogi:
#         print('######',k)

#13.     • Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę
# i katalog startowy. Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace
# w nazwie szukaną frazę - wraz ze ścieżkami. Wyszukiwarka ma być nieczuła na wielkość liter
#
# imie=input('podaj imię:')
# print(f'Hello {imie}')

# import os
# szukane='oRaClE'
# poczatek='e:\\'
# for e in os.walk(poczatek):
#     katalogi=e[1]
#     print(e[0],'katalogi:',e[1])
#     for k in katalogi:
#         if szukane in k:
#             pass
#         #sprawdź czy szukana fraza pojawia sie w nazwie tego katalogu...


#
# import os
# szukane='oRaClE'
# poczatek='e:\\'
# for e in os.walk(poczatek):
#     katalogi=e[1]
#     #print(e[0],'katalogi:',e[1])
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print(e[0],k)
#         #sprawdź czy szukana fraza pojawia sie w nazwie tego katalogu...

#
# import os
# szukane='oRaClE'
# poczatek='e:\\'
# for e in os.walk(poczatek):
#     katalogi=e[1]
#     #print(e[0],'katalogi:',e[1])
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print(e[0]+"\\"+k)
#         #sprawdź czy szukana fraza pojawia sie w nazwie tego katalogu...




# import os
# szukane='oRaClE'
# poczatek='e:\\'
# for e in os.walk(poczatek):
#     katalogi=e[1]
#     #print(e[0],'katalogi:',e[1])
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
        #sprawdź czy szukana fraza pojawia sie w nazwie tego katalogu...

#
# import os
# szukane='oRaClE'
# poczatek='e:\\'
# for e in os.walk(poczatek):
#     katalogi=e[1]
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     pliki=e[2]
#     for p in pliki:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))

#
# import os
# szukane='oRaClE'
# poczatek='e:\\'
# for e in os.walk(poczatek):
#     for k in e[1]:
#         if szukane.lower() in k.lower(): print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower(): print(os.path.join(e[0],p))


# import os
# szukane=input('podaj szukaną frazę:')
# poczatek=input('podaj ścieżkę początkową:')
# for e in os.walk(poczatek):
#     for k in e[1]:
#         if szukane.lower() in k.lower(): print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower(): print(os.path.join(e[0],p))

# import os
# szukane=input('podaj szukaną frazę:\n')
# poczatek=input('podaj ścieżkę początkową:\n')
# for e in os.walk(poczatek):
#     for k in e[1]:
#         if szukane.lower() in k.lower(): print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower(): print(os.path.join(e[0],p))
#
# import math
# import matplotlib.pyplot as plt
# lista1=[math.sin(e) for e in range(1,30)]
# lista2=[math.cos(e) for e in range(1,30)]
# plt.plot(lista1,'r--',label='niebieska kreska')
# plt.plot(lista2,'g:',label='pomarańczowa kreska')
# plt.xlabel('wartości X')
# plt.ylabel('wartości sin i cos')
# plt.grid()
# plt.legend()
# plt.savefig('wykres.png')
# plt.show()


# import math
# import matplotlib.pyplot as plt
# lista1=[math.sin(e) for e in range(1,30)]
# plt.plot(lista1)
# plt.show()
#
# import math
# import matplotlib.pyplot as plt
# plt.plot([math.sin(e) for e in range(1,30)])
# plt.show()

#14. Rzuć na wykres dwie serie posiadające po 50 elementów
#o wartościach losowych z zakresu 1-100. Zadbaj o legendę
#i etykiety osi. Dodaj też siatkę.

#import matplotlib.pyplot as plt

#z konsoli:  pip install matplotlib
#
# import matplotlib.pyplot as plt
# help(plt.plot)

#
# def funkcja():
#     '''To jest help do mojej funkcji.'''
#     print('hello')
#
# help(funkcja)
#
# import matplotlib.pyplot as plt
# import random
# seria1=[random.randint(1,100) for _ in range(50)]
# seria2=[random.randint(1,100) for _ in range(50)]
# plt.plot(seria1,label='losowe 1')
# plt.plot(seria2,label='losowe 2')
# plt.legend()
# plt.grid()
# plt.show()

#seaborn  - ladne wykresy
#JSON API - Fast API
#D3.JS - do wykresów dynamicznych (javascript)
#Python DASH (WTf?) https://www.youtube.com/watch?v=hSPmj7mK6ng
#https://dash.gallery/Portal/

# lista=[1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3]
# zbior={1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3}
# slownik={"klucz1":1111,
#          "klucz2":2222}
# print(type(zbior))
#
# for x in range(100):
#     zbior.add(4)
# print(lista)
# print(zbior)
#
# z1={1,2,3,4}
# z2={3,4,5,6}
# print('z1=',z1)
# print('z2=',z2)
# print('suma=',z1.union(z2))
# print('część wspólna=',z1.intersection(z2))
# print('z1-z2=',z1.difference(z2))
# print('z2-z1=',z2.difference(z1))


# lista=[1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
# print(lista)
# zbior=set(lista)
# print(zbior)
# wynik=list(zbior)
# print(wynik)

# lista=[1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
# result=list(set(lista))
# print(result)

#15. Wygeneruj dwa zestawy, dodaj do nich po 20
# (w przypadku duplikatów lista może być mniejsza niż
# 20 elementów) losowych liczb z zakresu 1-40.
# Wyswietl ich sumę, różnicę i część wspólną
#
# import random
# z1=set([random.randint(1,40) for _ in range(20)])
# z2=set([random.randint(1,40) for _ in range(20)])
# print(z1)
# print(z2)



# import random
# z1={random.randint(1,40) for _ in range(20)}
# z2= {random.randint(1,40) for _ in range(20)}
# print(z1,type(z1))
# print(z2,type(z2))
# print('suma=',z1.union(z2))
# print('część wspólna=',z1.intersection(z2))
# print('z1-z2=',z1.difference(z2))
# print('z2-z1=',z2.difference(z1))

# import my_tools as mt
# lista=set(mt.get_data("data.csv"))
# for e in lista:
#     print(e)
#
# zestaw={
#     (1,'B'),
#     (2,'C'),
#     (1,'B')
# }
# print(zestaw)


# import my_tools as mt
# lista=set(  mt.get_data("data.csv")  )
# for e in lista:
#     print(e)

#map, filter

#przerwa do 10:17

#
# slownik={
#     "klucz1":1234
# }
#
# slownik=dict()
# slownik['klucz1']='wartość 1'
# slownik['inny_klucz']=123456
# slownik['lista']=[1,2,3,4,'whatever']
# slownik['krotka']=(88,88,88,88)
#
#
#
# print(slownik['inny_klucz'])
# print(slownik['lista'])
# slownik['lista']='zmienione'
# print(slownik['lista'])
#
# for k in slownik:
#     print(k,slownik[k])
#
#
# for k in slownik.keys():
#     print(k,slownik[k])
#
# for v in slownik.values():
#     print(v)
#
# if 'gołąb' in slownik:
#     print('mamy taki klucz')
# else:
#     print('nie mamy takiego klucza')
#
# print(list(slownik.values()))
#
# if 'zmienione' in list(slownik.values()):
#     print('mamy taką wartość')
# else:
#     print('nie mamy takiej wartości')
#

#print(config['encoding'])

#16. Stwórz plik ustawienia.txt i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości
#
# import my_tools as mt
# data=mt.get_data('config.conf',div='=')
# config=dict()
# for d in data:
#     print('klucz=',d[0],'wartość=',d[1])
#     config[d[0]]=d[1]
#
# print(config)
# for k in config:
#     print(k,config[k])
#
# print('=======')
# print(config['encoding'])
#print(config['dupa'])


#
# import my_tools as mt
# config=dict(mt.get_data('config.conf',div='='))
# print(config)
# for k in config:
#     print(k,config[k])

#17. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy słów.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
#    c) Przepakuj dane ze słownika do listy i posortuj.

# tadeusz 1032
# trawa 876
# bal 500
#http://andrzejklusiewicz.blogspot.com/
#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia)

#Tadeusz
#Tadeusz,

# all=open('tadzio.txt',encoding='utf-8').read().lower().replace(',','').replace('.','')
# not_wanted=[',','.',':']
# all=all.replace(',','')
# print(all)
# print('ile razy slowo:',all.count('tadeusz'))
#
# print(all.split())
# ['tadeusz','drzewo','costam']

#
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']:
#     all=all.replace(nw,'')
# words=all.split()
# print(words)
#
# import time
# start=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']:
#     all=all.replace(nw,'')
# words=all.split()
# for w in words:
#     #print(w,words.count(w))
#     c=words.count(w)
# end=time.time()
# print(f'czas trwania {end-start}s')
# #print(words)
#

#210s


#import time
#
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']:
#     all=all.replace(nw,'')
# words=all.split()
# print('ilość słów=',len(words))

# import time
# start=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']:
#     all=all.replace(nw,'')
# words=all.split()
# for w in words:
#     c=words.count(w)
# end=time.time()
# print(f'czas trwania {end-start}s')
# #print(words)

# import matplotlib.pyplot as plt
# data=[pow(x,2) for x in range(10000)]
# plt.plot(data)
# plt.show()
#
# import time
# start=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']:
#     all=all.replace(nw,'')
# dct=dict()
# for w in all.split():
#     if w in dct.keys():
#         #dct[w]=dct[w]+1 #jest już takie słowo w słowniku
#         dct[w]+=1
#     else:
#         dct[w]=1 #nie ma takiego słowa w słowniku
# end=time.time()
# print(f'czas trwania {end-start}s')
# #print(words)

#print(0.08/210)

#algorytmy, struktury danych i techniki programowania

#
# import time
# start=time.time()
# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']:
#     all=all.replace(nw,'')
# dct=dict()
# for w in all.split():
#     if w in dct.keys():
#         #dct[w]=dct[w]+1 #jest już takie słowo w słowniku
#         dct[w]+=1
#     else:
#         dct[w]=1 #nie ma takiego słowa w słowniku
# result=[]
# for k in dct:
#     krotka=(k,dct[k])
#     result.append(krotka)
# result.sort(key=lambda x:x[1], reverse=True)
# for r in result:
#     print(r)
# end=time.time()
# print(f'czas trwania {end-start}s')
#print(words)




# all=open('tadzio.txt',encoding='utf-8').read().lower()
# for nw in [',','.','!','?','(',')',':',';','/','-','…','—']: all=all.replace(nw,'')
# dct=dict()
# for w in all.split():
#     if w in dct.keys():
#         dct[w]+=1
#     else:
#         dct[w]=1
# result=[]
# for k in dct:
#     result.append( (k,dct[k]) )
# result.sort(key=lambda x:x[1], reverse=True)
# for r in result:  print(r)


#import this

#przerwa do 11:58
# import time
# def zamulator(x):
#     time.sleep(1)
#     return x*2
#
# for i in range(1,4):
#     print(zamulator(i))
#
# import functools
# import time
#
# @functools.lru_cache(maxsize=10)
# def zamulator(x):
#     time.sleep(1)
#     return x*2
#
# start=time.time()
# for _ in range(10):
#     for i in range(1,4):
#         print(zamulator(i))
# koniec=time.time()
# print(f'czas={koniec-start}s')

#
# def funkcja(x,y):
#     result=x+y
#     return result

# def get_big():
#     result=[]
#     x=0
#     while True:
#         x+=1
#         result.append(f'element numer {x}')
#     return result
#
# data=get_big()
#
# import time
# def get_list():
#     result=[]
#     for x in range(10):
#         time.sleep(1)
#         result.append(x)
#     return result
#
# for g in get_list():
#     print(g)
#
#
# import time
# def get_list():
#     for x in range(10):
#         time.sleep(1)
#         yield x
#
# for g in get_list():
#     print(g)


#
# def get_big():
#     x=0
#     while True:
#         x+=1
#         yield f'element numer {x}'
#
# for g in get_big():
#     print(g)
#
# import time
# import requests
# def ceny_zlota():
#     while True:
#         time.sleep(1)
#         response=requests.get('http://api.nbp.pl/api/cenyzlota')
#         if response.status_code==200:
#             data=response.json()
#             print(data)
#             yield data[0]['cena']
#
# for cz in ceny_zlota():
#     print(cz)


#18. Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal
# elementy o tresci 'element o indeksie x'( gdzie x bedzie numerem podawanego elementu)
# czekajac 1 sekunde przed zwrotem kazdego elementu.
#
# import time
# def generator(ile):
#     for x in range(1,ile+1):
#         time.sleep(1)
#         yield f'element o numerze {x}'
#
#
# for g in generator(10):
#     print(g)

#
# import time
# def generator(ile):
#     for x in range(1,ile+1):
#         time.sleep(1)
#         yield f'element o numerze {x}'
#
# g=generator(10)
# print(next(g))
# print(next(g))
# print(next(g))
#
# for g in generator(10):
#     print(g)

#
# import time
# def generator(ile):
#     for x in range(1,ile+1):
#         time.sleep(1)
#         yield f'element o numerze {x}'
# #
# # g=generator(10)
# # for _ in range(3):
# #     print(next(g))
#
#
# g=generator(10)
# for _ in range(30):
#     print(next(g))

#19. Stwórz generator który będzie podawał nieskończenie wiele liczb parzystych.
# Przetestuj go pobierając z niego kolejne wartości i wyświetlając je na konsoli.
#
# def parzyste(): #fuuuuuu edition
#     x=0
#     while True:
#         x+=1
#         if x%2==0:
#             yield x
#
# for p in parzyste():
#     print(p)


#
# def parzyste(): #fuuuuuu edition
#     x=0
#     while True:
#         x+=2
#         yield x
#
# for p in parzyste():
#     print(p)


#x=0
# for i in range(10):
#     print(i)
#
# x=0
# while x<100:
#     x+=1
#     print(x)
#


x=0
# while 1==1:
#     x+=1
#     print(x)

# while True:
#     x+=1
#     print(x)


#przerwa obiadowa do 13:25

#pytest

#pip install pytest

#Stworz w osobnym module funkcje ktora bedzie zwracala liste 100 losowych liczb z zakresu 1-100.
# Dodaj testy jednostkowe ktore beda sprawdzaly czy funkcja zwrocila 100 elementow,
# czy wszystkie mieszcza sie w zakresie 1-100 i czy wszystkie zwracane wartosci sa
# liczbami calkowitymi


# X=1.2
# print(type(X))
# if type(X)==int:
#     print('to jest liczba całkowita')
# elif type(X)==float:
#     print('to jest liczba zmiennoprzecinkowa')

# import my_tools as mt
# print(mt.get_random_list())

# #
# import time
#
# def mierzczas(koza):
#     def wewnetrzna(*args,**kwargs):
#         start=time.time()
#         koza()
#         koniec=time.time()
#         print(f'czas trwania {koniec-start}s')
#     return wewnetrzna
#
# @mierzczas
# def fun():
#     time.sleep(3)
#     print('koniec funkcji')
#
# fun()


#
# def funkcja(x,y):
#     print('x=',x)
#     print('y=',y)
#
# funkcja(1,2)


# def funkcja(*args):
#     print(args,type(args))
#     print(args,'|',*args)
#
# funkcja(1,2,3,'Kalafior')


# def funkcja(*params):
#     print(params,type(params))
#     print(params,'|',*params)

#funkcja(1,2,3,'Kalafior')

# def funkcja(*params):
#     for p in params:
#         print(p)
#
# funkcja(1,2,3,'Kalafior')

#20. Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args
#
# def fun(*args):
#     print(sum(args))
#
# fun(1,2,3,4,5,6,7)

#21. Stwórz funkcję która przyjmie nieokreśloną liczbę elementów przez argument,
# a następnie wypisze na konsoli ilość otrzymanych elementów.
# Poniżej informacji o ilości otrzymanych elementów wyświetl w osobnych
# liniach każdy argument oraz jego typ.
import time
# def fun(*args):
#     for a in args:
#         print(a,type(a))
#
# fun('nietoperz','toperz',1,3.14,[1,2,3])
#
# def fun(x,*args):
#     pass
#
# fun(None,None)

#
# def fun(*args,x): #fuuuu
#     pass
#
# fun(None,None)

# def fun(x,*args):
#     pass
#
# fun(None,None)

#22. Stwórz funkcję która przyjmie przez argument mnożnik oraz elementy typu args.
# Funkcja ma dla kazdego elementu typu args wyswietlic na konsoli wynik jego
# mnożenia przez mnożnik
#
# def fun(mnoznik,*liczby):
#     for l in liczby:
#         print(l*mnoznik)
#
#
# fun(1000,1,2,3,4)

#przerwa do 14:43

# def fun(param1,param2):
#     print('param1=',param1)
#     print('param2=',param2)
#
# fun(1,2)
# fun(param1=1,param2=2)
# fun(param2=2,param1=1)


# def fun(**kwargs):
#     print(kwargs)
#
# fun(param1=1,param2=2,nowy_param=3)

# def fun(**kwargs):
#     print(kwargs)
#     for k in kwargs:
#         print(k,kwargs[k])
#
# fun(param1=1,param2=2,nowy_param=3)
#

#config(encoding='utf-8', color='red')

#23. Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
# Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach z czego
# pierwsza jest nazwa argumentu a druga jego wartoscia.
# Jesli dane argument juz istnieje w pliku to trzeba bedzie tylko zaktualizowac
# jego wartosc, jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.

#1. najpierw wczytaj konfigurację do słownika
#2. następnie zaktualizuj słownik o nowe ustawienia z parametrów
#3. Na koniec zapisz słownik do pliku z konfiguracją
#
# plik=open('log.log',encoding='utf-8',mode='w')
# plik.write('dupa1\n')
# plik.write('dupa2\n')
# plik.write('dupa3\n')
# plik.close()

#
# with open('log.log',encoding='utf-8',mode='w') as plik:
#     plik.write('dupa1\n')
#     plik.write('dupa2\n')
#     plik.write('dupa3\n')
# print('koniec')
#
# import my_tools
# def config(**kwargs):
#     data=my_tools.get_data('config.conf',div='=')
#     di=dict(data)
#     print(di)
#     for k in kwargs:
#         pass
#
# config(color='red',new_settings='whatever')


#
# import my_tools
# def config(**kwargs):
#     data=my_tools.get_data('config.conf',div='=')
#     print(data)
#     di=dict(data)
#     print(di)
#     for k in kwargs:
#         di[k]=kwargs[k]
#     print(di)
#     with open("config.conf",encoding='utf-8',mode='w') as file:
#         for kk in di:
#             file.write(f'{kk}={di[kk]}\n')
#
# config(color='red',new_settings='whatever')


# def hello():
#     print('hello!')
# def odpal(fun):
#     print(f'dzieki za funkcję: {fun.__name__}')
#     for x in range(10):
#         fun()
#
# odpal(hello)
#print(hello)
#
# def hello():
#     print('hello!')
# def odpal(fun):
#     print(f'dzieki za funkcję: {fun.__name__}')
#     for x in range(10):
#         fun()
#
# odpal(hello)

#
# def hello():
#     print('hello!')
#
# def hello_first_name(first_name):
#     print(f'hello {first_name}!')
#
#
# def odpal(fun):
#     print(f'dzieki za funkcję: {fun.__name__}')
#     for x in range(10):
#         fun()
#
# odpal(hello)

#
# def hello():
#     print('hello!')
#
# def hello_first_name(first_name):
#     print(f'hello {first_name}!')
#
#
# def odpal_bezargumentowy(fun):
#     print(f'dzieki za funkcję: {fun.__name__}')
#     for x in range(10):
#         fun()
#
#
# def odpal_jednoargumentowy(fun,q):
#     print(f'dzieki za funkcję: {fun.__name__}')
#     for x in range(10):
#         fun(q)
#
# odpal_bezargumentowy(hello)
# odpal_jednoargumentowy(hello_first_name,'Andrzej')
#
#
# def hello():
#     print('hello!')
#
# def hello_first_name(first_name):
#     print(f'hello {first_name}!')
#
#
# def odpal(fun,*args):
#     print(f'dzieki za funkcję: {fun.__name__}')
#     for x in range(10):
#         fun(*args)
#
# odpal(hello)
# odpal(hello_first_name,'Andrzej')
#
# import time
#
# def hello():
#     print('hello!')
#
# def odpal(f):
#     time.sleep(2)
#     f()
#
# odpal(hello)



#24. Stwórz dwie funkcje - jedna ma zwracać powiększony tekst który otrzyma
# przez argument, druga analogicznie ale pomniejszony.
# Dodaj funkcję która będzie w stanie przyjąć przez argument inną funkcję
# oraz ciąg tekstowy do obróbki który następnie po obrobieniu przez funkcję
# podaną jako argument zostanie wyświetlony na konsoli
#
# def pomniejsz(text):
#     return text.lower()
# def powieksz(text):
#     return text.upper()
#
# def obrob(fun,text):
#     print(fun(text))
#
#
# obrob(pomniejsz,'siala BABA mak')
# obrob(powieksz,'siala BABA mak')
# obrob(lambda x:x.split(),'siala BABA mak')
# obrob(lambda x:x.upper(),'siala BABA mak')
# obrob(lambda x:x.lower(),'siala BABA mak')

#25. Stworz funkcje ktora bedzie drukowala na konsoli dane otrzymane przez pierwszy argument
# obrobione uprzednio przez wyrazenie lambda podane jako drugi argument.
#
# def siala():
#     print('siała')
#
# def baba():
#     print('baba')
#
# def mak():
#     print('marychę (i dostała 10 lat)')
#
# #s=siala
# #s()
#
# funkcje=[siala,baba,mak]
# for f in funkcje:
#     f()

#print('s=',s)
#
# def pomnoz_przez_dwa(x):
#     return x*2
#
# def podziel_przez_dwa(x):
#     return x/2
#
# def dodaj_dwa(x):
#     return x+2
#
#
# funkcje=[pomnoz_przez_dwa,podziel_przez_dwa,dodaj_dwa]
# for f in funkcje:
#     print(f.__name__ ,f(100)  )

#26. Stwórz funkcję "parse" która będzie otrzymywała przez argumenty wartosc tekstową oraz *args funkcji.
# Funkcja ta ma zastosować każdą z otrzymanych przez *args funkcji na wartości tekstowej którą następnie
# wypisze na konsoli. Dodaj funkcję "powieksz" i "podziel" które mają zwracać otrzymane przez argument
# dane odpowiednio po powiększeniu i podzieleniu tekstu na słowa. Wywołaj funkcję "parse"
# przekazując do niej ciąg tekstowy składający się z więcej niż 1 słowa oraz funkcje "powieksz" i "podziel"



# def parse(text,*functions):
#     for f in functions:
#         text=f(text)
#     print(text)
#
# def powieksz(text):
#     return text.upper()
#
# def podziel(text):
#     return text.split()
#
# parse('siała baba mak',powieksz,podziel)

# def extract():
#     print('extract')
# def transform():
#     print('transform')
# def load():
#     print('load')
#
# # load()
# # extract()
# # transform()
#
#
# #
# def load_warehouse():
#     extract()
#     transform()
#     load()
#
# load_warehouse()
#




# #
# def load_warehouse():
#     def extract():
#         print('extract')
#     def transform():
#         print('transform')
#     def load():
#         print('load')
#     extract()
#     transform()
#     load()
#
# load_warehouse()

#wzorce projektowe


# def oddaj_funkcje():
#     def funkcja():
#         print('dupa')
#     return funkcja
#
#
# f=oddaj_funkcje()
# f()


#27. Stwórz funcję która będzie posiadała dwie funkcje wewnętrzne.
# Jedna z tych funkcji ma powiekszac i zwracac otrzymany ciag znakow,
# druga pomniejszac i zwracac otrzymany ciąg znaków. Funkcja zewnętrzna ma
# zwracać funkcję powiększającą gdy zostanie jej przez argument przekazana wartosc 1
# i funkcję pomniejszającą gdy otrzyma wartość 2.
# Odbierz obiekt funkcji wewnętrznej poprzez wywołanie funkcji zewnętrznej
# i zastosuj otrzymaną funkcję na ciągu tekstowym.

# def dej(x):
#     def powieksz(t):
#         return t.upper()
#     def pomniejsz(t):
#         return t.lower()
#
#     if x==1:
#         return powieksz
#     elif x==2:
#         return pomniejsz
#     else:
#         raise Exception('muka! Nie ma takiej opcji')
#
# f1=dej(1)
# print(f1('siała BABA mak'))
# f2=dej(2)
# print(f2('siała BABA mak'))
# f3=dej(3)

#przerwa do 10:03


# @observer
# def jakas():
#     pass

#@login_required
#
# def siemator():
#     print('no siema!')
# def dekorator(fun):
#     def opakowanie():
#         print('przed')
#         fun()
#         print('po')
#     return opakowanie
#
#
# f=dekorator(siemator)
# f()

#SOLID


# def dekorator(fun):
#     def opakowanie():
#         print('przed')
#         fun()
#         print('po')
#     return opakowanie
#
# @dekorator
# def siemator():
#     print('no siema!')
#
#
# siemator()
#
# def dekorator(fun):
#     def opakowanie():
#         print('przed')
#         fun()
#         print('po')
#     return opakowanie
#
# @dekorator
# def siemator():
#     print('no siema!')
#
# @dekorator
# def siemator_imie(imie):
#     print(f'no siema {imie}!')
#
#
# siemator()
# siemator_imie('Andrzej')


#
#
# def dekorator_bezargumentowy(fun):
#     def opakowanie():
#         print('przed')
#         fun()
#         print('po')
#     return opakowanie
#
#
#
# def dekorator_jednoargumentowy(fun):
#     def opakowanie(i):
#         print('przed')
#         fun(i)
#         print('po')
#     return opakowanie
#
#
# @dekorator_bezargumentowy
# def siemator():
#     print('no siema!')
#
# @dekorator_jednoargumentowy
# def siemator_imie(imie):
#     print(f'no siema {imie}!')
#
#
# siemator()
# siemator_imie('Andrzej')


# #
# def dekorator(fun):
#     def opakowanie(*args,**kwargs):
#         print(f'przed funkcją {fun.__name__}')
#         fun(*args,**kwargs)
#         print(f'po funkcji {fun.__name__}')
#     return opakowanie
#
# @dekorator
# def siemator():
#     print('no siema!')
#
# @dekorator
# def siemator_imie(imie):
#     print(f'no siema {imie}!')
#
#
# siemator()
# siemator_imie('Andrzej')

#siemator_imie(imie='Andrzej')


#
# def dekorator(fun):
#     def opakowanie(*args,**kwargs):
#         print(f'przed funkcją {fun.__name__}')
#         fun(*args,**kwargs)
#         print(f'po funkcji {fun.__name__}')
#     return opakowanie
#
# @dekorator
# def siemator():
#     print('no siema!')
#
# @dekorator
# def siemator_imie(imie):
#     print(f'no siema {imie}!')
#
#
# siemator()
# siemator_imie('Andrzej')



# def dekorator(fun):
#     def opakowanie(*args,**kwargs):
#         print(f'przed funkcją {fun.__name__}')
#         result=fun(*args,**kwargs)
#         print(f'po funkcji {fun.__name__}')
#         return result
#     return opakowanie
#
# @dekorator
# def dej_koze():
#     return 'koza'
#
# x=dej_koze()
# print('x=',x)
#
#
# import my_decorators
# @my_decorators.dekorator
# def dej_koze():
#     print('jestem w funkcji')
#     return 'koza'
#
# x=dej_koze()
# print('x=',x)

#help(dej_koze)


#28. Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
# Dodaj dekorator który zliczy czas wykonywania tej funkcji.
# Pobranie aktualnego czasu to: "time.time()", wstrzymanie na 3 sekundy: "time.sleep(3)"
#
# import time
# start=time.time()
# time.sleep(3)
# koniec=time.time()
# print(f'czas={koniec-start}s')
#
# #@mierzczas

#
#
# def rejestrator(fun):
#     def opakowanie(*args,**kwargs):
#         print(f'przed funkcją {fun.__name__}')
#         result=fun(*args,**kwargs)
#         print(f'po funkcji {fun.__name__}')
#         return result
#     return opakowanie
#
# @rejestrator
# def dej_koze():
#     return 'koza'
#
# x=dej_koze()
# print('x=',x)

#https://realpython.com/
# import time
# def mierzczas(fun):
#     def wewn(*args,**kwargs):
#         print('dekorator!!')
#         start=time.time()
#         x=fun(*args,**kwargs)
#         end=time.time()
#         print(f'czas trwania funkcji {fun.__name__}: {end-start}s')
#         return x
#     return wewn
#
# @mierzczas
# def spij(x):
#     print('chrrrrrr....')
#     time.sleep(x)
#     print('pobudka!')
#
#
#
# spij(3)


#create table log(id serial primary key, function_name text, time_of_run numeric);
#select avg(time_of_run) from log where function_name='spij';
#select function_name, avg(time_of_run) from log group by function_name order by 2 desc;
#
# import time
# import random
# import psycopg2
# def mierzczas(fun):
#     def wewn(*args,**kwargs):
#         start=time.time()
#         x=fun(*args,**kwargs)
#         end=time.time()
#         print(f'czas trwania funkcji {fun.__name__}: {end-start}s')
#         connection=psycopg2.connect(host='localhost',database='postgres',user='postgres',password='oracle')
#         cursor=connection.cursor()
#         cursor.execute(f"insert into log(function_name,time_of_run) values ('{fun.__name__}','{end-start}')")
#         connection.commit()
#         connection.close()
#         return x
#     return wewn
#
# @mierzczas
# def spij(x):
#     #print('chrrrrrr....')
#     time.sleep(x)
#     #print('pobudka!')
#     print('spanko')
#
# @mierzczas
# def inna(x):
#     #print('chrrrrrr....')
#     time.sleep(x)
#     #print('pobudka!')
#
#
# for x in range(10):
#     spij(random.randint(1,4))
#     inna(random.randint(1, 4))
#


#28.     • Stwórz dekorator który będzie rejestrował na konsole wszystkie wywołania
# dekorowanej funkcji z informacją o nazwie dekorowanej funkcji, dacie i czasie jej wywołania
# , argumentach przekazanych do dekorowanej funkcji i ewentualna wartosc zwracana. Log ma być w formacie CSV.
# Same argumenty powinny być rejestrowane w jednej kolumnie razem.
# Pobranie nazwy funkcji: fun.__name__,
# Pobranie aktualnego czasu i daty:
#
# from datetime import datetime
# now = datetime.now()
# print(now.strftime("%d/%m/%Y %H:%M:%S"))
#
# def funkcja(*args):
#     print(','.join( [str(a) for a in args] ))
#
# funkcja(1,'koza','kebab')

#
# from datetime import datetime
# def observe(fun):
#     def inside(*args,**kwargs):
#         result=fun(*args,**kwargs)
#         when = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         print(f'{when};{fun.__name__};args={str(args)},kwargs={str(kwargs)};{result}')
#         return result
#     return inside
#
#
# @observe
# def test(a,b):
#     print('whatever')
#     return a*b
#
# test(3,2)
#
#
# import random
# from datetime import datetime
# def observe(fun):
#     def inside(*args,**kwargs):
#         result=fun(*args,**kwargs)
#         when = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         line = f'{when};{fun.__name__};args={str(args)},kwargs={str(kwargs)};{result}'
#         print(line)
#         with open('mylog.log',encoding='utf-8',mode='a') as file:
#             file.write(line+"\n")
#         return result
#     return inside
#
#
# @observe
# def test(a,b):
#     print('whatever')
#     return a*b
#
# for x in range(20):
#     test(random.randint(1,100),random.randint(1,100))


#przerwa do 11:40

#SQL Achemy

# print(osoba.imie,osoba.nazwisko) #obiekt
# print(osoba[0],osoba[1]) #krotka
#
# class Person:
#     first_name=None
#     last_name=None
#
# p1=Person()
# p1.first_name='Andrzej'
# p1.last_name='Klusiewicz'
# p2=Person()
# p2.first_name='Agnieszka'
# p2.last_name='Borucka'
#
# print(p1.first_name,p1.last_name)
# print(p2.first_name,p2.last_name)
#
#
# class Person:
#     first_name=None
#     last_name=None
#     def witacz(self):
#         print('siema!')
#
# p1=Person()
# p1.first_name='Andrzej'
# p1.last_name='Klusiewicz'
# p2=Person()
# p2.first_name='Agnieszka'
# p2.last_name='Borucka'
#
# print(p1.first_name,p1.last_name)
# print(p2.first_name,p2.last_name)
# p1.witacz()
# p2.witacz()



#
# class Person:
#     first_name=None
#     last_name=None
#     def witacz(self):
#         print(f'siema, jestem {self.first_name} {self.last_name}!')
#
#
#
# p1=Person()
# p1.first_name='Andrzej'
# p1.last_name='Klusiewicz'
# p2=Person()
# p2.first_name='Agnieszka'
# p2.last_name='Borucka'
#
# print(p1.first_name,p1.last_name)
# print(p2.first_name,p2.last_name)
# p1.witacz()
# p2.witacz()

#29.Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
# Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
# Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
#
# class Samochod:
#     marka=None
#     model=None
#     rejestracja=None
#     def wyswietl_mnie(self):
#         print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')
#
# s1=Samochod()
# s1.marka='Renault'
# s1.model='Kadjar'
# s1.rejestracja='WY 12345'
# s2=Samochod()
# s2.marka='Czarny'
# s2.model='Ciągnik'
# s2.rejestracja='POJ 2400'
# s1.wyswietl_mnie()
# s2.wyswietl_mnie()
# # print(s1.marka,s1.model,s1.rejestracja)
# # print(s2.marka,s2.model,s2.rejestracja)

#
# class Person:
#     first_name=None
#     last_name=None
#     def witacz(self):
#         print(f'siema, jestem {self.first_name} {self.last_name}!')
#     def set_values(self,i,n):
#         self.first_name=i
#         self.last_name=n
#
#
#
# p1=Person()
# p1.set_values('Andrzej','Klusiewicz')
# p1.witacz()
# p2=Person()
# p2.set_values('Andrzej','Klusiewicz')
# p2.witacz()

#30. Zadbaj o to by klasa Samochod posiadała metodę pozwalającą ustawić wartości wszystkich pól.
# Jej przykładowe wywołanie: s1.ustaw_wartosci(‘Renault’,’Kadjar’,’WE968RP’)

class Samochod:
    marka=None
    model=None
    rejestracja=None
    def wyswietl_mnie(self):
        print(f'marka={self.marka}, model={self.model}, rejestracja={self.rejestracja}')

s1=Samochod()
s1.marka='Renault'
s1.model='Kadjar'
s1.rejestracja='WY 12345'
s1.wyswietl_mnie()