function C=cost_fcn(chromosome,G,N_Colors)
    C=0;
    for i=1:N_Colors
        if sum(i==chromosome)==0
            C=inf;
            return;
        end
    end   
    for i=1:size(G,1)
        for j=1:size(G,2)
            if G(i,j)==1
                if chromosome(i)==chromosome(j)
                    C=C+1;
                end
            end
        end
    end
    
end