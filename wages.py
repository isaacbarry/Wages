# TODO setup kivy and gui


def main():
    # ask user if adding new user
    # if adding new user add them to a csv and ask what their salary is
    check = False
    add_another = True
    while add_another:
        while not check:
            print('Do you want to add a new user? Yes/No')
            user_add = input().upper()
            user_add = check_input(user_add)
            response = str(user_add[0])
            check = bool(user_add[1])
        # if adding new user get details of new user
        if user_add:
            check = False
            while not check:
                # Check to see if user is salary or overstay
                response = input('Are they on salary or overstay?').upper()
                response = check_response(response)
                overstay = response[0]
                salary = response[1]
                check = response[2]
        else:
            add_another = False
            print('NO')
        check = False
        while not check:
            add_another = input('Do you want to add another user? yes/no').upper()
            temp = check_response(add_another)
            add_another = temp[0]
            check = bool(temp[1])


def check_input(user_add):
    """Checks a valid input was entered for yes/no"""
    check = False
    if user_add == 'YES':
        user_add = True
        check = True
    elif user_add == "NO":
        user_add = False
        check = True
    else:
        print('Please enter yes or no.')
        check = False

    return user_add, check


def check_response(response):
    """Checks input if it is overstay or salary"""
    overstay = 0
    salary = 0
    if response == 'OVERSTAY':
        overstay = input('Amount per day')
        check = True
    elif response == 'SALARY':
        salary = input('What is their yearly salary?')
        check = True
    else:
        print('Please enter overstay or salary')
        check = False

    return overstay, salary, check




if __name__ == '__main__':
    main()