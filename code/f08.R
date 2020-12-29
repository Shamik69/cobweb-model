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
png(filename = 'C:/Users/User/PycharmProjects/cobweb-model/figs/periods-time path(Rplot).jpg',
    width=600, height=350)
plot(t, time_path,'l', xlab= 'periods', ylab= 'time path', col = "#2E9FDF")
dev.off()

png(filename = 'C:/Users/User/PycharmProjects/cobweb-model/figs/periods-quantity(Rplot).jpg',
    width=600, height=350)
plot(t, dd,'l', xlab= 'periods', ylab='quantity', col = "#2E9FDF")
dev.off()

png(filename = 'C:/Users/User/PycharmProjects/cobweb-model/figs/periods-price(Rplot).jpg',
    width=600, height=350)
plot(t, p1,'l', xlab='periods', ylab='price', col = "#2E9FDF")
dev.off()

png(filename = 'C:/Users/User/PycharmProjects/cobweb-model/figs/time path-demand(Rplot).jpg',
    width=600, height=350)
plot(time_path, p1,'l', ylab= 'price', xlab='time path', col = "#2E9FDF")
dev.off()

png(filename = 'C:/Users/User/PycharmProjects/cobweb-model/figs/time path-demand(Rplot).jpg',
    width=600, height=350)
plot(time_path, dd, 'l', xlab = 'time path', ylab= 'demand',col = "#2E9FDF")
dev.off()
