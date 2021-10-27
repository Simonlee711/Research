%% Majid Farzaneh: majid.farzaneh91@gmail.com
% graph-coloring problem, solved by genetic algorithm.
clc
clear 
close all
%% Input Graph:
N_nodes=input('Enter Number of Nodes:');
N_Colors=input('Enter Number of Colors:');
G=zeros(N_nodes);
type=input('Graph Type: Custom(1) / Random(2)?');
if type==1
    % Custom Graph:
    for i=1:N_nodes
        for j=i:N_nodes
            if i~=j
                connectivity=input(['Is there a link between nodes ',num2str(i),' and ',num2str(j), ' ? (0/1) : ']);
                if connectivity==1
                    G(i,j)=1;
                    G(j,i)=1;
                end
            end
        end
    end
else
    % Random Graph:
    for i=1:N_nodes
        for j=i:N_nodes
            if i~=j
                if rand>0.5
                    G(i,j)=1;
                    G(j,i)=1;
                end
            end
        end
    end
end
%% Drawing Graph:
position=randsrc(2,N_nodes,1:1000); 
figure(1),
plot(position(1,:),position(2,:),'o');
title('Input Graph');
hold on
for i=1:N_nodes
    for j=1:N_nodes
        if G(i,j)==1
             line([position(1,i),position(1,j)],[position(2,i),position(2,j)]);
        end
    end
end
hold off
%% Genetic Initialization
Npop=100; % Number of population
MaxGeneration=1000; 
for i=1:Npop
    chromosome{i}=make_a_sol(N_nodes,N_Colors);
end
%% Genetic Optimization:

for iter=1:MaxGeneration
    for i=1:Npop
        costs(i)=cost_fcn(chromosome{i},G,N_Colors);
    end
    [best(iter),bestIDX]=min(costs);
    bestsol=chromosome{bestIDX};
    if best(iter)==0
        disp('--------------------------------');
        disp('Problem Converged Successfully!');
        break;
    end
    figure(2),
    plot(iter,best(iter),'ro')
    title('Genetic Convergence');
    xlabel('Iteration #')
    ylabel('Cost')
    grid()
    hold on
    pause(0.001);
    [~,sortIDX]=sort(costs);
    bests=sortIDX(1:Npop/2);
    for i=1:2:numel(bests)
        parent1=chromosome{bests(i)};
        parent2=chromosome{bests(i+1)};
        child1=crossover(parent1,parent2);
        child1=mutation(child1,N_Colors);
        child2=crossover(parent2,parent1);
        child2=mutation(child2,N_Colors);
        chromosome{sortIDX(end-i+1)}=child1;
        chromosome{sortIDX(end-i)}=child2;
    end
    if iter==MaxGeneration
        disp('Maximum Number of Generation Reached!');
        if best(iter)>0
            disp('---------------------------------------------------------');
            disp('Input Graph and input number of colors has cost for GCP');
        end
    end
end
bestsol
%% Create Color Table:
w=9;
Color={[0 0 0],[0 0 1],[0 1 0],[0 1 1],[1 0 0],[1 0 1],[1 1 0],[1 1 1]};
stepsize=0.1;
for i=0.1:stepsize:0.9
    for j=0.1:stepsize:0.9
        for k=0.1:stepsize:0.9
            Color{w}=[i j k];
            w=w+1;
        end
    end
end
%% Drawing Colored Graph:
figure(3),
for i=1:N_nodes
    for j=1:N_nodes
        if G(i,j)==1
             line([position(1,i),position(1,j)],[position(2,i),position(2,j)]);
             hold on
        end
    end
end
for i=1:N_nodes  
    plot(position(1,i),position(2,i),'o','MarkerFaceColor',Color{bestsol(i)},'MarkerEdgeColor',Color{bestsol(i)},'MarkerSize',11);
    text(position(1,i),position(2,i),num2str(bestsol(i)),'color','r')
    hold on
end
title('Colored Graph');