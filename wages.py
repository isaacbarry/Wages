# TODO setup kivy and gui


def main():
    # ask user if adding new user
    # if adding new user add them to a csv and ask what their salary is
    check = False
    add_another = False
    while not add_another:
        while not check:
            print('Do you want to add a new user? Yes/No')
            user_add = input().upper()
            user_add = check_input(user_add)
            response = str(user_add[0])
            check = bool(user_add[1])
        # if adding new user get details of new user
        if user_add:
            print('Salary of new user')
            salary = int(input('What is their salary?'))
        else:
            add_another = False


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


if __name__ == '__main__':
    main()