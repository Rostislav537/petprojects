from  tkinter import *
import ConnectLib
from io import BytesIO
from PIL import Image, ImageTk
class SpecialLib:   #вспомогательная библиотека которая связывает библиотеки с визуалом и подключением
    def __init__(self, API):
        self.Lib_for_connect=ConnectLib.Connection(API)
    def get_poster_label(self,parent,  posterPath):     #деф который возвращает дэйблу с постерам(на эти 6 строчек я потратил около двух часов)
        lable_LEFT = Label(parent, bg="grey")
        pil_image = Image.open(BytesIO(self.Lib_for_connect.get_poster(posterPath).content))
        image = ImageTk.PhotoImage(pil_image)
        lable_LEFT.config(image=image, text='')
        lable_LEFT.image = image
        return lable_LEFT
    def search_film(self, text, page):      #вспомогающий деф который осуществляет поиск фильма
        return self.Lib_for_connect.search_film(text, page)

    def get_most_populared(self, page, genre):  #вспомогающий деф который возвращает самые популярные фильмы
        return self.Lib_for_connect.get_most_populared(page, genre)
    def get_genres_list(self):  #вспомогающий деф который возвращает список жанров
        return self.Lib_for_connect.get_genre_list()
    def get_pages(self):
        return self.Lib_for_connect.get_pages()-1
    def now_playing(self, page):
        return self.Lib_for_connect.playing_now(page)