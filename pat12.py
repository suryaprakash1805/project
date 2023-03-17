#program to check the no is armstrong or not
class display:
    def __init__(self):
        self.count=0
        self.sum=0
    def accept(self):
        self.n=int(input("enhter a number:"))
        self.num=self.n
        self.value=self.n
    def process(self):
        while self.n!=0:
            self.count=self.count+1
            self.n=self.n//10
    def output(self):
        while self.num!=0:
            r=self.num%10
            self.sum=self.sum+r**self.count
            self.num=self.num//10
    def result(self):
        if self.value==self.sum:
            print(self.value,"is armstrong")
        else:
            print(self.value,"is not armstrong")
s=display()
s.accept()
s.process()
s.output()
s.result()
