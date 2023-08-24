B_0 = [1,-0.3,-0.3,-0.4;
-0.3,1,0,-0.7;
-0.3,0,0.9,-0.6;
-0.4,-0.7,-0.6,1.7]*1e-3;
B_1 = [0.3 0.3 -0.2 -0.4;
0.3 0.3 -0.4 -0.2;
-0.2 -0.4 0.1 0.5;
-0.4 -0.2 0.5 0.1]*1e-3;

r = @(eta) r_mat(B_0 + eta.*B_1);
P = @(x) 1+10.*(x./1000).^2;
P_tot = @(eta) sum(P(r(eta)));
tol =1e-10;
iterationer = 0;
gs = (sqrt(5)+1)/2;
a = 0;
b = 1;
while abs(b-a)>tol
    c = b-(b-a)/gs;
    d = a+(b-a)/gs;
    if P_tot(c) < P_tot(d)
        b = d;
    else
        a = c;
    end
    iterationer= iterationer+1;
end
los = (b+a)/2;
felkvadratsumman = norm(F(1./r(los),B_0+los.*B_1))^2;

display(felkvadratsumman);
display(iterationer)
display(los)