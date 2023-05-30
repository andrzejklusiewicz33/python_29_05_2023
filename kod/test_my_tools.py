import my_tools as mt

def test_add():
    assert mt.add(4,5)==9

def test_minus():
    assert mt.minus(10,5)==5

def test_get_data_size():
    assert len(mt.get_data('data.csv'))>0

def test_get_data_type_of_element():
    assert type(mt.get_data('data.csv')[0])==tuple
#
# def test_example():
#     lista = [1, 2, 3, 4, 5, 5,5,4,3,2,1]
#     ok = True
#     for e in lista:
#         if e > 5:
#             ok=False
#     assert ok==True


def test_example():
    lista = [1, 2, 3, 4, 5, 5,5,4,3,2,1]
    ok = True
    for e in lista:
        if e > 5:
            ok=False
    assert ok