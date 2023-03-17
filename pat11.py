#program to find sum of the given numbers
class new:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter a number:"))
    def process(self):
        while self.n!=0:
            self.r=self.n%10
            self.sum=self.sum+self.r**2
            self.n=self.n//10
    def output(self):
        print("the sum of squares of numbers ",self.sum)
s=new()
s.accept()
s.process()
s.output()
