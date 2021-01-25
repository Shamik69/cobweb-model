x= [];
y= [];
i=1;
while i<= length(price)
    x(length(x)+1)= price(i).*timepath(i);
    y(length(y)+1)= quantity(i).*timepath(i);
    
end
scatter(x, y)