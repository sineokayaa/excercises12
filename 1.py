class Date:
    '''
    A class representing a date with comparison and conversion functionalities.

    Attributes:
        days_lap (list): List of days in leap years.
        days_not_lap (list): List of days in non-leap years.
        months (list): Names of months.
    '''
    days_lap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_not_lap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

    def __init__(self, date):
        day = int(date.split('.')[0])
        month = int(date.split('.')[1])
        year = int(date.split('.')[2])
        if not isinstance(date, str):
            self.__date = None
        checking_year = Date.ch_year(year)
        if checking_year is False:
            print('ошибка')
            self.__date = None
        elif year not in range(1000, 10000) or year != int(year):
            print('ошибка')
            self.__date = None
        elif month not in range(1, 13) or month != int(month):
            print('ошибка')
            self.__date = None
        elif day not in range(1, checking_year[month - 1] + 1) or day != int(day):
            print('ошибка')
            self.__date = None
        else:
            self.__date = date

    def __str__(self):
        if self.__date is None:
            return 'None'
        day = int(self.__date.split('.')[0])
        month = int(self.__date.split('.')[1])
        year = int(self.__date.split('.')[2])
        return f'{day} {Date.months[month - 1]} {year} г.'

    def __repr__(self):
        return str(self.__date)

    @staticmethod
    def ch_year(year):
        '''
        Check if the given year is a leap year and return the corresponding list of days.

        Args:
            year (int): The year to be checked.

        Returns:
            list: List of days based on whether it's a leap year or not.
        '''
        if year not in range(1000, 10000) or year != int(year):
            return False
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = Date.days_lap
        else:
            days = Date.days_not_lap
        return days

    @property
    def date(self):
        day = int(self.__date.split('.')[0])
        month = int(self.__date.split('.')[1])
        year = int(self.__date.split('.')[2])
        return f'{day} {Date.months[month - 1]} {year} г.'

    @date.setter
    def date(self, ptr):
        '''
        Setter method to set the date string.

            Args:
                ptr (str): The date string to be set.
            '''
        day = int(ptr.split('.')[0])
        month = int(ptr.split('.')[1])
        year = int(ptr.split('.')[2])
        if not isinstance(ptr, str):
            self.__date = None
        checking_year = Date.ch_year(year)
        if checking_year is False:
            print('ошибка')
            self.__date = None
        elif year not in range(1000, 10000) or year != int(year):
            print('ошибка')
            self.__date = None
        elif month not in range(1, 13) or month != int(month):
            print('ошибка')
            self.__date = None
        elif day not in range(1, checking_year[month - 1] + 1) or day != int(day):
            print('ошибка')
            self.__date = None
        else:
            self.__date = ptr

    @date.getter
    def date(self):
        '''
        Getter method to retrieve the date string.

        Returns:
            str: The formatted date string.
        '''
        if self.__date is None:
            return None
        day = int(self.__date.split('.')[0])
        month = int(self.__date.split('.')[1])
        year = int(self.__date.split('.')[2])
        return f'{day} {Date.months[month - 1]} {year} г.'

    def to_timestamp(self):
        '''
        Convert the Date object to a Unix timestamp.

        Returns:
            int: Unix timestamp representing the date.
        '''
        SEC_DAY = 60 * 60 * 24
        YEAR_ST = 1970
        count = 0
        end_year = int(self.__date.split('.')[2])
        end_month = int(self.__date.split('.')[1])
        end_day = int(self.__date.split('.')[0])
        for year in range(YEAR_ST, end_year):
            days = Date.ch_year(year)
            for month in range(0, 12):
                count += days[month] * SEC_DAY
        days = Date.ch_year(end_year)
        for month_e in range(0, end_month - 1):
            count += days[month_e] * SEC_DAY
        count += SEC_DAY * (end_day - 1)
        return count

    def __eq__(self, other):
        count_f = Date.to_timestamp(self)
        count_oth = Date.to_timestamp(other)
        if count_f == count_oth:
            return True
        return False

    def __ne__(self, other):
        count_f = Date.to_timestamp(self)
        count_oth = Date.to_timestamp(other)
        if count_f != count_oth:
            return True
        return False

    def __lt__(self, other):
        count_f = Date.to_timestamp(self)
        count_oth = Date.to_timestamp(other)
        if count_f < count_oth:
            return True
        return False

    def __le__(self, other):
        count_f = Date.to_timestamp(self)
        count_oth = Date.to_timestamp(other)
        if count_f <= count_oth:
            return True
        return False

    def __gt__(self, other):
        count_f = Date.to_timestamp(self)
        count_oth = Date.to_timestamp(other)
        if count_f > count_oth:
            return True
        return False

    def __ge__(self, other):
        count_f = Date.to_timestamp(self)
        count_oth = Date.to_timestamp(other)
        if count_f >= count_oth:
            return True
        return False


d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
