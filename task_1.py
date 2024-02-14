if __name__ == "__main__":
    # ДОКУМЕНТАЦИЯ
    # Для подкласса Легковые автомобили был перезагружен
    # метод "Фильтр года" (year_filter): покупателям легковых авто не предлагаются слишком старые модели.
    # Для подкласса Грузовые автомобили был перезагружен метод
    # "Фильтр марки" (brand_filter): в предполагаемой базе данных грузовые авто имеют свой порядковый номер.
    # Инкапсулированы атрибуты brand (марка авто) и year (год выпуска), так как для любого автомобиля они
    # остаются неизменными. Цена и масса авто могут меняться в течение времени, поэтому атрибуты price и
    # mass не инкапсулированы.
    pass

class Cars:
    """
    Создание и подготовка к работе базового класса автомобили.

    """
    def __init__(self, brand: str, year: int):
        self._brand = brand
        self._year = year
    """ 
    param brand: Марка автомобиля
        param year: Год выпуска автомобиля
        Данные атрибуты для любого автомобиля
        остаются неизменными, поэтому они 
        инкапсулированы
        
    """

    def __str__(self):
        return f"Автомобиль {self._brand}. Год выпуска: {self._year}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self._brand!r}, year={self._year!r})"

    """ 
    Реализация магических методов __str__ и __repr__
    
    """

    def __year_filter__(self, year: int):
        if not isinstance(year, int):
            raise TypeError

        """
         Метод: фильтр, проверяющий соответствие типа данных для атрибута year - фильтр года
         
        """

    def __brand_filter__(self, brand: str):
        if not isinstance(brand, str):
            raise TypeError

    """ 
    Метод: фильтр, проверяющий соответствие типа данных для атрибута brand - фильтр марки
    
    """

class Pas_cars(Cars):
    """ Создание и подготовка к работе дочернего класса легковые автомобили. """

    def __init__(self, brand: str, year: int, price: int):
        super().__init__(brand, year)
        super().__brand_filter__(brand)
        self.price = price
        if not isinstance(price, int):
             raise TypeError
        if not 200000 <= price <= 10000000:
            raise ValueError

        """
         Все методы, кроме фильтра года выпуска, унаследованы
         
        """

    def __year_filter__(self, year: int):
        super().__year_filter__(year)
        if year <= 1990:
            raise ValueError

        """
         Метод фильтр года перезагружен, так как покупателям легковых авто не предлагаются слишком старые модели
        
        """

    def __str__(self):
        return f"{super().__str__()}. Стоимость автомобиля: {self.price} р"

    def __repr__(self):
         return f"{super().__repr__().replace(')', '')}, price={self.price!r})"


    """
    Перезагрузка магических методов __str__ и __repr__
    
    """

class Truck(Cars):
    """ Создание и подготовка к работе дочернего класса грузовые автомобили. """

    def __init__(self, brand: str, year: int, mass: float):
        super().__init__(brand, year)
        super().__year_filter__(year)
        self.mass = mass
        if not isinstance(mass, float):
             raise TypeError
        if mass <= 0:
            raise ValueError

    """
     Все методы, кроме фильтра марки, унаследованы

    """

    def __brand_filter__(self, brand: str or int):
        if not isinstance(brand, str or int):
            raise TypeError

    """
     Метод фильтр марки перезагружен, так как в предполагаемой базе данных грузовые авто имеют свой порядковый номер
    
    """

    def __str__(self):
        return f"{super().__str__()}. Масса автомобиля: {self.mass} т"

    def __repr__(self):
        return f"{super().__repr__().replace(')', '')}, mass={self.mass!r})"

    """
     Перезагрузка магических методов __str__ и __repr__

    """

    """
     Атрибуты цена и масса авто могут меняться в течение времени, поэтому атрибуты price и
     mass не инкапсулированы.
    
    """

print(Cars("Москвич", 1991))
print(Pas_cars("Toyota", 2022, 5000000))
print(Truck("Камаз", 2001, 18.3))

"""
Вывод результатов
"""