def func2(func):
    def func3(a,b):
        if a<b:
            print("decorators function if block")
            return func(a,b)
        else:
            print("decorators function else block")
            return a-b
    return func3



@func2
def fun(a,b):
    print("i am from main function")
    return a+b
print (fun(10,40))
    
