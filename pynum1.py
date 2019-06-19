#!/usr/bin/python3

import numpy as np
for i in range(2):
  r=int(input("enter a no. of row...>>"))
  c=int(input("enter no.of columns...>>"))
  q=np.random.randint(low=1,high=10,size=(r,c))
  print(q)
  n=input("enter name of file..")
  np.savetxt(n,q)
  np.loadtxt(n)
