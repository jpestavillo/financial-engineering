function biseccion
f = input('Ingresa la función','s')
x0= input('Ingresa el valor de x0')
x1= input('Ingresa el vaor de x1')
error= input('Ingresa el error')

m(1,1) = 0
m(1,2) = x0
m(1,3) = x1
xm= (x0+x1)/2
m(1,4) = xm
x = xm
y = eval(f)
m(1,5) = y
m(1,6) = 1



if m(1,5) > 0
   m(2,2) = m(1,2)
   m(2,3) = m(1,4)   
   elseif m(1,5)<0
   m(2,2) = m(1,4)
   m(2,3) = m(1,3)
end


xm = (m(2,1)+m(2,2))/2
x = xm
y = eval(f)
m(2,4) = x
m(2,5)= y
error_a = abs(m(2,5)-m(1,5))
m(2,6)=error_a



i = 1

j = 1

while error_a > error

    m(i, j) = i -1

    if m(1,5)>0

        m(i,2) = m((i-1),2)

        m(i,3) = m((i-1),4)

    else

        if m(i,5)<0

            m(i,2) = m((i-1),4)

            m(i,3) = m((i-1),3)

        end

    end
end
 xm = (m(i,2)+m(i,3))/2

 x =xm

 y = eval(fun)

 m(i,4) = x

 m(i,5) = y

 error_a = abs(m(i-5-m(i,5)))

 m(i,6)= error_a

 i = i + 1

 j = j + 1
 
 
 
