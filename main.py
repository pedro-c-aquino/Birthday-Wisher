##################### Normal Starting Project ######################

import datetime as dt
import pandas
import random
import smtplib

# Define constants to access the sender email
MY_EMAIL = # Your Email
PASSWORD = # Your password

# Grab the date time
now = dt.datetime.now()

# Build a pandas dataframe from the birthdays.csv
df = pandas.read_csv("birthdays.csv")

# Define a tuple to check the current day with datetime
birthday_today = (now.month, now.day)

# Create a dictionary with a tuple with the date of birthdays as keys and data as values
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}

# Check to see if today is anyone's birthday with the tuples created
if birthday_today in birthdays_dict:

    # If it returns true, send an email wishing happy birthday.
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
    birthday_person = birthdays_dict[birthday_today]
    letter = letter.replace("[NAME]", birthday_person["name"])
    birthday_email = birthday_person["email"]
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_email, msg=f"Subject: Feliz Aniversario\n\n{letter}")




