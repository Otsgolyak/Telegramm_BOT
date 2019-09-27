import os




def images_list():
    directory = 'E:/test_01/Telegramm_BOT/file_import'

    # Получаем список файлов в переменную files
    files = os.listdir(directory)

    list_images = []

    # Фильтруем список
    images = filter(lambda x: x.endswith('.jpg'), files)
    for i in images:
        list_images.append(i)
    csv_s = filter(lambda x: x.endswith('.xlsx'), files)
    for i in csv_s:
        continue
    return list_images

