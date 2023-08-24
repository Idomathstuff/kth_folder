function JX = J(x,S_0)
ksize = 5;
h = 1e-10;
JX = zeros(length(F(x,S_0)),ksize); %16x1 vector function, 5 derivatives
for j=1:ksize
        hm = zeros(1,ksize); % hm = h matrix
        hm(j) = h;
        Fd = (F(x+hm,S_0)-F(x-hm,S_0))./h;
        JX(:,j) = Fd;
end
end