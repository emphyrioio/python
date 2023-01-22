class A:
    A = 1
    _B = 2


a = A()
A._B = 3
print(A.A)
print(A._B)
