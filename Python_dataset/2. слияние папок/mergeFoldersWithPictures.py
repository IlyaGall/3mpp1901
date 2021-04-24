import numpy as np
from PIL import Image  # pip install Pillow
import os
import shutil  # для копирования файлов
from myLib import bilder
from myLib import LibFiles

def mergeFoldersWithPictures(path1, path2, nameFolder='mergeFolders',proverkaImages=False):
    '''
    слияние папок с картинками
    ф-я нужна для слияния 2-х папок в одну с одинаковым названием картинок
    ф-я(mergeFoldersWithPictures) нужна для подсчёта
    кол-во файлов для объеденения папок
    !!! нужно чтобы название файлов было по порядку начиная с 0.img
    :param path1: путь к первой папке
    :param path2: путь ко второй папке
    :param nameFolder: название папки в которую будут доваблены файлы с 2-х папок
    :return: nope
    '''
    myBilder = bilder(nameFolder)  # создаю экземпляр класса для использования в дальнейшем
    myBilder.bildFolder(True, True, True)  # вызываю метод из класса, который инцилизировал выше
    myLibFiles = LibFiles(nameFolder)

    lenFilesInFirstFoder = 0  # переменная в которую будет записано кол-во файлов в первой папке
    lenFilesInSecondFoder = 0  # переменная в которую будет записано кол-во файлов во второй папке
    for root, dirs, files in os.walk(path1):
        lenFilesInFirstFoder = len(files)  # Узнаем длину(количество файлов в папке)
        countCopyProcent = 0  # подсчёт в процентах сколько осталось
        countAddOneProcent = 100 / lenFilesInFirstFoder  # 100% делим на кол-во, чтобы узнать, сколько осталось
        for file in files:
            print(str('copy File: ' + file + ' From :' + path1 + '/' + file))  # вывод какой файл копируется и откуда
            countCopyProcent += countAddOneProcent  # добавления процентный доли
            print('Progress : ', round(countCopyProcent), '%')  # прогресс в %
            print(os.getcwd() + '\\' + nameFolder)
            print(os.getcwd() + '\\' + path1 + '\\' + str(file))
            if proverkaImages==True:
                if poverca(os.getcwd() + '\\' + nameFolder, os.getcwd() + '\\' + path1 + '\\' + str(file))==False:
                   shutil.copy2(os.getcwd() + '\\' + path1 + '\\' + str(file), os.getcwd() + '\\' + nameFolder + '\\' + str(file))  # копирование в новую папку слияния
            else:
                shutil.copy2(os.getcwd() + '\\' + path1 + '\\' + str(file),
                             os.getcwd() + '\\' + nameFolder + '\\' + str(file))  # копирование в новую папку слияния
    print(os.getcwd() + '\\' + nameFolder)
    ###############################################################
    '''вторая папка'''
    ###############################################################
    for root, dirs, files in os.walk(path2):
        lenFilesInSecondFoder = len(files)  # Узнаем длину(количество файлов в папке)
        countCopyProcent = 0  # подсчёт в процентах сколько осталось
        countAddOneProcent = 100 / lenFilesInFirstFoder  # 100% делим на кол-во, чтобы узнать, сколько осталось
        for file in files:
            print(str('copy File: ' + file + ' From :' + path2 + '/' + file))  # вывод какой файл копируется и откуда
            countCopyProcent += countAddOneProcent  # добавления процентный доли
            print('Progress : ', round(countCopyProcent), '%')  # прогресс в %
            if proverkaImages == True:
                if poverca(os.getcwd() + '\\' + nameFolder, os.getcwd() + '\\' + path2 + '\\' + str(file)) == False:
                     shutil.copy2(os.getcwd() + '\\' + path2 + '\\' + str(file), os.getcwd() + '\\' + nameFolder + '\\' +'Copy2'+ str(file))  # копирование в новую папку слияния
            else:
                     shutil.copy2(os.getcwd() + '\\' + path2 + '\\' + str(file),
                             os.getcwd() + '\\' + nameFolder + '\\' + 'Copy2' + str(
                                 file))  # копирование в новую папку слияния

    print(os.getcwd() + '\\' + nameFolder)
    myLibFiles.renameFiles()  # вызываю метод из класса, который изменяет имя файла, чтобы было всё по порядку

    print(lenFilesInFirstFoder, lenFilesInSecondFoder)


