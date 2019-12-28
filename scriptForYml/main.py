from YmlSkript import *


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
        print('want to do a full configuration setup? y/n\n')
        choice = input()
        start_to_create(choice)


if __name__ == "__main__":
    create_yml()
