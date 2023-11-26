from PIL import Image


class Filter:
    """
    Базовый класс для создания фильтров
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        """
        Применяет фильтр к одному пикселю
        :param pixel: цвет пикселя
        :return: новый цвет пикселя
        """
        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: исходное изображение
        :return: новое изображение
        """
        new_img = Image.new("RGB", img.size)
        for i in range(img.width):
            for j in range(img.height):
                # получаем цвет
                r, g, b = img.getpixel((i, j))

                # применяем фильтр к пикселю
                new_pixel = self.apply_to_pixel((r, g, b))

                # сохраняем пиксель обратно
                new_img.putpixel((i, j), new_pixel)
        return new_img


class BrightFilter(Filter):
    """
    Фильтр, который делает изображение ярче.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel

        r = min(r + 50, 255)
        g = min(g + 50, 255)
        b = min(b + 50, 255)

        return r, g, b


class DarkFilter(Filter):
    """
    Фильтр, который делает изображение темнее.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel

        r = max(r - 50, 0)
        g = max(g - 50, 0)
        b = max(b - 50, 0)

        return r, g, b


class InverseFilter(Filter):
    """
    Фильтр, который инвертирует изображение.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel

        r = 255 - r
        g = 255 - g
        b = 255 - b

        return r, g, b


class GreenFilter(Filter):
    """
    Фильтр, который делает зеленее изображение.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel

        r = min(r + 50, 255)
        g = min(g + 200, 255)
        b = min(b + 50, 255)

        return r, g, b


class BlueFilter(Filter):
    """
    Фильтр, который делает синее изображение.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel

        r = min(r + 50, 255)
        g = min(g + 50, 255)
        b = min(b + 150, 255)

        return r, g, b


class RedFilter(Filter):
    """
    Фильтр, который делает краснее изображение.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel

        r = min(r + 150, 255)
        g = min(g + 50, 255)
        b = min(b + 50, 255)

        return r, g, b


def main():
    img = Image.open()

    bright_filter = BrightFilter()
    img = bright_filter.apply_to_image(img)

    dark_filter = DarkFilter()
    img = dark_filter.apply_to_image(img)

    inverse_filter = InverseFilter()
    img = inverse_filter.apply_to_image(img)

    green_filter = GreenFilter()
    img = green_filter.apply_to_image(img)

    blue_filter = BlueFilter()
    img = blue_filter.apply_to_image(img)

    red_filter = RedFilter()
    img = red_filter.apply_to_image(img)

    img.show()


if __name__ == "__main__":
    main()
