#program to display odd no in the givaen range
class display:
    def accept(self):
        self.i=int(input("enter the initial vales"))
        self.f=int(input("enter the final valyes"))
    def process(self):
        while self.i<=self.f:
              if(self.i%2!=0):
                 print(self.i,end=' ')
              self.i=self.i+1
s=display()
s.accept()
s.process()
