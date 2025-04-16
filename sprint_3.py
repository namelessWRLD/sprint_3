import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    # 2. Добавление товара в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Название товара должно быть от 1 до 40 символов!')
        if name not in self.__item_price:
            raise NameError('Такого товара нет в магазине!')
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удаление товара из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Этого товара нет в чеке!')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Общая сумма чека (со скидкой 10%, если >10 товаров)
    def check_amount(self):
        total = 0
        for item in self.__name_items:
            total += self.__item_price[item]
        
        if self.__number_items > 10:
            total *= 0.9  # скидка 10%
        return total

    # 5. НДС для товаров с 20% налогом
    def twenty_percent_tax_calculation(self):
        total = 0
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                total += self.__item_price[item]
        
        # Учитываем скидку, если товаров >10
        if self.__number_items > 10:
            total *= 0.9
        
        return total * 0.2  # 20% от суммы

    # 6. НДС для товаров с 10% налогом
    def ten_percent_tax_calculation(self):
        total = 0
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                total += self.__item_price[item]
        
        if self.__number_items > 10:
            total *= 0.9
        
        return total * 0.1  # 10% от суммы

    # 7. Общий НДС (10% + 20%)
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    # 8. Форматирование номера телефона (+7XXXXXXXXXX)
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Номер должен состоять только из цифр!')
        if len(str(telephone_number)) != 10:
            raise ValueError('Номер должен содержать ровно 10 цифр (без +7)!')
        return f'+7{telephone_number}'
