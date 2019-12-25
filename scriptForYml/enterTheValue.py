from ipaddress import ip_address
import getpass
import validators

def enterTheHost():
    print('enter host address:')
    host = input()
    if host=='localhost':
        host='127.0.0.1'
        return host
    elif host[0:4]=='http':
        return host
    else:
        try:
            ip = ip_address(host.split()[0])
        except ValueError:
            print('Incorrect IP address')
            return enterTheHost()
        except IndexError:
            print('Bad input string')
            return enterTheHost()
        return str(ip)

def enterTheName():
    print(' enter username:')
    name = input()
    return name

def enterThePassword():
    print('enter password')
    pw1 = getpass.getpass()
    #pw1=input()
    print('сonfirm password')
    pw2 = getpass.getpass()
    #pw2=input()
    if pw1!=pw2:
        print ('confirm password does not match. enter password again')
        return enterThePassword()
    else:
        return pw1

def enterTheDBName():
    print('enter database name:')
    return input()

def enterTheClientId():
    print('enter client ID:')
    return input()

def enterTheSecret():
    print('enter client secret:')
    return input()
    
def enterTheRedirectUri():
    print('enter redirect uri:')
    redirect = input()
    if validators.url(redirect):
        if redirect.endswith('/callback'):
            return redirect
            
        else:
            print('missing postfix / callback. correct format: http: // {{ansible_remote_address}} / callback')
            return enterTheRedirectUri()
    else:
            print('The string was entered incorrectly. correct format: http: // {{ansible_remote_address}} / callback')
            return enterTheRedirectUri()