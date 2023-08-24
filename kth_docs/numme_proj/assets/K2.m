function Kirs = K(k)
if width(k) ~= 5 && length(k)~=1
    error('size of k must be a 1x5 vector');
end
n = 6;
km = zeros(n);
km(1,5) = k(1);
km(5,1) = k(1);
km(2,6) = k(2);
km(6,2) = k(2);
km(5,6) = k(3);
km(6,5) = k(3);
km(3,5) = k(4);
km(5,3) = k(4);
km(4,6) = k(5);
km(6,4) = k(5);
Kirs = zeros(n,n);
for i=1:n
    for j=1:n
        if j==i
            Kirs(i,j) = sum(km(i,:)) - km(i,j);
        else
            Kirs(i,j) = -km(i,j);
        end
    end
end
end

