import matplotlib.pyplot as ptimport numpy as npl=int(input("enter the no of samples:"))x=np.zeros(l)for i in range(l):	x[i]=int(input("enter"))print (x)l=len(x)y=[ ]for n in range(0,l):	y=np.append(y,x[l-n-1])print(y)