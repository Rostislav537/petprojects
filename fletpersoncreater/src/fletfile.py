from src.usercreate import Character  # Импортируем класс Character из модуля src.usercreate
import flet as ft  # Импортируем библиотеку flet для создания пользовательского интерфейса

def main(page: ft.Page):
    page.title = "Character Generator"  # Устанавливаем заголовок окна
    page.window.width = 800  # Устанавливаем ширину окна
    page.window.height = 600  # Устанавливаем высоту окна
    page.theme_mode = ft.ThemeMode.DARK  # Устанавливаем темную тему для интерфейса

    characters = []  # Создаем пустой список для хранения созданных персонажей
    selected_character = ft.Ref[ft.Text]()  # Создаем ссылку для хранения выбранного персонажа
    selected_index = ft.Ref[int]()  # Создаем ссылку для хранения индекса выбранного персонажа

    def generate_character(e):
        character = Character()  # Создаем новый экземпляр персонажа
        characters.append(character)  # Добавляем персонажа в список
        character_list.controls.append(ft.ListTile(
            title=ft.Text(character.full_name),  # Устанавливаем заголовок элемента списка
            subtitle=ft.Text(character.job),  # Устанавливаем подзаголовок элемента списка
            on_click=lambda e, c=character, idx=len(characters)-1: select_character(c, idx)  # Обработчик клика для выбора персонажа
        ))
        page.update()  # Обновляем интерфейс

    def select_character(character, index):
        selected_character.current.value = str(character)  # Устанавливаем значение выбранного персонажа
        selected_index.current = index  # Устанавливаем индекс выбранного персонажа
        delete_button.visible = True  # Делаем кнопку удаления видимой
        page.update()  # Обновляем интерфейс

    def delete_character(e):
        if selected_index.current is not None:
            characters.pop(selected_index.current)  # Удаляем выбранного персонажа из списка
            character_list.controls.pop(selected_index.current)  # Удаляем элемент списка
            selected_character.current.value = ""  # Очищаем значение выбранного персонажа
            selected_index.current = None  # Очищаем индекс выбранного персонажа
            delete_button.visible = False  # Делаем кнопку удаления невидимой
            page.update()  # Обновляем интерфейс

    generate_button = ft.ElevatedButton(
        text="Generate Character",  # Текст на кнопке
        on_click=generate_character,  # Обработчик клика для генерации персонажа
        icon=ft.icons.PERSON_ADD,  # Иконка на кнопке
        expand=True  # Растягиваем кнопку по ширине
    )

    header = ft.Row(
        [
            ft.Text("Character Generator", scale=2),  # Заголовок приложения
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Выравнивание по центру
    )

    button_bar = ft.Row(
        [
            generate_button,  # Кнопка генерации персонажа
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,  # Равномерное распределение пространства
        expand=True,  # Растягиваем по ширине
        spacing=10,  # Отступы между элементами
    )

    character_list = ft.ListView(expand=True, spacing=5, padding=5, auto_scroll=False)  # Создаем список для отображения персонажей
    selected_character.current = ft.Text()  # Создаем текстовый элемент для отображения выбранного персонажа

    delete_button = ft.ElevatedButton(
        text="Delete Character",  # Текст на кнопке
        on_click=delete_character,  # Обработчик клика для удаления персонажа
        icon=ft.icons.DELETE,  # Иконка на кнопке
        visible=False  # Изначально кнопка невидима
    )

    left_panel = ft.Container(
        content=ft.Column(
            [
                header,  # Заголовок
                button_bar,  # Панель с кнопками
                ft.Container(content=character_list, expand=True, border_radius=30, padding=10),  # Контейнер для списка персонажей
            ],
            expand=True,  # Растягиваем по высоте
            spacing=10,  # Отступы между элементами
            alignment=ft.MainAxisAlignment.START,  # Выравнивание по верху
        ),
        width=350,  # Ширина контейнера
        padding=10,  # Отступы внутри контейнера
        border_radius=30,  # Радиус скругления углов
        bgcolor=ft.colors.GREY_800  # Цвет фона
    )

    right_panel = ft.Container(
        content=ft.Column([selected_character.current, delete_button], expand=True),  # Контейнер для отображения выбранного персонажа и кнопки удаления
        padding=20,  # Отступы внутри контейнера
        expand=True,  # Растягиваем по высоте
        border_radius=30,  # Радиус скругления углов
        bgcolor=ft.colors.GREY_900  # Цвет фона
    )

    page.add(
        ft.Row(
            [
                left_panel,  # Левая панель
                right_panel  # Правая панель
            ],
            expand=True  # Растягиваем по ширине
        )
    )
def run_app():
    ft.app(target=main)