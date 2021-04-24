import os
import shutil# для копирования файлов
class bilder:
    def __init__(self, nameFolder):
        self.nameFolder=nameFolder;

    def bildFolder(self, boolLookdirectory=False, boolLookErrorBuldFolder=False, boolLookBuldFolder=False):
            """
            создаёт новую папку в корне
            :param nameFolder: имя новой папки
            :param boolLookdirectory: вывести в консоль текущий каталог
            :param boolLookErrorBuldFolder:  вывести в консоль ошибку при создании папки
            :param boolLookBuldFolder:  вывести в консоль сообщение о успешном создании папки
            :return: Nope
            """
            nameFolder=self.nameFolder;
            path = os.getcwd()  # определяем текущий каталог и печатаем
            if boolLookdirectory: print("Текущая рабочая директория %s" % path)
            path += r'/' + str(nameFolder)
            try:
                os.mkdir(path)  # создание папки
            except OSError:
                if boolLookErrorBuldFolder: print("Создать директорию %s не удалось" % path)
            else:
                if boolLookBuldFolder: print("Успешно создана директория %s " % path)

    def bildFolderInDerectory (self,  boolLookErrorBuldFolder=False, boolLookBuldFolder=False):
        """
        создаёт новую папку по указаному пути
        :param nameFolder: имя новой папки
        :param boolLookdirectory: вывести в консоль текущий каталог
        :param boolLookErrorBuldFolder:  вывести в консоль ошибку при создании папки
        :param boolLookBuldFolder:  вывести в консоль сообщение о успешном создании папки
        :return: Nope
        """
        nameFolder = self.nameFolder
        try:
            os.mkdir(nameFolder)  # создание папки
        except OSError:
            if boolLookErrorBuldFolder: print("Создать директорию %s не удалось" % nameFolder)
        else:
            if boolLookBuldFolder: print("Успешно создана директория %s " % nameFolder)

class LibFiles:
    def __init__(self, path):
        self.path=path;

    def renameFiles(self, farmatFiles='.jpg'):
        '''
            переменовывает файлы в числовом порядке, например с RandomName.jpg(farmatFiles) на Number.jpg(farmatFiles)
            eddasd12dsad.jpg на 1.jpg(если конечно он первый)
            :param farmatFeles: формат файлов (по умолчанию jpg)
            :return: None
        '''
        path=self.path

        Mybilder = bilder(path + r'\temp')  # инцилизация нового класса
        Mybilder.bildFolderInDerectory(True, True)  # создание новой папки+ вывести сообщение об этом
        countImagesReName = 0  # номер нового файла
        for root, dirs, files in os.walk(path):  # перебор файлов в папке
            for fileImage in files:  # перебор файлов в папке
                print('copy file: ', fileImage,
                      ' in folder temp')  # выводит информацию о копировании в новую временную папку
                shutil.copy2(path + '\\' + fileImage, path + r'\temp' + '\\' + str(
                    countImagesReName) + farmatFiles)  # копирование в новую временную папку
                print('Rename file: ', fileImage, 'to ',
                      str(countImagesReName) + farmatFiles)  # выводит информацию о переменовывании файлов
                countImagesReName += 1  # увеличивает переменную имени файлов
            break
        namesFilesImages = os.listdir(
            path)  # получает список файлов, которые есть в указаной папке, !!!ВКЛЮЧАЯ И ПАПКИ!!!
        for namesFilesImage in namesFilesImages:  # перебор списка файлов
            print(namesFilesImage)  # вывод информации о найденом файле
            fullname = os.path.join(path, namesFilesImage)  # склейка путь к файлу с именем
            if os.path.isfile(fullname):  # проверка фаил ли это
                print(fullname)  # вывод имени файла
                os.remove(fullname)  # удаляет файлы из корневого каторога задавалось path
        '''теперь перекидываем файлы из временой папки temp в корень path'''
        namesFilesImages = os.listdir(
            path + '\\' + 'temp')  # получает список файлов, которые есть в указаной папке, !!!ВКЛЮЧАЯ И ПАПКИ!!!
        for namesFilesImage in namesFilesImages:  # перебор списка файлов
            print(namesFilesImage)  # вывод информации о найденом файле
            fullname = os.path.join(path + '\\' + 'temp', namesFilesImage)  # склейка путь к файлу с именем
            if os.path.isfile(fullname):  # проверка фаил ли это
                shutil.copy2(path + r'\temp' + '\\' + namesFilesImage,
                             path + '\\' + namesFilesImage)  # копирование в новую временную папку
                print(fullname)  # вывод имени файла
                os.remove(fullname)  # удаляет файлы из корневого каторога задавалось path
        os.rmdir(path + r'\temp')  # удаляем временный каталог temp