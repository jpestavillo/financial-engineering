function gauss_villo
fx=input('enter f(x):','s')
fy=input('enter f(y):','s')
fz=input('enter f(z):','s')
era= input('ingresa el error a alcanzar')
i=2
x=0
y=0
z=0
iteracion=0
M(1,1)=i
M(1,2)=x
M(1,3)=y
M(1,4)=z
M(1,5)=1
M(1,6)=1
M(1,7)=1
i=2
erx=1
ery=1
erz=1
i=2
while erz>era
M(i,1)=iteracion

x=eval(fx)
y=eval(fy)
z=eval(fz)

M(i,2)=eval(fx)
x=M(i,2)
M(i,3)=eval(fy)
y=M(i,3)
M(i,4)=eval(fz)
z=M(i,4)

erx=abs((M(i,2)-M(i-1,2))/M(i,2))
ery=abs((M(i,3)-M(i-1,3))/M(i,3))
erz=abs((M(i,4)-M(i-1,4))/M(i,4))
M(i,5)=erx
M(i,6)=ery
M(i,7)=erz
i=i+1

end

end