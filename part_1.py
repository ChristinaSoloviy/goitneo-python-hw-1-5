from collections import defaultdict
from datetime import datetime


def get_birthdays_per_week(users: list[dict]) -> None:
    """ функція для виведення списку колег, яких потрібно привітати з днем народження на тижні """
    birthday_persons = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name: str = user["name"]
        birthday: datetime = user["birthday"].date()  
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year+1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            weekday = birthday_this_year.weekday()
            if weekday in [5, 6, 0]:
                birthday_persons['Monday'].append(name)
            elif weekday == 1:
                birthday_persons['Tuesday'].append(name)
            elif weekday == 2:
                birthday_persons['Wednesday'].append(name)
            elif weekday == 3:
                birthday_persons['Thursday'].append(name)
            elif weekday == 4:
                birthday_persons['Friday'].append(name)
    info = ''
    for day, persons in birthday_persons.items():
        info += f'{day}: {" ".join(persons)}\n'
    print(info)    



# тестування
users =  [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
          {"name": "Bob", "birthday": datetime(2000, 2, 25)},
          {"name": "Bill", "birthday": datetime(2000, 2, 28)},
          {"name": "Nick", "birthday": datetime(2000, 3, 3)}]    


if __name__ == '__main__':
    get_birthdays_per_week(users)