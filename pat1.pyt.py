class display:
    def accept(self):
        self.i=int(input("enter initial val;ues"))
        self.f=int(input("ebnter final valyues of numbers"))
    def process(self):
        while self.i<=self.f:
            print(self.i,end=' ')
            self.i=self.i+1
d=display()
d.accept()
d.process()
            
