#FINAL IGCSE MAY-JUNE 2022 PRE-RELEASE CODE PAPER 21

import datetime
date_founded=datetime.datetime(2022, 1, 1).date()
First_name=["John","Marten","Jesse","Brian","Sarah-Jane","Stacey","Randall","Wandia","Klein","Eugene"]
Last_name=["Nyaribo","Zaky","Kipkorir","Maina","Migabo","Ebot","Gituku","Karimi","Nderitu","Omondi"]
Volunteer_options=["0","1","2","3","1","3","0","2","3","1"]
Volunteer_areas=["Not Volunteering","Gift Shop","Entrance Gate","Painting and Decoration"]
Option_code=["0","1","2","3"]
Joining_date=[]
Year_joined=[2022,2022,2018,2019,2021,2020,2017,2018,2022,2015]
Payment_status=["Yes","No","No","Yes","No","Yes","Yes","No","No","Yes"]
Sponsors=[["Daniel Kimani","For my Daughter Karen"],["Chanzu Patel","In memory of Gritty"],["Andrew John","Like i'm playing Fortnite"]]
finished=0

print()
print("=======Welcome To Friends Of SeaView System=======")
print()
print("==================================================")
print("=============Entering Members records=============")
print("==================================================")
print()
while finished==0:
    first_name=input("Enter your First Name: ")
    last_name=input("Enter your Last Name: ")
    First_name.append(first_name)
    Last_name.append(last_name)
    print("===============================================")
    print("Volunteer Option Areas")
    print("===============================================")
    code=""
    while code not in Option_code:
        print("Select your volunteer option")
        print()
        print("Option_code       Description")
        for i in range(len(Volunteer_areas)):
            print(Option_code[i],"       ",Volunteer_areas[i])
        print()
        code=input(str("Please type in the option code to volunteer: "))
        if code not in Option_code:
            print("Area code does not exist, Please try again!")
        else:
            areaposition=Option_code.index(code)
            print("You have chosen: ",Volunteer_areas[areaposition])
            Volunteer_options.append(code)

    days_in_months=[[1,3,5,7,8,10,12],[4,6,9,11],[2]]

    year=int(input("What year did you join: "))
    while year>datetime.date.today().year:
        year=int(input("This is an invalid year! Re-enter the year joined: "))
    Year_joined.append(year)
    month=int(input("Month number (1 to 12): "))
    while month<1 or month>12:
        month=int(input("This is an invalid month. Please enter a month from 1 to 12: "))
    day=int(input("Day: "))
    if month in days_in_months[0]:
        while day<1 or day>31:
            day=int(input("Please enter a day between 1 to 31: "))
    if month in days_in_months[1]:
        while day<1 or day>30:
            day=int(input("Please enter a day between 1 to 30: "))
    if month in days_in_months[2]:
        while day<1 or day>28:
            day=int(input("Please enter a day between 1 to 28: "))

    date=str(day)+"/"+str(month)+"/"+str(year)
    date=datetime.datetime.strptime(date,"%d/%m/%Y").date()
    print("Joining date is: "+date.strftime('%d/%m/%Y'))
    Joining_date.append(date.strftime('%d/%m/%Y'))

    payment=str(input("Membership fee of $75 paid? (Yes/No): "))
    while payment not in ["Yes","No"]:
        payment=input("Invalid payment entry. Please enter either, Yes or No: ")
    Payment_status.append(payment)
    more=input("Enter more records? (Yes/No): ")
    if more=="No":
        finished=1
    print()

Sponsor_detail=input("Enter sponsor detail? (Yes/No): ")
if Sponsor_detail=="Yes":
    print()
    print("=======Input new wooden plank sponsor details=======")
    print()
    false=0
    while false==0:
        name=input("Please enter your name: ")
        text=input("Please enter the message you would like to display: \n")
        print("Outputting preferences: ")
        print("Name:", name)
        print("Message displayed:", text)
        confirm=input("Are you happy with your preferences? Enter 'Yes' if so, and enter 'No' to change them: ").lower()
        if confirm=="Yes":
            print()
            print("Thank you for sponsoring the pier. You have been charged $200.")
            print()
        if confirm=="No":
            print("Let's try that again")
            false=0
        Sponsors.append([name,text])
        another_sponsor=input("Enter another sponsor detail? (Yes/No): ")
        if another_sponsor=="No":
            false=1

print()
print("\nPlease choose what you'd like to do: ")
print("1. Output full members list")
print("2. Output those members not volunteering")
print("3. Output those members volunteering at the giftshop")
print("4. Output those members volunteering at the enterance gate")
print("5. Output those members volunteering for painting and decoration")
print("6. Output members whose membership has expired")
print("7. Output members that have not paid $75")
print("8. Output wooden planks sponsers and their message")
print("9. Exit program")
print()
selection=int(input("Please enter your choice number (1,2,3,4,5,6,7,8,9): "))
while selection<1 or selection>9:
    selection=int(input("Please enter a valid choice number, between 1 to 9: "))
print()

if selection==1:
    print("The full members list is: ")
elif selection==2:
    print("The members volunteering are: ")
elif selection==3:
    print("The members volunteering at the gift shop are: ")
elif selection==4:
    print("The members volunteering at the entrance are: ")
elif selection==5:
    print("The members volunteering for painting and decoration are: ")
elif selection==6:
    print("The members whose membership has expired are: ")
elif selection==7:
    print("The members that have not yet paid the membership fee of $75 are: ")
elif selection==8:
    print("The wooden plank sponsers are: ")

for i in range(0,len(First_name)):
    if selection==1:
        print(i+1,".",First_name[i],"   ",Last_name[i])
    elif selection==2:
        if Volunteer_options[i]!="0":
            print(i+1,".",First_name[i],"   ",Last_name[i])
    elif selection==3:
        if Volunteer_options[i]!="1":
            print(i+1,".",First_name[i],"   ",Last_name[i])
    elif selection==4:
        if Volunteer_options[i]!="2":
            print(i+1,".",First_name[i],"   ",Last_name[i])
    elif selection==5:
        if Volunteer_options[i]!="3":
            print(i+1,".",First_name[i],"   ",Last_name[i])
    elif selection==6:
        if Year_joined[i]<2022:
            print(i+1,".",First_name[i],"   ",Last_name[i])
    elif selection==7:
        if Payment_status[i]=="No":
            print(i+1,".",First_name[i],"   ",Last_name[i])
if selection==8:
    for i in range(0,len(Sponsors)):
        print(i+1,".",Sponsors[i])
        
if selection==9:
    print("Exiting program...")

print()
print("=======Thank you for using the Friends Of Seaview system=======")
