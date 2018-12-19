from math import sqrt
c = 50
h = 30
d=input().split(',')
q=[]
type(d)
for i in d:
    v = sqrt((2*c*int(i))/h)
    q.append(int(v))
print(q)
