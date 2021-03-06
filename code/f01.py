# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fD0UgR-I-82CoJQjvfmd_4wMfcL58TAG
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

x0= sym.symbols('x0')
a0= sym.symbols('a0')
a1= sym.symbols('a1')
b0= sym.symbols('b0')
b1= sym.symbols('b1')
p0= sym.symbols('p0')
t= sym.symbols('t')
x1= (a1- a0)- (b1/b0)*x0
dd= a0+ b0*x1
ss= a1 + b1*x0
pp= -((a0-a1)/(b0-b1))
time_path_fn= ((p0- pp)*(b0/b1)**-t)+ pp

time_path=[]
solve= []
t1= list(range(1, 100))
x= 0
bi_pasa0= []
bi_pasa1= []
d=[]
s=[]

for i in t1:
  values= [2, -2, 5, 1.5, 4]
  x_1= x1.subs([(x0, x), (a0, values[0]), (b0, values[1]), (a1, values[2]), (b1, values[3])])
  op= time_path_fn.subs([(x0, x), (a0, values[0]), (b0, values[1]), (a1, values[2]), (b1, values[3]), (p0, values[4]), (t, i)])
  time_path.append(op)
  d.append(dd.subs([(x1, x_1), (a0, values[0]), (b0, values[1]), (a1, values[2]), (b1, values[3])]))
  s.append(ss.subs([(x0, x), (a0, values[0]), (b0, values[1]), (a1, values[2]), (b1, values[3])]))
  bi_pasa0.append(x)
  bi_pasa1.append(x_1)
  x= x_1
plt.plot(t1, time_path, label= 'time path')
plt.legend()
plt.show()
plt.plot(t1, bi_pasa0, label= 'price')
plt.legend()
plt.show()
plt.plot(time_path, d)
plt.plot(time_path, s)
plt.show()