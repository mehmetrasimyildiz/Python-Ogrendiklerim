import re


def check_password(psw):
    if len(psw)<8:
        raise Exception("password less must be seven caracters")
    elif not re.search("[a-z]",psw):
        raise Exception("password must be lowercase")
    elif not re.search("[A-Z]",psw):
        raise Exception("password must be uppercase ")
    elif not re.search("[0-9]",psw):
        raise Exception("password must be number")
    elif not re.search("[_@$]",psw):
        raise Exception("password must be alpha numeric")
    elif re.search("[\n]",psw):
        raise Exception("password must not be include space")
    
password="12345678aA_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("accept password")
finally:
    print('validation completed')
    
    
        