Sn1 = [1.10;-0.18;-0.38;-0.57];
Sn2 = [-0.19;1.11;-0.16;-0.8];
Sn3 = [-0.37;-0.15;0.95;-0.42];
Sn4 = [-0.55;-0.77;-0.40;1.75];
S_0 = [Sn1 Sn2 Sn3 Sn4]*1e-3;
tol = 1e-15;
r_skatt = r_mat(S_0);
total_fel = 0;
for i=1:4
    for j=1:4
        felm = zeros(4); %"fel" matris
        felm(i,j) = S_0(i,j)*0.02;
        r_exp = r_mat(S_0+felm);
        total_fel= total_fel +abs(r_exp-r_skatt);
    end
end
display(total_fel)