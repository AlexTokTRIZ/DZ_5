# тесты для консольного файлового менеджера (чистые и грязные)

from change_pa import *
from oss import*
import os

def test_dirpath_recurs():
    path = os.getcwd()
    print(path)
    print(dirpath_recurs(path))
    assert type(dirpath_recurs(path)) == type(['test'])

def test_look_os():  # "look_os","просмотр информации об операционной системе"))
    assert look_os()==sys.platform

def test_the_creator():  #cоздатель программы"))
    assert the_creator()=='Создатель программы - AlexCreo'