def ImageСomparison(path1, path2, precisionDifference=20,printInfo=False):
    '''
    сравнение картинок
    !Указывать полный путь к картинке, включая саму картинку и её расширение path/images.jpg
    :param path1:
    :param path2:
    :param precisionDifference: точность различия в 20 %
    :return:
    '''
    # сравнение начинается с размера файлов
    image1Size = int(os.path.getsize(path1))  # размер 1-го файла
    image2Size = int(os.path.getsize(path2))  # размер 2-го файла
    if image1Size / image2Size > 1.5 or image2Size / image1Size > 1.5:
        return False
    # 2 сравнение расматриваются массив пикселей изображения 10 000
    percentageOfSimilarity = 0  # процент сходства, чем он выше, тем изображения более похожи
    img1 = Image.open(path1)  # загрузка 1-го изображения
    img2 = Image.open(path2)  # загрузка 2-го изображения
    arr1 = np.asarray(img1, dtype='uint8')  # перобразование изображения 1-го в пиксели
    arr2 = np.asarray(img2, dtype='uint8')  # перобразование изображения 2-го в пиксели
    '''
     если длина пикселей такая же, то это наводит на вывод, что изображения, как минимум имеют одинаковое разрешение
    '''
    if len(arr1) == len(arr2):
        countDiferent = -2
    else:
        countDiferent = 1
    # 3 сравнение расматриваются пиксели изображения, если разница больше 10 000
    if np.array_equal(arr1,
                      arr2): return True  # если всё равны пиксели, то значит и изображения одинаковые. Воспользовался встроеной ф-ей в  numpy
    '''Значение истинности массива с более чем одним элементом неоднозначно(3-х мерный массив). Нужно использовать a.any() или a.all()'''
    # print(arr[0][0][0], arr[0][0][1], arr[0][0][2]) # вывести  значения пикселя arr[0][0][0](R) arr[0][0][1](G) arr[0][0][1](B)
    n1 = len(arr1)  # узнаём кол-во столбиков у 1-го
    n2 = len(arr2)  # узнаём кол-во столбиков у 2-го
    j1 = len(arr1[0])  # кол-во строк у 1-го
    j2 = len(arr2[0])  # кол-во строк у 2-го

    # сравнение будет происходить по наименьшему значению
    # тем самым обрежим наибольшую картинку, так как если этого не сделать, то у нас вылезет ошибка, так как сравнение пикселя с не сущ. пикселем не возможно
    globalN = 0
    if n1 > n2:
        globalN = n2  # если 1 больше значит сравнения по второму
    elif n1 < n2:
        globalN = n1
    else:
        globalN = n1
    globalJ = 0
    if j1 > j2:
        globalJ = j2  # если 1 больше значит сравнения по второму
    elif j1 < j2:
        globalJ = j1
    else:
        globalJ = j1
    '''сравнение пикселей будет с помощью треугольного способа 
[0 0]
[1 0] [1 1]
[2 0] [2 1] [2 2]
[3 0] [3 1] [3 2] [3 3]
[4 0] [4 1] [4 2] [4 3] [4 4]
[5 0] [5 1] [5 2] [5 3] [5 4] [5 5]
[6 0] [6 1] [6 2] [6 3] [6 4] [6 5] [6 6]
[7 0] [7 1] [7 2] [7 3] [7 4] [7 5] [7 6] [7 7]
[8 0] [8 1] [8 2] [8 3] [8 4] [8 5] [8 6] [8 7] [8 8]
[9 0] [9 1] [9 2] [9 3] [9 4] [9 5] [9 6] [9 7] [9 8] [9 9]
######################
'''
    # обрежем пиксели до квадратного вида
    step = 0  # шаг
    if globalJ > globalN:
        step = globalN  # найдём на
    else:
        step = globalJ
    procentOfSimilarity = 100 / (step * step)  # узнаем сколько будет один процент от числа
    for i in range(0, step):
        for j in range(0, i + 1):
            if printInfo==True: print('Pixel coordinates: [', i, j, ']')
            stringRGB1 = str(int(arr1[i][j][0]) + int(arr1[i][j][1]) + int(arr1[i][j][2]))
            stringRGB2 = str(int(arr2[i][j][0]) + int(arr2[i][j][1]) + int(arr2[i][j][2]))
            if printInfo == True: print(stringRGB1, ' ', 'R= ', int(arr1[i][j][0]), 'G= ', int(arr1[i][j][1]), 'B= ', int(arr1[i][j][2]))
            if printInfo == True: print(stringRGB2, ' ', 'R= ', int(arr2[i][j][0]), 'G= ', int(arr2[i][j][1]), 'B= ', int(arr2[i][j][2]))
            if stringRGB1 != stringRGB2:
                countDiferent += procentOfSimilarity
                if printInfo == True: print(countDiferent)
            if (countDiferent >= precisionDifference): return False
        if printInfo == True: print('Reverse triangle')  # обратный треугольник см. 127 строчку
        for i in range(0, step):
            for j in range(0, i):
                if printInfo == True:  print('Pixel coordinates: [', i, j, ']')
                stringRGB1 = str(int(arr1[i][j][0]) + int(arr1[i][j][1]) + int(arr1[i][j][2]))
                stringRGB2 = str(int(arr2[i][j][0]) + int(arr2[i][j][1]) + int(arr2[i][j][2]))
                if printInfo == True: print(stringRGB1, ' ', 'R= ', int(arr1[i][j][0]), 'G= ', int(arr1[i][j][1]), 'B= ', int(arr1[i][j][2]))
                if printInfo == True: print(stringRGB2, ' ', 'R= ', int(arr2[i][j][0]), 'G= ', int(arr2[i][j][1]), 'B= ', int(arr2[i][j][2]))
                if stringRGB1 != stringRGB2:
                    countDiferent += procentOfSimilarity
                    if printInfo == True: print(countDiferent)
                if (countDiferent >= precisionDifference): return False
    return True

def poverca(pathDerectory,pathToFile):
    '''
    мостик между mergeFoldersWithPictures и ImageСomparison
    :param pathDerectory: путь куда копируются файлы
    :param pathToFile: проверяемый файл
    :return:
    '''
    for root, dirs, files in os.walk(pathDerectory):
        for file in files:
            fullnameList = os.path.join(pathDerectory + '\\' , file)  # склейка путь к файлу с именем
            print(fullnameList,'\n', pathToFile,'\n')
            flag=ImageСomparison(fullnameList,pathToFile)
            if flag==True:
                return True
    return False

mergeFoldersWithPictures(r'downloaded images/Автомобиль',r'downloaded images/Мопед','dd')
#print(ImageСomparison('downloaded images/Автомобиль/0.jpg', 'downloaded images/Автомобиль/2.jpg'))
#print(poverca('downloaded images/Автомобиль', 'downloaded images/Автомобиль/2.jpg'))
