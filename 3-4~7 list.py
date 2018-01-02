from random import randint

MAXGUESTS = 3
guests = []
print("Now, you are going to have a party, Please input the names of you guests")
for i in range(MAXGUESTS):
    name = input("Guest NO.%d>>> " % (i+1))
    guests.append(name)

num = randint(1, MAXGUESTS)

print("Oh! %s can not come,so you need to invite another guest." % guests[num-1])
name = input("Name of new guest>>> ")
guests[num-1] = name

print("You just got a bigger table, you can invite three more guests.")
for i in range(MAXGUESTS):
    name = input("Guest NO.%d>>> " % (MAXGUESTS+i+1))
    guests.insert(0, name)

print("Sorry! You table will not be here in time. So you can only invite two guest!")
for i in range(4):
    print("Sorry! %s, I'm regret to tell you that I can't invite you to join the party."  % guests.pop())

for guest in guests:
    print(guest + ", please have fun here.")

guests.clear()
print(guests)
