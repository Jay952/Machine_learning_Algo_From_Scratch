X=[-12,-10,-8,-5,-2,-1,-.75,-.5,0,1,2,5,8,13,15]
Y=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
theta0=8
theta1=1


i=0
while i<100:
    dJ0= []
    dJ1= []
    for (x, y) in zip(X, Y):
        dJ0.append(((1/(1+pow(2.718,x)))-y)*x)
        dJ1.append(((1/(1+pow(2.718,x)))-y)*x)
        k=sum(dJ0)
        l=sum(dJ1)
        theta0=theta0-.01*k
        theta1=theta1-.01*l
    i=i+1
print(theta1,theta0)
