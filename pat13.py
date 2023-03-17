#program to display mathmetical table
class new:
    def __init__(self):
        pass
    def accept(self):
        self.n=int(input("enter a value:"))
    def process(self):
        for i in range(1,11):
            print(self.n,"*",i,"=",i*self.n)
s=new()
s.accept()
s.process()
