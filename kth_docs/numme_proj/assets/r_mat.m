function r_sol= r_mat(input)
S_0 = input;
k = ones(1,5); % initial guess
tol = 1e-15;
felfel = 1;
while felfel>tol
    fel_1 = norm(F(k,S_0));
    JX = J(k,S_0);
    FX = F(k,S_0);
    d = (JX'*JX)\(JX'*FX);
    k = k-d';
    fel_2 = norm(F(k,S_0));
    felfel = abs(fel_2-fel_1);
end
r_sol=1./k;
end