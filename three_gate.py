# -*- coding: utf-8 -*-


import numpy as np
times=100000

x=np.random.choice(3,times)
print(x.shape)
print(x)

a=np.zeros((times,3))
a[range(times),x]=1

y=np.random.choice(3,times)
b=np.zeros((times,3))
b[range(times),y]=1
print(y.shape)
print(b)
print(b.shape)

p1=np.sum((a+b)==2)/times
print('原始获奖几率：'+str(p1))


c=np.argmin(a+b,axis=1)
d=np.zeros((times,3))
d[range(times),c]=1
e=np.ones((times,3))
f=e-b-d
p2=np.sum((a+f)==2)/times
print(type(p2))
print('改变之后的获奖几率：'+str(p2))



z=np.random.choice(3,times)
h=np.zeros((times,3))
h[range(times),x]=1
h[range(times),z]=0
p3=np.sum((a+h)==2)/times
print('中奖的几率：'+str(p3))
