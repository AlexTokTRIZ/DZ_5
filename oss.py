import os
import sys
import shutil

from decor import add_separators

@add_separators
def create_pa():
    pa=input('Ведите имя создаваемой папки: ')
    os.mkdir(pa) if not os.path.exists(pa) else print('Такая папка уже существует')

@add_separators
def delete_pa():
    look_pa()
    pa=input('Введите имя удаляемой папки или файла: ')
    if os.path.exists(os.path.join(os.getcwd(),pa)):
        if os.path.isfile(pa):
            os.remove(pa)
        elif os.path.isdir(pa):
            os.rmdir(os.path.join(os.getcwd(), pa))
    else:
        print('Такая папка не существует')
@add_separators
def look_pa(): #"просмотр содержимого рабочей директории"))
    print(os.listdir(os.getcwd()))
@add_separators
def copy_pa(): # "copy_pa", "копировать (файл/папку)"))
    look_pa()
    pa=input('Ведите имя копируемой папки или файла: ')
    if os.path.exists(os.path.join(os.getcwd(),pa)):
        pa_new = input('Ведите новое имя копируемой папки или файла: ')
        if os.path.isfile(pa):
            shutil.copy(os.path.join(os.getcwd(), pa), pa_new)
        elif os.path.isdir(pa):
            shutil.copytree(os.path.join(os.getcwd(), pa), pa_new)
    else:
        print('Такая папка не существует')
@add_separators
def look_pap():
    my_dirs=[]
    for i in os.listdir(os.getcwd()):
            if os.path.isdir(os.path.join(os.getcwd(),i)):
                my_dirs.append(os.path.join(i))
    print(my_dirs)
@add_separators
def look_files(): # "look_files","посмотреть только файлы"))
    my_files=[]
    for i in os.listdir(os.getcwd()):
             if not os.path.isdir(os.path.join(os.getcwd(),i)):
                 my_files.append(os.path.join(i))
    print(my_files)
def look_os():  # "look_os","просмотр информации об операционной системе"))
    print(sys.platform)

def the_creator():  #cоздатель программы"))
    print('Создатель программы - AlexCreo')

def dir_save():  #"сохранить содержимое рабочей директории в файл"
    with open('listdir.txt','w') as f:
        print(look_pap())
        if look_pap()!='None':
            f.write('Dirs  : ')
            f.write(", ".join(look_pap()))
            f.write('\n')
        if look_files()!='':
            f.write('Files : ')
            f.write(", ".join(look_files()))
    print(look_pap())
    print(look_files())
    return


if __name__ == '__main__':
    dir_save()