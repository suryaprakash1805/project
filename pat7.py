#program to find ther facotrs
class new:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter a number"))
    def process(self):
        for i in range(1,self.n):
            if self.n%i==0:
                print(i)
                self.sum=self.sum+i
    def output(self):
        if self.sum==self.n:
              print("the no ",self.n,"is perfect")
        else:
            print("the no is",self.n,"is not perfect")
s=new()
s.accept()
s.process()
s.output()
