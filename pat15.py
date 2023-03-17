#program to find gcd of two numbers\
class gcd:

     def accept(self):
        self.a=int(input("enter a number"))
        self.b=int(input("enter a number"))
     def process(self):
        while(self.a!=self.b):
             if(self.a>self.b):
                self.a=self.a-self.b
             else:
                self.b=self.b-self.a
     def output(self):
          print("the gcd of two numbers is ",self.a)
s=gcd()
s.accept()
s.process()
s.output()
