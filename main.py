import random
import time

class Define_CardSet:
    def __init__(self, Name, Color, Type):
        self.Name = Name
        self.Color = Color
        self.Type = Type
        self.set = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Person:
    def __init__(self, Name, Country):
        self.Name = Name
        self,Country = Country


def Calc(First, Second):
    if First in ['J', 'Q', 'K']: First = 10
    elif First == 'A': First = 1
    if Second in ['J', 'Q', 'K']: Second = 10
    elif Second == 'A': Second = 1
    #check ace
    if First == 1 or Second == 1 and First + Second <= 11:
        return(First + Second + 10)
    return(First + Second)


def remove_card(set, card):
    set.remove(card)


def pair():
    NList = [] #count card sets
    for i in List:
        List.remove(i) if len(i.set) == 0 else NList.append(i) #remove empty list
    if len(NList) >= 1:
        if len(NList) == 1 and len(NList[0].set) < 2: exit(0)
        random_list_First = random.choice(List)
        random_card_First = random.choice(random_list_First.set)
        if len(random_list_First.set) < 1: List.remove(random_list_First)

        random_list_Second = random.choice(List)
        random_card_Second = random.choice(random_list_Second.set)
        remove_card(random_list_Second.set, random_card_Second)
        if len(random_list_Second.set) < 1: List.remove(random_list_Second)

        if len(List) == 0: exit(0)
        return(random_card_First, random_list_First.Type, random_card_Second, random_list_Second.Type)
    else:
        exit(0)


def Deal():
    for i in List:
        if len(i.set) == 0: List.remove(i)
        random_list_First = random.choice(List)
        random_card_First = random.choice(random_list_First.set)
        if len(random_list_First.set) < 1: List.remove(random_list_First)
        if len(List) == 0: exit(0)
        return(random_card_First, random_list_First.Type)


def deal_c(machine, machine_count, User, User_Count):
    User_Deal = Deal()
    User_New_Calc = Calc(User_Count, User_Deal[0])
    if User_New_Calc > 21:
        print("Your set: " + str(User) + " - " + str(User_Deal) + "total of:" + str(User_New_Calc))
        print("YOU LOSE!")
        exit(0)
    else:
        print("Your set: " + str(User) + " - " + str(User_Deal) + "total of:" + str(User_New_Calc))
        print("machine: " + str(machine))
        if machine_count > User_New_Calc:
            print(" you lose!")
        else:
            random_wait = random.randrange(1, 7)
            time.sleep(random_wait)
            machine_random_choise = random.choice(['true', 'false'])
            if machine_random_choise == 'true':
                machine_deal = Deal()
                machine_new_calc = Calc(machine_count, machine_deal[0])
                if machine_new_calc > 21:
                    print("Your set: " + str(machine) + " - " + str(machine_deal) + "total of:" + str(machine_new_calc))
                    print("you won!")
                else:
                    if machine_new_calc > User_New_Calc:
                        print("machine won!")
                    elif User_New_Calc > machine_new_calc:
                        print("You won!")
                    else:
                        print("Tie")
            else:
                if machine_count > User_New_Calc:
                    print("machine won!")
                elif User_New_Calc > machine_count:
                    print("You won!")
                else:
                    print("Tie")


def stand_c(machine, machine_count, User, User_Count):
    print("machine: " + str(machine))
    if machine_count < User_Count:
        random_wait = random.randrange(1, 7)
        time.sleep(random_wait)
        machine_random_choise = random.choice(['true', 'false'])
        if machine_random_choise == 'true':
            machine_deal = Deal()
            machine_new_calc = Calc(machine_count, machine_deal[0])
            if machine_new_calc > 21:
                print("Your set: " + str(machine) + " - " + str(machine_deal) + "total of:" + str(machine_new_calc))
                print("you won!")
            else:
                if machine_new_calc > User_Count:
                    print("machine won!")
                elif User_Count > machine_new_calc:
                    print("You won!")
                else:
                    print("Tie")
        else:
            if machine_count > User_New_Calc:
                print("machine won!")
            elif User_New_Calc > machine_count:
                print("You won!")
            else:
                print("Tie")
    elif machine_count > User_Count:
        print("machine won!")
    else:
        print("Tie")


def main():
    while True:
        machine = pair()
        machine_count = Calc(machine[0], machine[2])
        print("machine: " + str(machine[0]) + " " + str(machine[1]))
        User = pair()
        User_Count = Calc(User[0], User[2])
        print("Your set: " + str(User) + " - " + str(User_Count))
        User_Input = input("please choose between 'stand' and 'deal': ")
        if User_Input.lower() == 'deal':
            deal_c(machine, machine_count, User, User_Count)
        elif User_Input.lower() == 'stand':
            stand_c(machine, machine_count, User, User_Count)
        else:
            main()


#Card sets [Hearts, Diamonds, Clubs, Spads]
Hearts = Define_CardSet('Hearts', 'Red', 'Hearts')
Diamonds = Define_CardSet('Diamonds', 'Red', 'Diamonds')
Clubs = Define_CardSet('Clubs', 'Black', 'Clubs')
Spads = Define_CardSet('Spads', 'Black', 'Spads')

List = [Hearts, Diamonds, Clubs, Spads]


#print(Calc(random_card_First, random_card_Second))

main()