from datetime import datetime
import re

def check_date_input():
    pattern = '%d.%m.%Y'  # only accept DD.MM.YYYY!!! https://stackoverflow.com/questions/69906987/how-to-limit-the-input-in-python-for-only-dates
    date = None

    while date is None:
        inp = input('Please enter a date (DD.MM.YYYY): ')

        try:
            date = datetime.strptime(inp, pattern)
        except ValueError:
            print(f'"{inp}" is not a valid date. Please use the format DD.MM.YYYY.')
            continue

    print(f'You entered a valid date: {date.strftime("%d.%m.%Y")}')
    valid_date = date.strftime('%d.%m.%Y')
    return valid_date

# check if the email is valid method 1: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def email_checker():
    # check if the email matches the regex pattern
    email_correct = False
    while email_correct is False:
        email = input('Please enter a valid e-mail address: ')
        if re.fullmatch(regex, email):
            email_correct = True
            return email
        else:
            print("Invalid e-email address.")




def repeat_password_check():
    while True:
        aPassword = input("Please choose your password: ")
        aPassword2 = input("Confirm your password: ")

        if aPassword == aPassword2:
            print("Passwords match.")
            return aPassword
        else:
            print("Passwords do not match. Please try again.")


# function to identify the actual password after entering username
# needing this for logging in
def search_the_password(json_file, searched_id):
    for x in json_file.get('users', []):
        if x.get("aAccountName") == searched_id:
            return x.get("aPassword")

