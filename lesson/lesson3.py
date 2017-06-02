class A:
    def sayhi(self):
        print('I am A hi')
class B:
    def sayhi(self):
        print('I am B Hi')
class C(A,B):
    def sayhi(self):
        print ('I am C hi')
        super().sayhi()
    pass

class D(A,B):
    def sayhi(self):
        print ('I am C hi')
        super().sayhi()
    pass
d=A()
d.sayhi()
B.sayhi(d)
A.sayhi(d)


