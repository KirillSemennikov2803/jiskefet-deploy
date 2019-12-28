from ipaddress import ip_address
import getpass
import validators


def set_some_value(nameOfvalue):
    print('enter ' + nameOfvalue + ':')
    return input()


def enter_the_host():
    host = set_some_value('host address')
    if host == 'localhost':
        host = '127.0.0.1'
        return host
    elif host[0:4] == 'http':
        return host
    else:
        try:
            ip = ip_address(host.split()[0])
        except ValueError:
            print('Incorrect IP address')
            return enter_the_host()
        except IndexError:
            print('Bad input string')
            return enter_the_host()
        return str(ip)


def enter_the_password():
    print('enter password')
    pw1 = getpass.getpass()
    # pw1=input()
    print('сonfirm password')
    pw2 = getpass.getpass()
    # pw2=input()
    if pw1 != pw2:
        print('confirm password does not match. enter password again')
        return enter_the_password()
    else:
        return pw1


def enter_the_redirect_uri():
    redirect = set_some_value('redirect uri')
    if validators.url(redirect):
        if redirect.endswith('/callback'):
            return redirect

        else:
            print('missing postfix / callback. correct format: http: // {{ansible_remote_address}} / callback')
            return enter_the_redirect_uri()
    else:
        print('The string was entered incorrectly. correct format: http: // {{ansible_remote_address}} / callback')
        return enter_the_redirect_uri()


def enter_yes_or_no(nameOfvalue, trueFalse):
    print('use ' + nameOfvalue + '?')
    choice = input()
    if trueFalse == 0:
        if choice == 'yes' or choice == 'no':
            return choice
        else:
            print('please enter only yes or no')
            enter_yes_or_no(nameOfvalue, trueFalse)
    if trueFalse == 1:
        if choice == 'true' or choice == 'false':
            return choice
    else:
        print('please enter only true or false')
        enter_yes_or_no(nameOfvalue, trueFalse)
