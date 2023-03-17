#program to find sum of no
class new:
    def __init__(self):
        self.sum=0
        self.q=0
        self.r=0
    def accept(self):
        self.n=int(input("enter a number"))
    def process(self):
        while(self.n!=0):
                self.r=self.n%10
                self.q=self.n//10
                self.n=self.q
                self.sum=self.r+self.sum
    def output(self):
              print(self.sum)
        
s=new()
s.accept()
s.process()
s.output()
