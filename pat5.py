#to t=cjeck the no divisible 2 and 5
class new:
    def accept(self):
        self.i=int(input("enterba valyes"))
    def process(self):
        if(self.i%2==0 and self.i%5==0):
            print("the number is divible",self.i)
        else:
            print("not divisible")
d=new()
d.accept()
d.process()
