N<- 500
p0<- seq(0,0)
p1<- seq(0,0)
t<- seq(0,0)
a0=1
b0=-2
a1=-0.5
b1=1.95
x0<- 0
for (i in seq(1, N)){
 p0[i]<- x0
 x1<- ((a1 - a0) + (b1 * x0))/b0
 p1[i]<- x1
 t[i]<- i
 if (round(x0,2)==round(x1,2)){
   break
 }
 x0<- x1
}
dd = a0 + b0 * p1
ss = a1 + b1 * p0
pp = -((a0 - a1) / (b0 - b1))
time_path = ((p0 - pp) * (b0 / b1) ** t) + pp
length(dd)
plot(t, time_path,'l', col = "#2E9FDF", ylab= 'time path', xlab=' period')
