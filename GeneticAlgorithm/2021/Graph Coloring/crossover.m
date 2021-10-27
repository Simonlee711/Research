function child=crossover(parent1,parent2)
    cross_point=round(numel(parent1)/2);
    child=parent1;
    child(cross_point:end)=parent2(cross_point:end);
end