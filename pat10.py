#to check the no is palindrome

class display:
    def __init__(self):
        self.rev=0
    def accept(self):
        self.n=int(input("enhter a number:"))
        self.value=self.n
    def process(self):
        while(self.n!=0):
            self.r=self.n%10
            self.rev=self.rev*10+self.r
            self.n=self.n//10
    def output(self):
        if self.value==self.rev:
            print( self.value,"it is a palindrome")
        else:
            print(self.value,"is not a palindromne")
s=display()
s.accept()
s.process()
s.output()
