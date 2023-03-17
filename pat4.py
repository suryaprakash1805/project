#program to display sum of odd no in the givaen range
class display:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.i=int(input("enter the initial vales"))
        self.f=int(input("enter the final valyes"))
    def process(self):
        while self.i<=self.f:
              if(self.i%2!=0): 
                 print(self.i,end=' ')
                 self.sum=self.sum+self.i
              self.i=self.i+1
        print("sum is ",self.sum)      
s=display()
s.accept()
s.process()

