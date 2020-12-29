t= [1:1:10];
a0=1;
b0=-2;
a1=-0.5;
b1=1.95;
p0={};
p1={};
n= 100;
while n>0
    p0(length(p0)+1)= x0;
    x1= ((a1 - a0) + (b1 .* x0))/b0;
    p1(length(p0)+1)= x0;
    x0=x1;
    n= n-1;
end
pp = -((a0 - a1) / (b0 - b1));
time_path = ((10 - pp) .* ((b0 / b1) .^ t)) + pp;
dd = a0 + (b0 .* p1);
ss = a1 + (b1 .* p0);
plot(time_path, dd)
    