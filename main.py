import requests  # библиотека/пакет  для работы c URL адресами
from PIL import Image, ImageFilter  # библиотека/пакет  для работы с изображениями
import numpy as np


# url = 'https://httpbin.org/get'
# url_2 = 'https://www.youtube.ru/results' # URL youtube
# query = {'search_query': 'mister bin'} # запрос по ключу и значению
# response = requests.get(url_2, params=query) # вызов get c добавлением параметра (запроса)
# print(response.headers, 'headers')
# print(response.status_code, 'status_code')
# print(response.url, 'url')
# print(response.content,'content')
# print(response.text,'text')
# print(response.json(), 'json')

# image_1 = Image.open('image_1.jpg')
# image_2 = Image.open('image_2.jpg')
# with Image.open('image_2.jpg') as img: # работа с пиксилями
#     px = img.load() #загружаем пиксель
#     print(px[4,4])
#     px[4,4]=(0,0,0) # изменяем его
#     print(px[4,4])
# img = image_1.filter(ImageFilter.EDGE_ENHANCE)  # накладываем фильтр и придаем четкость изображению
# img_2 = image_2.filter(ImageFilter.EDGE_ENHANCE)
#
# img.save('img.jpg')  # сохраняем файл
# img_2.save('img_2.jpg')

data = [[1,23,34],[43,56,56],[23,543,4]] # передаем список вложенных списков для использование библиотеке numpy
arr = np.array(data)# создаем массив (array)
arr_2 = np.arange(2,2000,2)
print(arr)
print(arr.size) # принтуем размер(size) массива
print(arr.shape)# принтуем форму (shape)
print(arr.ndim)# принтуем n-мерность массива
print(arr.dtype)
print(arr_2)
print(arr_2.size) # принтуем размер(size) массива
print(arr_2.shape)# принтуем форму (shape)
print(arr_2.ndim)# принтуем n-мерность массива
print(arr_2.dtype)