import os
import re
import ffmpeg

# директория тестового задания
path_directory = 'E:\TEST'
# глубина паддинга
padding = 4


def get_sequence():
    """ Функция для получения имени файлов и пути"""
    c = 0
    for root, dirs, files in os.walk(path_directory):
        for file in files:
            # условие №1, находим нужную папку по количеству секвенций в имени 4 и расширением jpg
            if file.endswith('.jpg') and len(re.split("_|.jpg", file)[-2]) == padding:
                return root, file


def write_txt():
    # получаем имя секвенции папки с файлами
    name = get_sequence()[1].split('_')
    # путь получается: file 'E:\TEST\sea\burn\burn_%04d.jpg'
    filelist = f"file '{get_sequence()[0]}\\{name[0]}_%0{padding}d.jpg'"

    # записываем в тексовый редактор, так как возможно условие создание более 1 видео
    with open('filelist.txt', "w") as filesToProcess:
        filesToProcess.write(filelist)


def save():
    # имя файла сохраняем для output
    name_out = get_sequence()[1].split('.')

    ff_output_filename = f"{name_out[0]}.mp4"
    (
        ffmpeg
        .input('filelist.txt', format='concat', safe=0)
        .output(ff_output_filename).run()
    )


if __name__ == '__main__':
    get_sequence()
    write_txt()
    save()
