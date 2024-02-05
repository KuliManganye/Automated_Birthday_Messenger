import datetime as dt
import smtplib
import pandas
import random


MY_EMAIL = "myemail@gmail.com" """ use your own email address here"""
PASSWORD = "hbfnjsd67hfbnbdo8"  """use own email password here"""
# Email password is obtained from your provider, you need to create an app password that will be used solely for the
# app that you create and a new password will be generated for you that should be used with this app only, separate
# from your account password

# Using the date time module, if running the program every day, the program needs to be able to pick out what day and
# what month it is on and save the day and month as a tuple

today = dt.datetime.now()
month = today.month
day = today.day
birthday_day = (month, day)
print(birthday_day)


# use Pandas to read the csv file that contains the names, emails, and birthdays of the One Piece characters.
birthday = pandas.read_csv("birthday.csv")

# Using List Comprehension, create a dictionary that will only hold the day and month of all the one piece characters
# in the csv file
birthdays_dictionary = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday.itterows()}

# Having set date time to get the "today's date", everytime the program is run, using an if statement, check if
# "today's date" corresponds with any days in the new dictionary - birthday dictionary
if birthday_day in birthdays_dictionary:
    person = birthdays_dictionary[birthday_day]
    # Since there are 3 template letters to choose from, using random, will allow the program to choose one of the 3 at
    # random
    letter = f"letter_templates/letter_{random.randint(1,3)}.txt"

    # Open the letter and replace the name on top of the template with the name of the person whose birthday pinged,
    with open(letter) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    # finally, with smtplib, send them an automated happy birthday message
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")

