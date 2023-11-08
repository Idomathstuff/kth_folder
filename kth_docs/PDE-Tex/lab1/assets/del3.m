Sn1 = [1.10;-0.18;-0.38;-0.57];
Sn2 = [-0.19;1.11;-0.16;-0.8];
Sn3 = [-0.37;-0.15;0.95;-0.42];
Sn4 = [-0.55;-0.77;-0.40;1.75];
S_0 = [Sn1 Sn2 Sn3 Sn4]*1e-3;
k = ones(1,5); % initial guess
tol = 1e-15;
felfel = 1;
iterationer = 0;
while felfel>tol
    fel_1 = norm(F(k,S_0));
    JX = J(k,S_0);
    FX = F(k,S_0);
    d = (JX'*JX)\(JX'*FX);
    k = k-d';
    fel_2 = norm(F(k,S_0));
    felfel = abs(fel_2-fel_1);
    iterationer = iterationer+1;
end
r = 1./k;
display(k);
display(r);
display(iterationer)