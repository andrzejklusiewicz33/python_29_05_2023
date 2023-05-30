import pytest
import my_tools as mt

@pytest.mark.proste
def test_add():
    assert mt.add(4,5)==9

@pytest.mark.proste
def test_minus():
    assert mt.minus(10,5)==5

@pytest.mark.trudne
def test_get_data_size():
    assert len(mt.get_data('data.csv'))>0

@pytest.mark.trudne
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

def test_get_random_list_count():
    assert len(mt.get_random_list())==100

def test_get_random_list_range():
    ok=True
    data=mt.get_random_list()
    for d in data:
        if d>100 or d<1:
            ok=False
    assert ok

def test_get_random_list_type():
    ok=True
    data=mt.get_random_list()
    for d in data:
        if type(d)!=int:
            ok=False
    assert ok