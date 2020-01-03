from YmlSkript import *


def option ():
    print('want to do a full configuration setup? y/n\n')
    choice = input()
    if choice == 'y' or choice == 'n':
        start_to_create(choice)
    else:
        print('use only y or n\n')
        option()


def get_help():
    with open('help') as f:
        print(f.read())


def create_yml():
    print('to display help enter "help" \n')
    print('to start to start creating ansible.config.yml press "enter" \n')
    solution = input()
    if solution == 'help':
        get_help()
        create_yml()
    elif solution == '':
        option()
    else:
        create_yml()


if __name__ == "__main__":
    create_yml()


