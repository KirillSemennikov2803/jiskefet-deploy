from YmlSkript import *


def getHelp():
    with open('help') as f:
      print(f.read())
def main():
    print('to display help enter "help" \n')
    print('to start to start creating ansible.config.yml press "enter" \n')
    solution = input()
    if solution=='help':
        getHelp()
        main()
    elif solution=='':
       startToCreate()

main()
    