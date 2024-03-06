def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def sayHello(name):
    print("hello",name)
    
sayHello("ali")
    
    
# def sayGreeting():
#     print("greeting")
    
# sayHello = my_decorator(sayHello)
# sayGreeting = my_decorator(sayGreeting)
# sayHello()
# sayGreeting()
