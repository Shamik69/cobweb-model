n=0;
x0=0;
p0=[];
p1=[];
t= [];
a0=1;
b0=-2;
a1=-0.5;
b1=1.95;
while n<=500
    p0(length(p0)+1)= x0;
    x1= ((a1 - a0) + (b1 .* x0))/b0;
    p1(length(p1)+1)= x1;
    t(length(t)+1)=n;
    if round(x0, 2)== round(x1, 2)
        break
    end
    x0=x1;
    n= n+1;
end
length(t)
dd = a0 + b0 .* p1;
ss = a1 + b1 .* p0;
pp = -((a0 - a1) / (b0 - b1));
time_path = ((10 - pp) .* ((b0 / b1) .^ t)) + pp;

fig1= figure(1);
plot(t, time_path)
xlabel('periods')
ylabel('time path')
saveas(fig1,'C:/Users/User/PycharmProjects/cobweb-model/figs/periods-time path(matplotlib).png')

fig2= figure(2);
plot(t, dd)
xlabel('periods')
ylabel('demand')
saveas(fig2,'C:/Users/User/PycharmProjects/cobweb-model/figs/periods-demand(matplotlib).png')

fig3= figure(3);
plot(t, p1)
xlabel('periods')
ylabel('price')
saveas(fig3,'C:/Users/User/PycharmProjects/cobweb-model/figs/periods-price(matplotlib).png')

fig4= figure(4);
plot(time_path, p1)
ylabel('price')
xlabel('time path')
saveas(fig4,'C:/Users/User/PycharmProjects/cobweb-model/figs/time path-price(matplotlib).png')

fig5= figure(5);
plot(time_path, dd)
ylabel('demand')
xlabel('time path')
saveas(fig5,'C:/Users/User/PycharmProjects/cobweb-model/figs/time path-demand(matplotlib).png')