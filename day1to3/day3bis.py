'''
programme d envoi d email pour nous rappeler les grosses deadlines
a finaliser
rajouter la partie d envoi de mail

'''
#import urllib.request
#import os
from datetime import date, datetime

def main():

    get_today_date()

    ask_user_deadlines_and_infos()

    #send_emails()

    return


def get_today_date():

    return date.today()


def ask_user_deadlines_and_infos():

    print("Hello user ! \nWelcome on our DEADLINE REMINDER Platform \nTell us more below")
    recipient = input("Who is the recipient of the email ? ")
    mail_object = input("What is the object of the email ? ")
    deadline = input("What is the deadline of your project ? ")
    delai_reminder_1 = input("How many days before the deadline do you want the first reminder to be sent ? ")
    delai_reminder_2 = input("How many days before the deadline do you want the second reminder to be sent ? ")
    text_email = input("Please just type any complementary details you wish to be sent to the email. ")

    today = date.today()

    print(deadline[0:2])
    print(deadline[3:5])
    print(deadline[6:8])

    year1 = int(deadline[0:2])
    month1 = int(deadline[3:5])
    day1 = int(deadline[6:8])

    #year2 = int(delai_reminder_2[0:2])
    #month2 = int(delai_reminder_2[3:5])
    #day2 = int(delai_reminder_2[6:8])

    deadline = datetime(year1, month1, day1)


    #date_reminder_2 = deadline -



    return deadline

def send_emails():

    pass




if __name__ == '__main__':
    main()