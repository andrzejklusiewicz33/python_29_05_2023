import random
def add(x,y):
    return x+y
def minus(x,y):
    return x-y

def get_data(file_name,div=';',enc='utf-8'):
    return [tuple(linia.strip().split(div)) for linia in open(file_name,encoding=enc) if len(linia.strip())>0]

def get_random_list():
    data=[random.randint(1,100) for e in range(100)]
    #data.append(1.2)
    return data

