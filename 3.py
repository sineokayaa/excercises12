class Date:
    '''
    A class representing a date with functionalities for date manipulation and conversion to timestamp.

    Attributes:
        days_lap (list): List of days in each month for leap years.
        days_not_lap (list): List of days in each month for non-leap years.
        months (list): Names of months.
        __date (str): Private attribute to store the date string in 'DD.MM.YYYY' format.
    '''
    days_lap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_not_lap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

    def __init__(self, date):
        '''
        Initialize a Date object with a given date string.

        Args:
            date (str): The date string in 'DD.MM.YYYY' format.
        '''
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
        if self.__date is None:
            return str('None')
        day = int(self.__date.split('.')[0])
        month = int(self.__date.split('.')[1])
        year = int(self.__date.split('.')[2])
        return str(f'{day} {Date.months[month - 1]} {year} г.')

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
        '''
        Getter method to retrieve the date string.

        Returns:
            str: The formatted date string.
        '''
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
        if self.__date == None:
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


class Load:
    '''
    A class responsible for loading data from files and managing user meetings.

    Attributes:
        ppl_meet (dict): A dictionary to store meeting attendees by meeting ID.
    '''
    ppl_meet = {}

    @classmethod
    def write(cls, file_1, file_2, file_3):
        '''
        Load data from files and create User and Meeting objects.

        Args:
            file_1 (str): The filename containing meeting information.
            file_2 (str): The filename containing user information.
            file_3 (str): The filename containing meeting attendee information.
        '''
        with open(file_2, 'r', encoding='utf-8') as prsn:
            lines = prsn.readlines()
            for i in range(1, len(lines)):
                User(lines[i])

        with open(file_3, 'r', encoding='utf-8') as prsn_meet:
            lines = prsn_meet.readlines()
            for i in range(1, len(lines)):
                Load.ppl_meet[lines[i].split(';')[0]] = []

        with open(file_3, 'r', encoding='utf-8') as prsn_meet:
            lines = prsn_meet.readlines()
            for i in range(1, len(lines)):
                Load.ppl_meet[lines[i].split(';')[0]].append(lines[i].split(';')[1])

        with open(file_1, 'r', encoding='utf-8') as meet:
            lines = meet.readlines()
            for i in range(1, len(lines)):
                Meeting(lines[i])


class User:
    '''
    A class representing a user with user details.

    Attributes:
        users (list): A list to store user objects.
        defintns (list): List of user data definitions.
    '''
    users = []
    defintns = ['ID:', 'LOGIN:', 'NAME:', 'GENDER:']

    def __init__(self, ptr_ppl):
        '''
        Initialize a User object with user details.

        Args:
            ptr_ppl (str): A string containing user information separated by semicolons.
        '''
        lst_ppl = ptr_ppl.split(';')
        self.id = lst_ppl[0]
        self.data = [lst_ppl[0], lst_ppl[1], f'{lst_ppl[3]}{(' ' + lst_ppl[2]) if lst_ppl[2] != '' else ''}'
                                             f'{(' ' + lst_ppl[4]) if lst_ppl[4] != '' else ''}', lst_ppl[5]]
        self.total = ''
        for i in range(len(User.defintns)):
            if self.data[i] != '':
                self.total += User.defintns[i] + self.data[i] + ' '
        User.users.append(self.total)

    def __str__(self):
        return self.total

    def __repr__(self):
        return str(self.total)


class Meeting:
    '''
    A class representing a meeting with meeting details and attendees.

    Attributes:
        lst_meeting (list): A list to store meeting objects.
    '''
    lst_meeting = []

    def __init__(self, ptr_meet):
        '''
        Initialize a Meeting object with meeting details and attendees.

        Args:
            ptr_meet (str): A string containing meeting information separated by semicolons.
        '''
        lst_meet = ptr_meet.split(';')
        self.id = lst_meet[0]
        self.date = Date(lst_meet[1])
        self.title = lst_meet[2]
        self.employees = Load.ppl_meet[self.id]
        self.item = [f'Рабочая встреча {self.id}', f'{self.date} {self.title}']
        for ppl in self.employees:
            self.item.append(User.users[int(ppl) - 1])
        self.final = ''
        for i in self.item:
            self.final += f'{i}{'\n'}'
        Meeting.lst_meeting.append(self.final)

    def add_person(self, person):
        '''
        Add a person to the meeting attendees.

        Args:
            person (str): The person to be added to the meeting.
        '''
        self.final += f'{person}{'\n'}'

    def count(self):
        '''
        Count the number of attendees in the meeting.

        Returns:
            int: The number of attendees in the meeting.
        '''
        count_ppl = self.final.count('ID:')
        return count_ppl

    @classmethod
    def count_meeting(cls, date):
        '''
        Count the number of meetings on a given date.

        Args:
            date (Date): The date object representing the date to count meetings for.

        Returns:
            int: The number of meetings on the given date.
        '''
        count_meet = 0
        for i in Meeting.lst_meeting:
            if str(date) in i:
                count_meet += 1
        return count_meet

    @classmethod
    def total(cls):
        '''
        Calculate the total number of attendees in all meetings.

        Returns:
            int: The total number of attendees in all meetings.
        '''
        total = 0
        for i in Meeting.lst_meeting:
            total += i.count('ID:')
        return total


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)

print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))