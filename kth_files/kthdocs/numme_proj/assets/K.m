function Kirs = K(k)
n = length(k);
Kirs = zeros(n,n);
for i=1:n
    for j=1:n
        if j==i
            Kirs(i,j) = sum(k(i,:)) - k(i,j);
        else
            Kirs(i,j) = -k(i,j);
        end
    end
end
end

