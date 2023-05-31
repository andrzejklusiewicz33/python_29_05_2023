def dekorator(fun):
    def opakowanie(*args,**kwargs):
        print(f'przed funkcją {fun.__name__}')
        result=fun(*args,**kwargs)
        print(f'odebrane w dekoratorze - wynik z funkcji: {result}')
        print(f'po funkcji {fun.__name__}')
        return result
    return opakowanie
