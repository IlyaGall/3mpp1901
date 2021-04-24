import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = 'E:/диплом/диплом фотографии/L1-L2/obj'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('E:/диплом/диплом фотографии/L1-L2/data/train.txt', 'w') # путь где находится файл в который будет записанны файлы для тренировки
file_test = open('E:/диплом/диплом фотографии/L1-L2/data/test.txt', 'w') #  путь где находится файл в который будет записанны файлы для теста

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write("obj" + "/" + title + '.jpg' + "\n") # использование облако, поэтому такой адрес записи
    else:
        file_train.write("obj" + "/" + title + '.jpg' + "\n") # использование облако, поэтому такой адрес записи
        counter = counter + 1