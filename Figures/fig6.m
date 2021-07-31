% -------------------------------------------------------------------------
% This script reproduces fig. 3 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure 6')
disp('    ')
disp('***********')

clear; 


%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE 6B %%%%%%%%
% open figure
fh = figure; box off;
set(fh, 'Position', [0 1200 1250 450], 'Color', 'white');

map = brewermap(15,'*RdBu');

ax = subplot(1,2,1); hold on
% load data
T = readtable('fig6b-r.csv','ReadVariableNames',true);
s = 15; 
% plot data points
s1 = scatter(T.MF_m1+0.05*randn(length(T.MF_m1),1),T.MF_m2+0.05*randn(length(T.MF_m2),1),s,real(exp(1 -T.BL/max(T.BL)).^2.5/10),'o','filled');
colormap(map)
c1 = colorbar; c1.Label.String = 'Learning speed';
set(gca,'xlim',[-.2 1.2],'ylim',[-.2 1.2],'xtick',[0 0.1 0.9 1],'ytick',[0 0.1 0.9 1])
xlabel('p(Feature RL)')
ylabel('p(Abstract RL)')
title('Relevant')

pout = myBinomTest(sum(T.MF_m2>.5),length(T.MF_m2),.5);
fprintf('All blocks pooled, binomial test, P(%d|%d)= %.2f \n',sum(T.MF_m2>.5),length(T.MF_m2),pout)

% 
ax = subplot(1,2,2); hold on
T = readtable('fig6b-i.csv','ReadVariableNames',true);

% plot data points
s1 = scatter(T.MF_m1+0.05*randn(length(T.MF_m1),1),T.MF_m2+0.05*randn(length(T.MF_m2),1),s,real(exp(1 -T.BL/max(T.BL)).^2.5/10),'o','filled');
colormap(map)
c1 = colorbar; c1.Label.String = 'Learning speed';
set(gca,'xlim',[-.2 1.2],'ylim',[-.2 1.2],'xtick',[0 0.1 0.9 1],'ytick',[0 0.1 0.9 1])
xlabel('p(Feature RL)')
ylabel('p(Abstract RL)')
title('Irrelevant')

pout = myBinomTest(sum(T.MF_m2>.5),length(T.MF_m2),.5);
fprintf('All blocks pooled, binomial test, P(%d|%d)= %.2f \n',sum(T.MF_m2>.5),length(T.MF_m2),pout)




%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE 6C %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 650 450], 'Color', 'white');

% load data
T = readtable('fig6c.csv','ReadVariableNames',true);

clrs = [.203 .761 .787;
        .193 .471 .223;
        .293 .671 .123];
    
v = violinplot([T.pmsl T.pmsr T.pmsi]);
for i = 1:3
    v(i).ViolinColor = clrs(i,:);
    v(i).ScatterPlot.CData = clrs(i,:);
end
set(gca,'ylim',[.2 1.0],'ytick',.3:.1:.9,'xticklabel',{'Before' 'After (R)' 'After (I)'});
ylabel('proportion Abstract RL')

[P(1),~,STATS(1)] = signrank(T.pmsl,T.pmsr, 'method', 'approximate');
[P(2),~,STATS(2)] = signrank(T.pmsl,T.pmsi, 'method', 'approximate');
[P(3),~,STATS(3)] = signrank(T.pmsi,T.pmsr, 'method', 'approximate');
disp(['Late vs Relevant, ranksum test, z = ' num2str(STATS(1).zval,2) ', p = ' num2str(P(1),3)])
disp(['Late vs Irrelevant, ranksum test, z = ' num2str(STATS(2).zval,2) ', p = ' num2str(P(2),3)])
disp(['Relevant vs Irrelevant, ranksum test, z = ' num2str(STATS(3).zval,2) ', p = ' num2str(P(3),3)])

plot([1 2], [.97 .97], 'k-');
plot([1 3], [.91 .91], 'k-');
plot([3.2 3.2], [.91 .97], 'k-');
plot([3.15 3.2], [.91 .91], 'k-');
plot([3.15 3.2], [.97 .97], 'k-');
if P(1)<.05; text(1.45,.98,'*','FontSize',16); else; text(1.40,.98,'n.s.','FontSize',10); end
if P(2)<.05; text(1.95,.93,'*','FontSize',16); else; text(1.90,.93,'n.s.','FontSize',10); end
if P(3)<.05; text(3.22,.93,'*','FontSize',16); else; text(3.22,.94,'n.s.','FontSize',10); end



%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE 6D %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 650 450], 'Color', 'white');

% load data
T = readtable('fig6d.csv','ReadVariableNames',true);

histogram(T.v_r,'normalization','pdf','EdgeColor','none','FaceColor',[.193 .471 .223])
histogram(T.v_i,'normalization','pdf','EdgeColor','none','FaceColor',[.293 .671 .123])
set(gca,'xlim',[-.35 .15],'xtick',-.3:.1:.1,'ylim',[0 20],'ytick',0:5:20)
xlabel('p(Feature RL) - p(Abstract RL)')
ylabel('density')

P_r = sum(T.v_r > 0)/length(T.v_r) * 2;
P_i = sum(T.v_i < 0)/length(T.v_i) * 2;

disp(['Bootstrap relevant: p = ' num2str(P_r,3)])
disp(['Bootstrap irrelevant: p = ' num2str(P_i,3)])



