class AirTicket:
    '''
    A class representing an airline ticket with passenger details and flight information.

    Attributes:
        passenger_name (str): The name of the passenger.
        _from (str): The departure location.
        to (str): The destination location.
        date_time (str): The date and time of the flight.
        flight (str): The flight number.
        seat (str): The seat number.
        _class (str): The class of the ticket (e.g., economy, business).
        gate (str): The gate number for boarding.
        ticket (str): Formatted ticket information.
    '''
    passenger_name = ''
    _from = ''
    to = ''
    date_time = ''
    flight = ''
    seat = ''
    _class = ''
    gate = ''

    def __init__(self, ptr):
        '''
        Initialize an AirTicket object with ticket details.

        Args:
            ptr (str): A string containing ticket information separated by semicolons.
        '''
        AirTicket.passenger_name = ptr.split(';')[0]
        AirTicket._from = ptr.split(';')[1]
        AirTicket.to = ptr.split(';')[2]
        AirTicket.date_time = ptr.split(';')[3]
        AirTicket.flight = ptr.split(';')[4]
        AirTicket.seat = ptr.split(';')[5]
        AirTicket._class = ptr.split(';')[6]
        AirTicket.gate = ptr.split(';')[7]
        self.ticket = (f'|{AirTicket.passenger_name}{' ' * (16 - len(AirTicket.passenger_name))}|{AirTicket._from} '
                       f'|{AirTicket.to}|{AirTicket.date_time}  |{AirTicket.flight}{' ' * (20 - len(AirTicket.flight))}|'
                       f'{AirTicket.seat}{' ' * (4 - len(AirTicket.seat))}|{AirTicket._class}  |{AirTicket.gate}  |')

    def __str__(self):
        return self.ticket

    def __repr__(self):
        return str(self.ticket)


class Load(AirTicket):
    '''
    A subclass of AirTicket responsible for loading ticket data from a file.

    Attributes:
        data (list): A list to store loaded AirTicket objects.
    '''
    data = []

    @classmethod
    def write(cls, file_name):
        '''
        Load ticket data from a file and create AirTicket objects.

        Args:
            file_name (str): The name of the file containing ticket information.

        Returns:
            list: A list of AirTicket objects created from the file.
        '''
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for i in range(1, len(lines)):
                Load.data.append(AirTicket(lines[i][:-1]))
        return Load.data


tickets = Load.write('askdnklsa')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)
