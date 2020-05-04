# instance method - klassenabhängig
# static method - klassenunabhängig
# class method - verändert Zustand einer Klasse (Bsp.: 2ter Konstruktor)

from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # instance method 
    def print_date(self):
        print('{} {} {}'.format(self.year, self.month, self.day))

    # class method - verändert den Zustand der Klasse (quasi neuer Konstruktor) 
    # - > (bekommt kein self) -> sondern cls -> übergibt die Klasse selbst
    @classmethod
    def get_todays_date(cls):
        date = cls.__new__(cls) # leere Hülle der Klasse also ohne Werte für Jahr, Monat, Tag
        time = localtime()
        date.year = time.tm_year
        date.month = time.tm_mon
        date.day = time.tm_mday
        return date

    # static method -> bekommt kein self, da Instanzunabhängig
    @staticmethod
    def is_todays_date(year, month, day):
        time = localtime()
        if year == time.tm_year and month == time.tm_mon and day == time.tm_mday:
            return True
        else:
            return False


# Aufruf instance method
date1 = Date(2008, 10, 8)
date1.print_date()

# Aufruf class method
date2 = Date.get_todays_date()
date2.print_date()

# Aufruf static method
date3 = Date.is_todays_date(2015, 20, 4)
print(date3)