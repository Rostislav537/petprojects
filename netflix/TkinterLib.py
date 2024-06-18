from  tkinter import *
from tkinter.ttk import Combobox
import LibForSpecialFuncs
import MyFilmsLib
class Visual:   #библиотека отвечающая за визуал
    def __init__(self, root, API):
        self.root=root  #окно
        self.page=1     #страница для библиотека подключения
        self.SpFunc=LibForSpecialFuncs.SpecialLib(API)  #библиотека с подключение и другими функциями
        self.elements=[]    #сдесь хранять постеры и описание для последующего уничтожения и добавления их
        self.genre=StringVar()  #стрингвар для комбобокса с жанром
        self.genres_dict=self.SpFunc.get_genres_list()  #список жанров
        self.films=MyFilmsLib.Library_()
        self.buttones=[]

    def load_genre(self):   #вспомогающий деф для получения id жанра
        id_=""
        if self.genre.get()=="Популярные":  #Популярные - это базовая страница которая открываеться при запуске
            id_=None
        else:
            for elementus in self.genres_dict:
                if elementus["name"] == self.genre.get():   #поиск выбраного айди по названию жанра
                    id_=elementus["id"]
        return id_


    def load_films(self, parent, type="standart", text=None):   #деф который загружает страницу(тоесть постер и описание)
        def add_to_lib(x, info):
            self.buttones[x].configure(text="Убрать\n с библиотеки", command=lambda x=x, info=info:remove_from_lib(x, info))
            self.films.write_film(info)
        def remove_from_lib(x, info):
            self.buttones[x].configure(text="Добавить\n в библиотеку", command=lambda x=x, info=info:add_to_lib(x, info))
            self.films.remove_film(info)

        def movie_info(event, info_, index):  #деф который открывает иноформацию о фильме по дабл клику по постеру
            def add_movie():    #деф для добавления фильма в библиотеку
                btn_add_to_lib.configure(text="Убрать с библиотеки", command=remove_movie)
                add_to_lib(index, info_)

            def remove_movie():     #деф для удаления фильма из библиотеки
                btn_add_to_lib.configure(text="Добавить в библиотеку", command=add_movie)
                remove_from_lib(index, info_)

            #создаём окно с информацией
            nwin=Toplevel()
            nwin['bg']="orange"
            nwin.title("Movie info")
            nwin.geometry("525x500")

            #проверка на правильность постерпача(он может быть 'null')
            try:
                poster=self.SpFunc.get_poster_label(nwin, info_["posterpath"])

            except:
                poster=Label(nwin, text="Не удалось загрузить постер.", bg='grey')#на случай если постерпач null

            poster.pack()

            #лэйбла с инфой о фильме
            Info_Label=Label(nwin, wraplength=500, bg="grey", text=f"""{info_['title']}\n{info_['overview']}\nРейнтинг{info_['popularity']}\nВышел {info_["release_date"]}\nОценка критиков:{info_["vote_average"]}""")
            Info_Label.pack()

            if self.films.isinlib(info_):   #проверка есть ли фильм в библиотеке
                btn_add_to_lib = Button(nwin, bg="grey", text="Убрать\n с библиотеки",
                                        command=remove_movie)
            else:
                btn_add_to_lib = Button(nwin, bg="grey", text="Добавить\n в библиотеку",
                                        command=add_movie)
            btn_add_to_lib.pack()


        if type == "search":    #проверка на тип запроса(поиск, обычный)a

            dict_with_information = self.SpFunc.search_film(text, self.page) #получаем информацию по поиску
        elif type == "lib":
            dict_with_information = self.films.my_lib()

        elif self.genre=="Смотрят Сейчас":
            dict_with_information = self.SpFunc.now_playing(self.page)
        else:
            dict_with_information = self.SpFunc.get_most_populared(self.page, self.load_genre()) #получаем информацию по жанру, странице


        for element in self.elements:     #уничтожаем все постеры и описания на предыдущей странице
            element.destroy()
        for element in self.buttones:
            element.destroy()
        self.elements.clear()   #чистим список с постерами и описаниями
        self.buttones=[]

        for i in range(len(dict_with_information)): #заполняем страницу информацией из запроса
            try:    #проверка на правильность постера

                #постер
                lable_LEFT=self.SpFunc.get_poster_label(parent, dict_with_information[i]["posterpath"])     #получаем постер
                lable_LEFT['text']=i    #делам текст постера как индекс для последующего использования(в окне с информацией о фильме)

            except:     #тоже самое но без постера
                lable_LEFT=Label(parent, text=i, bg='grey')


            # описание фильма
            overviewLabel=Label(parent, bg="grey", wraplength=300, text=f"{dict_with_information[i]['title']}\n{dict_with_information[i]['overview']}")

            if self.films.isinlib(dict_with_information[i]):
                btn_add_to_lib = Button(parent, bg="grey", text="Убрать\n с библиотеки",
                                        command=lambda x=i, info=dict_with_information[i]: remove_from_lib(x, dict(info)))
            else:
                btn_add_to_lib = Button(parent, bg="grey", text="Добавить\n в библиотеку",
                                        command=lambda x=i, info=dict_with_information[i]: add_to_lib(x, dict(info)))

     # добавляем постер и описание в список
            self.buttones.append(btn_add_to_lib)
            self.elements.append(btn_add_to_lib)
            self.elements.append(lable_LEFT)
            self.elements.append(overviewLabel)



            btn_add_to_lib.grid(column=3, row=i+2, sticky='news')
            lable_LEFT.grid(column=1, row=i + 2, sticky='news')
            overviewLabel.grid(column=2, row=i + 2, sticky='news')



            #биндим постер для открытия информации о фильме
            lable_LEFT.bind("<Double-Button-1>", lambda event, info=dict_with_information[i]:movie_info(event, info, i))

            print(i*5+5,"%")    #что-то типа прогрессбара
        if not len(dict_with_information)==0:
            self.results=dict_with_information[-1]

    def take_rootmenu(self):    #деф которыйоформляет визуал
        def theme_change(event): #деф который меняет тему
            if theme.get()=="black":
                lbl_t["fg"]="white"
            else:
                lbl_t["fg"] = "black"
            self.root["bg"]=theme.get()
            lbl_t["bg"]=theme.get()
            canvas_other["bg"]=theme.get()
        def click_num_button(parent, n):#деф который происходит по нажатию на кнопку с цифрой
            self.page = n
            self.load_films(parent)
            for element in buttons:
                element.destroy()
            buttones()

        def config_canavas():   #этот деф нужен чтобы обновлять длину канваса и тем самым обновлять дальность прокрутки скроллбара

            frame_labels.update_idletasks()
            canvas.configure(yscrollcommand=vsb.set)
            canvas.config(scrollregion=canvas.bbox("all"))

        def search_film(event):     #вспомогающий деф по которому осуществляиться поиск фильма
            #временно уничтожаем кнопки страниц так как при запросе на поиск страницы не нужны

            btn_canvas.grid_forget()

            for element in buttons:
                element.destroy()

            #тоже самое делаем с комбобоксом
            cmb['state']="disable"

            #гридим кнопку возвращения назад
            btn_comeback.grid(row=3, column=0, columnspan=2)

            #вызываем дефы обновления канваса и страницы
            self.load_films(frame_labels,"search", search.get())
            config_canavas()


        def new_genre(event):   # Вспомогающий деф которы меняет жанр

            self.page=1
            self.load_films(frame_labels)
            buttones()
        def back_page():    #деф которые перелистывает страницу

            if self.page != 1:      #деф которые перелистывает страницу
                self.page -= 1
                self.load_films(frame_labels)

            buttones()
        def next_page():    #деф которые перелистывает страницу
            if self.page!=self.results:
                self.page += 1
                self.load_films(frame_labels)
                buttones()
        def comeback():     #деф который возвращает от поиска к просматреваемой странице

            cmb['state'] = "readonly"

            btn_comeback.grid_forget()

            search["state"]=NORMAL


            btn_canvas.grid(row=3, columnspan=2, column=0)

            lib_button['state'] = NORMAL

            self.load_films(frame_labels)

            buttones()

            config_canavas()
        def buttones(): #деф который создает кнопки с цифрами
            global next_grid

            nums=[] #список в котором будет номера кнопок

            self.results=self.SpFunc.get_pages()

            if self.results>500:#проверка на кол-во результатов, больше 500 стпаницы листать нельзя
                self.results=500

            #дальше идут проверки после которых заполнится список с номерами кнопок
            if self.page>=3 and self.page<self.results-3:
                nums = [1, self.page - 2, self.page - 1, self.page, self.page + 1, self.page + 2, self.results]
                next_grid=6

            elif self.page<3 and self.results>4:
                nums = [1 ,2 ,3 ,4 ,5 , self.results]
                next_grid=5

            elif self.page<3 and self.results<4:
                print(self.results)
                nums=[i+1 for i in range(self.results)]
                next_grid=self.results-1

            elif self.page>self.results-3:
                nums=[1, self.results-4,self.results-3, self.results-2, self.results-1, self.page]
                next_grid=5

            buttons.clear()     #очищаем список с самими кнопками

            for i in range(len(nums)):      #создаем кнопки

                if nums[i]==self.page:
                    buttons.append(Button(btn_canvas,bg="grey",  state=DISABLED,text=nums[i],command=lambda x=nums[i]: click_num_button(frame_labels, x)))
                else:
                    buttons.append(Button(btn_canvas,bg="grey", text=nums[i],command=lambda x=nums[i]: click_num_button(frame_labels, x)))

            for i in range(len(buttons)):
                buttons[i].grid(row=0, column=i)

            btn_next.grid(row=2, column=next_grid)
        def lib_my():   #деф нужен для того чтобы попасть на страницу с библиотекой
            btn_canvas.grid_forget()

            cmb['state']="disable"

            search["state"]="disable"

            #гридим кнопку возвращения назад
            btn_comeback.grid(row=3, column=0, columnspan=2)
            lib_button['state']=DISABLED
            #вызываем дефы обновления канваса и страницы
            self.load_films(frame_labels, "lib")
            config_canavas()

            buttones()


        self.root["bg"]="orange"    #оформляем главное окно
        self.root.title("Sretflix")
        self.root.geometry("600x800")
        lbl_t=Label(text="Sretflix", bg="orange", font=("Comic Sans MS", 90))   #лэйбла с названием
        lbl_t.grid(row=0, column=0, columnspan=3)
        buttons=[]



        genres_name=["Популярные", "Смотрят Сейчас"]  #создаем список с жанрами

        for element in self.genres_dict:    #добавляем жанры в список
            genres_name.append(element["name"])


        self.genre.set(genres_name[0])

        canvas_other=Canvas()   #канвас на котором распологаются жанр, поиск, и тд

        cmb=Combobox(canvas_other, values=genres_name, textvariable=self.genre, state="readonly")     #комбобокс для выбора жанра
        cmb.grid(row=0, column=0)


        search=Entry(canvas_other)      #поле для поиска
        search.grid(row=0, column=1)

        search.bind("<Return>", search_film)

        lib_button=Button(canvas_other, text="Моя библиотека", bg='grey', command=lib_my)    #кнопка для попадения в библиотеку
        lib_button.grid(column=2, row=0)

        canvas_other['bg']='orange'
        canvas_other.grid(row=1, columnspan=2, column=0)


        #самая муторная часть - скроллбар
        frame_main = Frame(self.root, bg="gray")    #основной фрейм на котором расположаться еще один фрейм с канвасом
        frame_main.grid(columnspan=3, sticky='news')

        frame_canvas = Frame(frame_main)    #фрейм для канваса
        frame_canvas.grid(row=2, column=0,columnspan=3, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)

        frame_canvas.grid_propagate(False)
        canvas = Canvas(frame_canvas, bg="grey")    #канвас
        canvas.grid(row=0, column=0, sticky="news", columnspan=3)

        vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)  #сам скроллбар
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        frame_labels = Frame(canvas, bg="orange")       #фрейм для постеров и описаний
        canvas.create_window((0, 0), window=frame_labels, anchor='nw')      #эта строка самая основная без неё ничего бы не работало

        self.load_films(frame_labels)   #заполняем фрейм


        config_canavas()


        frame_canvas.config(width=580 + vsb.winfo_width(),
                            height=500)

        #без всех этих процедур скролбар у меня просто не работал

        btn_canvas=Canvas(bg="grey")
        btn_canvas.grid(row=3, columnspan=6, column=0)

        btn_back=Button(btn_canvas, text="Назад", bg="grey", command=back_page)     #страница назад
        btn_back.grid(row=2, column=0)

        btn_next = Button(btn_canvas, text="Вперед", bg="grey", command=next_page)  # страница вперед

        buttons=[]

        buttones()


        cmb.bind("<<ComboboxSelected>>", new_genre)     #биндим комбобокс на смену жанра


        btn_comeback=Button(text="Назад", bg="grey", command=comeback)  #кнопка возвращения к основной странице

        theme=StringVar(value="orange")

        themes=["white", "orange", "red", "black"]

        teheme_cmb=Combobox(canvas_other, values=themes, textvariable=theme, state="readonly")      #комбобокс с темой
        teheme_cmb.bind("<<ComboboxSelected>>", theme_change)

        teheme_cmb.grid(column=3, row=0)
