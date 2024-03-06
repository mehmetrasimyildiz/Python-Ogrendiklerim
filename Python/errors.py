liste=["1","2","5a","10b","abc","10","50"]

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

while True:
    sayi = input('sayi: ')
    if sayi == 'q':
       break
    try:
        result=float(sayi)
        print('girdiğiniz sayi: ',result)
    except ValueError:
        print('geçersiz sayi')
        continue

password= input('password: ')
turkce_karakterler='şçğüöı'

def checkpassword(password):

    for i in password:
        if i in turkce_karakterler:
            raise TypeError('wrong password doesnt use turkish caracters')
        else:
            pass
    print('actept passwpord')
    
try:
    checkpassword(password)
except TypeError as err:
    print(err)


def foctoriyel(x):
    x=int(x)

    if x < 0:
        raise ValueError('negatif değer')
    
    result=1

    for i in range(1,x+1):
        result *=i
    return result

for x in [3,4,5,]:
    try:
        y=foctoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)

    