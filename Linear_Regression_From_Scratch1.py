
X=[2,5,8,13,15,16,20,18,21,24,26]
Y=[5,8,9,15,18,20,23,21,25,28,29]
theta0=0
theta1=1


i=0
while i<1000:
    dJ0= []
    dJ1= []
    for (x, y) in zip(X, Y):
        dJ0.append((theta0+theta1*x+y)/11)
        dJ1.append(((theta0+theta1*x-y)*x)/11)
        k=sum(dJ0)
        l=sum(dJ1)
        theta0=theta0-.01*k
        theta1=theta1-.01*l
    i=i+1
print(theta1,theta0)




