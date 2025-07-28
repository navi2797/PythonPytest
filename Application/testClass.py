import sys

class Base:

    classvariable = 10

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def getdata(self):
        return self.a,self.b

    def setdata(self,x,y):
        self.a = x
        self.b = y

    @classmethod
    def classfunc(cls):
        print(cls.classvariable)

class child1(Base):

    def __init__(self,x,y,p,q):
        super().__init__(p,q)
        self.x = x
        self.y = y

    def setdataforchild(self,t1,t2,t3,t4):
        self.x = t1
        self.y = t2
        self.a = t3
        self.b = t4

    def getdatafromchild(self):
        return self.x,self.y,self.a,self.b
    
    @classmethod
    def setbaseclassvariable(cls):
        cls.classvariable = 1000


obj = Base(2,3)
Base.classfunc()
obj.classfunc()
child1.classfunc()  
child1.setbaseclassvariable()  
#Base.classfunc()
child1.classfunc() 
a,b = obj.getdata()
print(a,b)
obj.setdata("Arjuna","Sangeetha")
a,b=obj.getdata()
print(a,b)

childobj = child1(10,20,30,40)
t1,t2 = childobj.getdata()
print(t1,t2)
t1,t2,t3,t4 = childobj.getdatafromchild()
print(t1,t2,t3,t4)
childobj.setdataforchild(45,55,65,75)
t1,t2,t3,t4 = childobj.getdatafromchild()
print(t1,t2,t3,t4)

sq = lambda x:x*x
print("*************************")
print(sq(2))

def square(a,b):
    square_list = []
    for ele in b:
        a(ele)
        square_list.append(a(ele))
    return square_list

ee = square(sq,[4,5,8])
print(ee)

def decorator(func):
    print("inside deco")
    def wrapper(*a,**b):
        print("inside wrap")
        return func(a[0],a[1])
    return wrapper

@decorator
def add(a,b):
    print("inside add func")
    return a+b

@decorator
def concat(a,b):
    return a+b

d=add(4,9000)
print(d)
print(sys.argv[0],sys.argv[1],sys.argv[2])

dict1 = '{"Name":"Naveen","Gender":"Male","Job":"IT"}'
import json
json1 = json.loads(dict1)
print(json1['Name'])
ss = concat("Naveen","SangeethaArjuna")
print(ss)