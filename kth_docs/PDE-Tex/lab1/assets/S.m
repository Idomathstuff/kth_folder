function Resp = S(k)
n = length(k);
m = 4;
Kirs = K(k);
K_1_1 = Kirs(1:m,1:m);
K_1_2 = Kirs(1:m,m+1:n);
K_2_1 = Kirs(m+1:n,1:m);
K_2_2 = Kirs(m+1:n,m+1:n);
Resp = (K_1_1-K_1_2*inv(K_2_2)*K_2_1);
end

