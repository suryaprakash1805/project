#program to check given is prime or not
class hulk:
    def __init__(self):
        self.count=0
    def accept(self):
        self.n=int(input("enter a value"))
    def process(self):
        for i in range(1,self.n+1):
            if self.n%i==0:
                self.count=self.count+1
    def output(self):
        if self.count>2:
            print(self.n,"is not prime no")
        else:
            
            print(self.n,"is prime no")
s=hulk()
s.accept()
s.process()
s.output()
