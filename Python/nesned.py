def factorial(number):
    
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    
    if not number >=0:
        raise ValueError("number must be zero or possitive ")
        
    def inner_factorial(number):
        
        if number <= 1:
            return 1
        else:
            return number * inner_factorial(number-1)
    
    return inner_factorial(number)

try:
    print(factorial('a'))
except Exception as ex:
    print(ex) 