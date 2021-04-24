import os
from myLib import bilder# моя написанная библиотека
import shutil  # для копирования файлов

def sherchSmallFilesSize(pathDirectory,sizeFileStop=1000):
    '''
    Ищёт файлы которые не соотвествуют кретерию по размеру и перемещает их в новую папку
    :param pathDirectory: директория где будет происходить поиск файлов
    :param sizeFileStop: размер файлов(в кб),  которые отсеиваются
    :return:
    '''
    Mybilder = bilder(pathDirectory + r'\temp')  # инцилизация нового класса
    Mybilder.bildFolderInDerectory(True, True)  # создание новой папки+ вывести сообщение об этом

    ''' перебор папок только в текущем каталоге, без рекульсивного вызова'''
    names = os.listdir(pathDirectory) # путь к деректории
    for fileName in names: # перебор значений
        fullname = os.path.join(pathDirectory, fileName) # склеивание имени файла и пути его пути
        if os.path.isfile(fullname):
            sizeFile = int(os.path.getsize(fullname))  # размер файла
            if sizeFile <= sizeFileStop:
                print('copy file: ', fileName,
                      ' in folder ', pathDirectory + '\\temp', '\n', 'delite file: ', fileName, 'from ',
                      pathDirectory)  # выводит информацию о копировании в новую временную папку
                shutil.copy2(pathDirectory + '\\' + fileName, pathDirectory + r'\temp' + '\\'  + fileName)  # копирование в новую временную папку
                os.remove(pathDirectory + '\\' + fileName) # удаление файла


sherchSmallFilesSize('C:\\Users\\Ilya\\PycharmProjects\\searchImages\\downloaded images',100000)