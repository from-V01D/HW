import random

class Student:
    def init(self, full_name, year):
        self.name = full_name
        self.year = year
        self.skills = random.randint(1, 5)
        self.money = random.randint(1, 10)

    def grow_up(self):
        self.year += 1

    def study(self):
        self.skills += 0.5

    def chill(self):
        self.skills -= 0.3
        self.money -= 0.2

    def work(self):
        self.money += 0.5

    def introduce(self):
        print(f'My name is {self.name}')
        print(f'I am {self.year} years old')
        print(f'My skills is {self.skills:.2f}')
        print(f'Money: {self.money:.2f}$')


nick_mark = Student('Nick Mark', 17)

nick_mark.introduce()

for day in range(1, 365):
    print(f'======== {day} ========')

    choice = random.randint(0,2)

    if choice == 0:
        nick_mark.chill()
        print("Chilling... 😎🏖️")
    elif choice == 1:
        nick_mark.study()
        print('Studying... 🧑‍🎓📚')
    else:
        nick_mark.work()
        print('Working... 🧑‍💼🏢')
    print()

nick_mark.grow_up()
nick_mark.introduce()