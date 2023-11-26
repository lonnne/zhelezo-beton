from filter import BrightFilter, DarkFilter, InverseFilter, GreenFilter, BlueFilter, RedFilter
from PIL import Image
import os

def main():
    filter_names = ["Увеличить яркость", "Уменьшить яркость", "Инверсия", "Больше зелёного", "Больше синего", "Больше красного"]
    filters = [BrightFilter(), DarkFilter(), InverseFilter(), GreenFilter(), BlueFilter(), RedFilter()]
    filter_description = {
        0: "Увеличивает яркость на изображение",
        1: "Уменьшает яркость на изображение",
        2: "Инверсирует изображение",
        3: "Делает зеленее изображение",
        4: "Делает синее изображение",
        5: "Делает краснее изображение"
    }


    print("Добро пожаловать в консольный фоторедактор.")
    is_finished = False
    while not is_finished:
        # спрашиваем путь к файлу
        path = input("Введите путь к файлу: ")

        # проверяем ввод
        while not os.path.exists(path):
            path = input("Файл не найден. Попробуйте ещё раз: ")

        img = Image.open(path)

        print("Какой фильтр вы хотите применить?")
        for i in range(len(filter_names)):
            print(f"{i} - {filter_names[i]}")

        # Запрашиваем номер фильтра
        choice = input("Выберите фильтр: ")

        # проверяем ввод
        while not choice.isdigit() or int(choice) >= len(filters):
            choice = input("Неккоректный ввод. Попробуйте ещё раз: ")

        # Выводим описание фильтра
        filter_index = int(choice)
        print(f"Описание выбранного фильтра: {filter_description[filter_index]}")

        # спрашиваем, применить фильтр или вернуться назад
        apply_filter = input("Применить фильтр? (да/нет): ").lower()

        # проверяем ввод
        while apply_filter != "да" and apply_filter != "нет":
            apply_filter = input("Неккоректный ввод. Введите ещё раз: ").lower()

        if apply_filter == "да":

            # применяем фильтр
            selected_filter = filters[int(choice)]
            img = selected_filter.apply_to_image(img)

            # спрашиваем куда сохранить файл
            save_path = input("Куда сохранить: ")

            # Сохраняем
            img.save(save_path)

        # Спрашиваем, хотим ли повторить
        answer = input("Ещё раз? (да/нет): ").lower()

        # проверяем ввод
        while answer != "да" and answer != "нет":
            answer = input("Неккоректный ввод. Введите ещё раз: ").lower()

        is_finished = answer == "нет"

if __name__ == "__main__":
    main()

