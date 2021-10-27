function C=make_a_sol(N_nodes,N_Colors)
    C=[randperm(N_Colors) , randsrc(1,N_nodes-N_Colors,1:N_Colors)] ;
end