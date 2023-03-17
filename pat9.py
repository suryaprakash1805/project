class display:
    def __init__(self):
        self.rev=0
    def accept(self):
        self.n=int(input("enhter a number:"))
    def process(self):
        while(self.n!=0):
            self.r=self.n%10
            self.rev=self.rev*10+self.r
            self.n=self.n//10
    def output(self):
        print("the reverse of the number is :",self.rev)
s=display()
s.accept()
s.process()
s.output()
