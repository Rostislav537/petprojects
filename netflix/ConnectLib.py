from requests import *
class Connection:   #библиотека отвечающая за запросы
    def __init__(self, API_key):
        self.api_key=API_key
        self.results=None
    def playing_now(self, page):
        url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={self.api_key}&page={page}'
        respone=get(url).json()["results"]
        in_exit=[]
        for i in range(len(respone)):   #цикл записывает информацию о всех фильмах
            dict_={"title":respone[i]["title"],
                   "overview":respone[i]["overview"],
                   "posterpath":respone[i]["poster_path"],
                   "popularity":respone[i]["popularity"],
                   "release_date":respone[i]["release_date"],
                   "vote_average":respone[i]["vote_average"],
                   "id":respone[i]["id"]
                   }
            in_exit.append(dict_)
            self.results = get(url).json()["total_pages"]
        return in_exit
    def get_most_populared(self, page, genre):  #деф который возвращает страницу с 20 самыми популярными фильмами
        url=f'https://api.themoviedb.org/3/discover/movie?&language=ru&sort_by=popularity.desc&api_key={self.api_key}&page={page}&with_genres={genre}'
        respone=get(url).json()["results"]
        in_exit=[]
        for i in range(len(respone)):   #цикл записывает информацию о всех фильмах
            dict_={"title":respone[i]["title"],
                   "overview":respone[i]["overview"],
                   "posterpath":respone[i]["poster_path"],
                   "popularity":respone[i]["popularity"],
                   "release_date":respone[i]["release_date"],
                   "vote_average":respone[i]["vote_average"],
                   "id":respone[i]["id"]
                   }
            in_exit.append(dict_)
            self.results = get(url).json()["total_pages"]
        return in_exit
    def search_film(self, text, page):  #деф который ищет фильм
        url=f"https://api.themoviedb.org/3/search/movie?query={text}&api_key={self.api_key}&language=ru&page={page}"
        respone=get(url).json()["results"]
        in_exit=[]
        for i in range(len(respone)):
            dict_={"title":respone[i]["title"],
                   "overview":respone[i]["overview"],
                   "posterpath":respone[i]["poster_path"],
                   "popularity":respone[i]["popularity"],
                   "release_date":respone[i]["release_date"],
                   "vote_average":respone[i]["vote_average"],
                   "id":respone[i]["id"]
                   }
            self.results=get(url).json()["total_pages"]
            in_exit.append(dict_)
        return in_exit
    def get_poster(self, path):     #деф который возвращает изображение по постерпачу
        return get(f"https://image.tmdb.org/t/p/w185/{path}")
    def get_genre_list(self):   #деф который возвращает список со всеми жанрами и их айди
        url=f'https://api.themoviedb.org/3/genre/movie/list?language=ru&api_key={self.api_key}'
        return get(url).json()['genres']
    def get_pages(self):
        return self.results


