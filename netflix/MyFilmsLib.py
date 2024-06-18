import csv
class Library_:     #библиотека в которой хранятся сохранённые фильмы
    def __init__(self):
        self.names_=[]
        with open("Films.csv", "r") as csvfile:     #открываем файл с сохранением и читаем
            reader = csv.DictReader(csvfile)
            self.films=list(reader)
            for element in self.films:
                self.names_.append(element["title"])
    def my_lib(self):   #деф который возвращает библиотеку
        return self.films
    def write_film(self, filminformation):  #деф который записывает фильм в файл
        self.films.append(dict(filminformation))
        self.names_.append(dict(filminformation)["title"])
        with open("Films.csv", "w") as csvfile:
            names=list(filminformation.keys())
            writer=csv.DictWriter(csvfile, fieldnames=names)
            writer.writeheader()
            writer.writerows(self.films)
    def remove_film(self, filminformation):     #деф который убирает фильм из файла
        for element in self.films:
            if element["title"]==filminformation["title"]:
                self.films.remove(element)
        self.names_.remove(dict(filminformation)["title"])
        with open("Films.csv", "w") as csvfile:
            names=list(filminformation.keys())
            writer=csv.DictWriter(csvfile, fieldnames=names)
            writer.writeheader()
            writer.writerows(self.films)
    def isinlib(self, element):     #деф который провиряет есть ли фильм в библиотеке
        print(dict(element)["title"])
        if dict(element)["title"] in self.names_:
            return True
        else:
            return False