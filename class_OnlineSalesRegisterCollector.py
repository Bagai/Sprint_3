import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            "чипсы": 50,
            "кола": 100,
            "печенье": 45,
            "молоко": 55,
            "кефир": 70,
        }
        self.__tax_rate = {
            "чипсы": 20,
            "кола": 20,
            "печенье": 20,
            "молоко": 10,
            "кефир": 10,
        }

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    @property
    def item_price(self):
        return self.__item_price

    @property
    def tax_rate(self):
        return self.__tax_rate

    def add_item_to_cheque(self, name):
        try:
            if 0 < len(name) >= 40:
                raise ValueError(
                    "Нельзя добавить товар, если в его названии нет символов или их больше 40"
                )
            elif name not in self.__item_price:
                raise NameError("Позиция отсутствует в товарном справочнике")
        except ValueError:
            print(
                "Нельзя добавить товар, если в его названии нет символов или их больше 40"
            )
        except NameError:
            print("Позиция отсутствует в товарном справочнике")
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_checke(self, name):
        try:
            if name not in self.__name_items:
                raise NameError("Позиция отсутствует в чеке")
        except NameError:
            print("Позиция отсутствует в чеке")
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for name in self.__name_items:
            total.append(self.__item_price[name])
        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 20:
                twenty_percent_tax.append(name)

        for name in twenty_percent_tax:
            total.append(self.__item_price[name])
        if len(total) > 10:
            return sum(map(lambda x: x * 0.2, total)) * 0.9
        return sum(map(lambda x: x * 0.2, total))

    def ten_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 10:
                twenty_percent_tax.append(name)

        for name in twenty_percent_tax:
            total.append(self.__item_price[name])
        if len(total) > 10:
            return sum(map(lambda x: x * 0.1, total)) * 0.9
        return sum(map(lambda x: x * 0.1, total))

    def total_tax(self):
        return (
            self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        )

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if telephone_number != int(telephone_number):
                raise ValueError("Необходимо ввести цифры")
            elif len(str(telephone_number)) != 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
        except Exception:
            return f'+7{telephone_number}'
        else:
            return f'+7{telephone_number}'

