m = 10; % massan klader
M = 20; % massan utan klader
r = 0.25; % radius
k = 1000; % spring
c = 15; % damper
w = 250*2*pi/60; % rpm
w_n = sqrt(k/(M+m)); % naturlig frekvens
xi = c/(2*w_n*(M+m)); % weird greek symbol
X = ((m/(M+m))*r*w^2)/(sqrt((w_n^2-w^2)^2+(2*xi*w_n*w)^2)); % amplitud
a = atan((2*w_n*w)/(w_n^2-w^2)); % fas vinkeln
t = 1:0.01:10; % tid punkter
y = X*sin(w*t-a);
F_Y_stat = abs(k*X*sin(w*t-a)+c*X*cos(w*t-a));
F_X_stat = abs(m*cos(w*t)*w^2*r);
% plot(t,y);
plot(t,F_X_stat)

