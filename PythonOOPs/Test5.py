

import datetime
class Students:
    fee_hike = 2.0
    def __init__(self, fname,lname, fees):
        self.fname = fname
        self.lname = lname
        self.fees = fees
        self.email = f'{fname}.{lname}@gmail.com'

    def fullname(self):
        return f'{self.fname} {self.lname}'

    @staticmethod
    def is_holiday(day):
        if day.weekday == 5 or day.weekday == 6:
            return f'{day} is Holiday'
        return f'{day} is not holiday'

my_date = datetime.date(1997, 7, 5)
print(Students.is_holiday(my_date))