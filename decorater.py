def func2(func):
       def func3(arg):
              if arg.isupper():
                     return func(arg)
              else:
                     return arg.upper()
       return func3


@func2
def func(arg):
       print("i am a very bad function:",arg.lower())
       return arg.lower()

print(func("VEERA"))        
                
