class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


print(PaperBook("Стихи", "Есенин", 200))
print(AudioBook("Стихи", "Есенин", 19.4))