# FFmpeg
# AuthorBooksComments

## Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
* FFmpeg
  
___
## Тестовое задание

* Программа выполняется из командной строки (желательно linux).
  * Программе передается единственный аргумент, а именно путь до папки (к примеру /tmp/test).
  * В папке могут находится секвенции из jpg файлов (последовательность картинок по типу img_0001.jpg, img_0002.jpg и т.д), так и подпапки. В которых в свою очередь так же могут быть как секвенции так и подпапки. Вложенность не ограничена (не известна).
  * Требуется пройтись по всем вложенным папкам включая указанную, получить все секвенции и используя ffmpeg собрать их в видео файлы (кодек mjpeg, контейнер mov)
  * Полученные видео файлы сложить в папку которую мы передали как аргумент.

  * Реализовать возможность оставлять от имени автора комментарий к книгам.
  * В сущность книги обязательно добавить флаг Archived, заархированные книги не выводить в публичной части.
  * Выходной файл должен быть mov с кодеком mjpeg, 24 кадра в в секунду. Разрешение и качество не меняем. 
    
___

### Home 

![image](https://github.com/budennovsk/FFmpeg/assets/97764479/993d99b2-6ec7-4a3b-b7c2-9792105e89c9)


____

### Запуск проекта

* Перейти в корень проекта
* Запустить файл main.py

