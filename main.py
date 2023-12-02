import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Час для навчання')
        self.progress += 10
        self.gladness -= 5

    def to_sleep(self):
        print('Це час для сну')
        self.gladness += 5

    def to_chill(self):
        print('Це час для відпочинку')
        self.progress -= 5
        self.gladness += 10

    def is_alive(self):
        if self.progress < -2:
            print('Йди розвивайся')
            self.alive = False
        elif self.gladness <= 0:
            print('Упс в тебе депресія')
            self.alive = False
        elif self.progress > 5:
            print('Ти молодець')
            self.alive = False

    def end_of_the_day(self):
        print(f"щастя - {self.gladness}")
        print(f"{round(self.progress, 2)}")

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'life'
        print(f"{day:^50}")
        kubik = random.randint(1, 3)
        if kubik == 1:
            self.to_study()
        elif kubik == 2:
            self.to_sleep()
        elif kubik == 3:
            self.to_chill()
        self.end_of_the_day()
        self.is_alive()


nick = Student(name='Ivan')
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
