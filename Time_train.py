
import os,time
os.system('cls')

the_time=''
new_time = ''
new_time1 = ''
new_time2 = ''


class Time:
    def __init__(self,time) :

        self.hour = int(time[0])
        self.minutes = int(time[1])
        self.second = int(time[2])

    def __str__(self):
        return f'{self.hour:02}:{self.minutes:02}:{self.second:02}'

    def __add__(self,other):
        second = self.second + other.second 
        minutes = self.minutes + other.minutes + (second // 60)
        hour = self.hour + other.hour + (minutes // 60)

        return Time([hour%24 , minutes%60, second%60])

    def __gt__ (self ,other):
        return (self.hour > other.hour)\
            or (self.hour == other.hour and self.minutes > other.minutes)\
            or (self.hour == other.hour and self.minutes == other.minutes and self.second > other.second)

    def __eq__(self,other):
        return (self.hour == other.hour) and (self.minutes == other.minutes) and (self.second == other.second)

user_choose = int(input("Enter your choose \n1.Show current system time\n2.Enter time manualy\n3.both options :"))
while True:
    if user_choose == 1:
        the_time = time.strftime("%H:%M:%S")
        print(f'Sytem Time is : {the_time}')
        new_time = the_time.split(':')
        time1 = Time(new_time)

        break

    elif user_choose == 2:
        time1= input("Enter time1 by this format :Hour,Minute,Second : ")
        new_time1 = time1.split(',')
        time2= input("Enter time2 by this format :Hour,Minute,Second : ")
        new_time2 = time2.split(',')
        
        time1 = Time(new_time1)
        time2 = Time(new_time2)

        user_operator = int(input("1.Plus Times\n2.Equals\n3.Greater than : "))

        if user_operator == 1:
            print(f'Time1 + Time2 is : {time1 + time2}')
        elif user_operator == 2:
            print(f'is Time1 equals time2? {time1 == time2}')
        elif user_operator == 3:
            print(f'is Time1 greater than Time2? {time1 > time2}')
        break

    elif user_choose == 3:
        system_time = time.strftime("%H:%M:%S")
        print(f'Sytem Time is : {system_time}')
        the_time= input("Enter time by this format :Hour,Minute,Second : ")

        new_time1 = system_time.split(':')
        time1 = Time(new_time1)

        new_time2 = the_time.split(',')
        time2 = Time(new_time2)

        user_operator = int(input("1.Plus Times\n2.Equals\n3.Greater than : "))

        if user_operator == 1:
            print(f'System Time + User Time is : {time1 + time2}')
        elif user_operator == 2:
            print(f'is System Time equals User Time? {time1 == time2}')
        elif user_operator == 3:
            print(f'is System Time greater than User Time? {time1 > time2}')

        break

    else:
        print("\nyou just can choose 1,2,3 !!\n")
        user_choose = int(input("Enter your choose \n1.Show current system time\n2.Enter time manualy\n3.both options :"))

