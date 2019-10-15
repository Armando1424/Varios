import math

def menu(option):
    if str.upper(option) == "A":
        print("In one year, you would save: ",10*52)
    elif str.upper(option) == "B":
        saveMoney(10,52)
    elif str.upper(option) == "C":
        saveMoney(int(input("What initial amount, you would like to save?:\n")), 52)
    elif str.upper(option) == "D":
        amount = int(input("What initial amount, you would like to save?:\n"))
        suboption = input("If do you want to save weekly push A or B for monthly\n")
        if str.upper(suboption) == "A":
            weeks = int(input("How many weeks?\n"))
            saveMoney(amount, weeks)
        else:
            moths = int(input("How many months?\n"))
            saveMoney(amount, moths*4)
    else:
        total = int(input("What's the total amount do you want to get?\n"))
        print("Your initial amount is: ", math.ceil(total/1326))

def saveMoney(amount, weeks):
    accrued = 0
    for x in range(weeks):
        accrued += x*amount
    print("In one year, you would save: ", accrued)

print("Welcome, with this program you can calculate your save in one year")
msg =   "Push A: for to save $10 weekly\n"\
        "Push B: for to save $10 weekly but with an increment\n"\
        "Push C: for to save x amount weekly but with an increment\n"\
        "Push D: for to save x amount weekly, x number of weeks or x number of moths but with an increment\n"\
        "Push E: for to know the initial amount of a total amount\n"

menu(input(msg))    