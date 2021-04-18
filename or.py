#method overriding& over loading
"""class village:
    def m1(self,a,b):
        print(a,b)
    def m1(self,a,b,c):
        print(a,b,c)
vv=village()
vv.m1(10,20)
vv.m1(10,20,30)"""
class Village:
    __x =20
    def __init__(self,name):
        self.__village=name
    def post(self,name):
        print("post name",name)
    def __mandal(self,name):
        print("mandal name",name)
    def __district(self,name):
        print("dist",name)
        print(self.__village)
        print(Village.__x)
            

vv = Village("reddy vari palli")
vv.post("rami reddy")
vv._Village__mandal("singareni")
vv._Village__district("chittoor")
    
