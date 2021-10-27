function new_child=mutation(child,N_Colors)
    new_child=child;
    if rand>0.5
        new_child(randperm(numel(child),1))=randsrc(1,1,1:N_Colors);
    end
end