# A program that checks password strength.

# Strong password Criteria: Atleast 8 Characters in lenght,
#                           Atleast 1 lower and upper case letter
#                           Atleast 1 numerical digit
#                           Atleast 1 special non-letter special character (list obtained from https://www.owasp.org/index.php/Password_special_characters).

import re

def passwordCheck(password):

    # Define a regex for strong password
    strongPass = re.compile(r'''^((?=[A-Za-z0-9 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]{8,})                                  # Checks for atleast 8 characters
                                 (?=(?:[^a-z]*[a-z})+)                                                                  # Checks for atleast 1 Lowercase
                                 (?=(?:[^A-Z]*[A-Z])+)                                                                  # Checks for atleast 1 Uppercase
                                 (?=(?:[^0-9]*[0-9])+)                                                                  # Checks for atleast 1 Numerical Digit
                                 (?=(?:[^ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*[ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])+))     # Checks for atleast 1 Non-Letter Special Character
                                ''', re.VERBOSE)

    # Check Password
    passCheck = strongPass.search(password)
    return passCheck == None


def main():

    # receive password
    passwrd = str(input('Please enter your password: '))

    # call passwordCheck
    check = passwordCheck(passwrd)

    # display result
    if check == False:
        print('So Stronk')
    else:
        print("Little baby password doesn't match up small son")

    return

main()
