
def add(x,y):
    return x+y
def minus(x,y):
    return x-y

def get_data(file_name,div=';',enc='utf-8'):
    return [tuple(linia.strip().split(div)) for linia in open(file_name,encoding=enc) if len(linia.strip())>0]

