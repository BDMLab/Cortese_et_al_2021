% -------------------------------------------------------------------------
% This script reproduces fig. 3 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure 3')
disp('    ')
disp('***********')

clear;


%%
%%%%%%% FIGURE 3A %%%%%%%%

T = readtable('fig3a-1.csv'); 


% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 850 450], 'Color', 'white');

% color 
fc = [.205 .728 .819;
      .176 .192 .401];

% create subplot for model values
ax = subplot(1,3,1:2); hold on;

hn = 15; fa = 0.30; krn = 0.05; %0.035 for no noise case
x = 0:.01:1;

% reformat data
L_8s = T.L_8s; L_4s = T.L_4s;
L_8s(L_8s == 80) = []; L_4s(L_4s == 80) = [];
L_8s = 1 - L_8s/80; L_4s = 1 - L_4s/80;

h(1)    = histogram(L_4s, hn, 'normalization', 'pdf', 'FaceAlpha', fa, 'LineStyle', 'none', 'FaceColor', fc(2,:)); 
ksd     = fitdist(L_4s, 'Kernel', 'Width', krn);
pdf_k   = pdf(ksd, x);
p(1)    = plot(x, pdf_k, 'LineWidth', 1.5, 'Color', [h(1).FaceColor .6]); 
h(2)    = histogram(L_8s, hn, 'normalization', 'pdf', 'FaceAlpha', fa, 'LineStyle', 'none', 'FaceColor', fc(1,:));
ksd     = fitdist(L_8s, 'Kernel', 'Width', krn);
pdf_k   = pdf(ksd, x);
p(2)    = plot(x, pdf_k, 'LineWidth', 1.5, 'Color', [h(2).FaceColor .6]);

% axis params
set(ax, 'xlim', [0 1], 'xtick', 0:.2:1, 'ylim', [0 3.75], 'ytick', 0:.75:4)
xlabel('Learning speed', 'FontWeight', 'bold'); ylabel('pdf', 'FontWeight', 'bold');
% legend
legend(p,{'Abstract RL' 'Feature RL'},'Box','off','location','northwest')

% statistical tests
clear P STATS
[P,~,STATS] = ranksum(L_4s, L_8s);
disp('difference in learning speed distributions')
disp(['Stats F vs A, ranksum Z = ' num2str(STATS.zval) ', p = ' num2str(P)])


% create subplot for subject values
ax = subplot(1,3,3); hold on

T = readtable('fig3a-2.csv'); 
p8s = T.p8s; p4s = T.p4s;
simS = length(p8s);

bs = .8;
bar(2, mean(p8s), bs, 'FaceColor', fc(1,:), 'FaceAlpha', fa, 'EdgeColor','none')
errorbar(2, mean(p8s), std(p8s)/sqrt(simS), 'Color', 'k')
bar(1, mean(p4s), bs, 'FaceColor', fc(2,:), 'FaceAlpha', fa, 'EdgeColor','none')
errorbar(1, mean(p4s), std(p4s)/sqrt(simS), 'Color', 'k')

% statistical tests
clear P STATS
[P,~,STATS] = ranksum(p8s,p4s);

% add line and * for significance
y = max([mean(p8s) mean(p4s)])+(std(p8s)/sqrt(simS))+ 0.002;
plot([1 2],[y y],'k')

if P < 0.05; text(1.45, y + .0015, '*', 'FontSize', 14); else; text(1.2, y + .0015, 'n.s', 'FontSize', 16); end

disp('difference in failed block percentage')
disp(['Stats F vs A, ranksum Z = ' num2str(STATS.zval) ', p = ' num2str(P)])

% axis params
set(ax, 'xlim', [0 3], 'xtick', [], 'ylim', [0 0.021], 'ytick', 0:.01:.055)
ylabel('p(failed blocks)', 'FontWeight', 'bold');



%%
% ----------------------------------------------------------------------- %
% load data
T = readtable('fig3b-1.csv','ReadVariableNames',true);

%%%%%%% FIGURE 3B %%%%%%%%
% open figure
fh = figure; box off;
set(fh, 'Position', [0 1200 950 450], 'Color', 'white');

ax = subplot(1,5,1:3); hold on
s = 15; 
map = brewermap(15,'*RdBu');
% plot data points
s1 = scatter(T.MF_m1+0.05*randn(length(T.MF_m1),1),T.MF_m2+0.05*randn(length(T.MF_m2),1),s,real(exp(1 -T.BL/max(T.BL)).^2.5/10),'o','filled');
colormap(map)
c1 = colorbar; c1.Label.String = 'Learning speed';
set(gca,'xlim',[-.2 1.2],'ylim',[-.2 1.2],'xtick',[0 0.1 0.9 1],'ytick',[0 0.1 0.9 1])
xlabel('p(Feature RL)')
ylabel('p(Abstract RL)')

pout = myBinomTest(sum(T.MF_m2>.5),length(T.MF_m2),.5);
fprintf('All blocks pooled, binomial test, P(%d|%d)= %.2f \n',sum(T.MF_m2>.5),length(T.MF_m2),pout)

% 
ax = subplot(1,5,5); hold on
T = readtable('fig3b-2.csv','ReadVariableNames',true);

clrs = [.293 .761 .587];
plot([.55 1.45],[.5 .5],'k-.')
v = violinplot(T.pms);
v(1).ViolinColor = clrs;
v(1).ScatterPlot.CData = clrs;
set(ax,'xlim',[0.5 1.5],'ylim',[.3 .66],'ytick',.35:.075:.65,'xticklabel','');
ylabel('proportion Abstract RL')

[~,P,CI,STATS] = ttest(T.pms,.5);
fprintf('Group level t-test, t(%d)=%.2f, p=%.3f, CI=[%.2f %.2f] \n',STATS.df,STATS.tstat,P,CI(1),CI(2))




%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 3C %%%%%%%%
% open figure
fh = figure; box off;
set(fh, 'Position', [0 1200 1050 450], 'Color', 'white');

% plot abstraction vs learning speed
ax = subplot(1,2,1); hold on
% load data
T = readtable('fig3c.csv','ReadVariableNames',true);

scatter(T.abstraction-1, T.learningspeed, 50,[.3 .3 .3],'filled')
l = lsline;
set(l,'LineWidth',1,'Color',[0 0 0]);
ylabel('Learning speed'); xlabel('Abstraction level')
set(ax,'FontName','Helvetica', 'FontSize', 12,'xtick', 0.3:.05:0.6, 'ytick', .55:.05:.75);
[a,b] = robustfit(T.abstraction, T.learningspeed);
disp('Robust regression abstraction vs learning speed')
disp(['y = ' sprintf('%.3f', a(1)) ' + ' sprintf('%.3f', a(2)) 'x'])
disp(['t = ' sprintf('%.2f', b.t(2))])
disp(['p = ' num2str(b.p(2),3)])
disp(['df = ' num2str(b.dfe)])

% plot confidence vs abstraction 
ax = subplot(1,2,2); hold on
scatter(T.confidence, T.abstraction-1, 50,[.3 .3 .3],'filled')
l = lsline;
set(l,'LineWidth',1,'Color',[0 0 0]);
xlabel('Confidence'); ylabel('Abstraction level')
set(ax,'FontName','Helvetica', 'FontSize', 12,'ytick', 0.3:.05:0.6, 'xtick', 3:1:9,'xlim',[3.5 8.5]);
[a,b] = robustfit(T.confidence, T.abstraction);
disp('Robust regression confidence vs abstraction')
disp(['y = ' sprintf('%.3f', a(1)) ' + ' sprintf('%.3f', a(2)) 'x'])
disp(['t = ' sprintf('%.2f', b.t(2))])
disp(['p = ' num2str(b.p(2),3)])
disp(['df = ' num2str(b.dfe)])




%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 3D %%%%%%%%
% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 750 450], 'Color', 'white');

ax = subplot(2,3,[1 2 4 5]); hold on;

% load data
T = readtable('fig3d.csv','ReadVariableNames',true);

s = 15; a = .3;
% plot data points
s1 = scatter(T.LR_m1, T.LR_m2, s, [.3 .3 .3], 'o', 'filled');
plot([.05 .9],[.05 .9],'k-.')
set(ax,'xlim',[0 1],'ylim',[0 1],'xtick',0:.2:1,'ytick',0:.2:1)
xlabel('\alpha_{Feature RL}')
ylabel('\alpha_{Abstract RL}')
title('Learning rate')

% compute histogram of distance from diagonal
ax = subplot(2,3,3); hold on;

h = histogram((T.LR_m1-T.LR_m2)/sqrt(2), 'normalization','pdf','FaceAlpha',a,'EdgeColor','none','FaceColor',[.2 .2 .2]);
plot([0 0],[0 max(h.Values)+.25],'k')
plot([median(h.Data) median(h.Data)],[0 max(h.Values)+.25],'k-.')
ax.YLim = [0 max(h.Values)+1]; ax.YAxis.Visible = 'off';

[P,~,STATS] = signrank(h.Data);
disp(['Ranksum Z = ' sprintf('%.2f', STATS.zval) ', p = ' num2str(P,3)])

if P<.05; text(median(h.Data)-.0115,max(h.Values)+.5,'*','fontsize',16); end




%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 3E %%%%%%%%
% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 750 450], 'Color', 'white');

ax = subplot(2,3,[1 2 4 5]); hold on;

% load data
T = readtable('fig3e.csv','ReadVariableNames',true);

s = 15; a = .3;
% plot data points
s1 = scatter(T.St_m1,T.St_m2,s,[.3 .3 .3],'o','filled');
plot([.0 7.5],[.0 7.5],'k-.')
set(ax,'xlim',[0 8],'ylim',[0 8],'xtick',0:2:8,'ytick',0:2:8)
xlabel('\beta_{Feature RL}')
ylabel('\beta_{Abstract RL}')
title('Greediness')

% compute histogram of distance from diagonal
ax = subplot(2,3,3); hold on;
h = histogram((T.St_m1-T.St_m2)/sqrt(2), 'normalization','pdf','EdgeAlpha',a,'FaceAlpha',a,'EdgeColor','none','FaceColor',[.2 .2 .2]);
plot([0 0],[0 max(h.Values)+.15],'k')
plot([median(h.Data) median(h.Data)],[0 max(h.Values)+.15],'k-.')
ax.YLim = [0 max(h.Values)+.3]; ax.YAxis.Visible = 'off';

[P,~,STATS] = signrank(h.Data);
disp(['Ranksum Z = ' sprintf('%.2f', STATS.zval) ', p = ' num2str(P,3)])

if P<.05; text(median(h.Data)-.065,max(h.Values)+.2,'*','fontsize',16); end





%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 3F-G %%%%%%%%
% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 950 400], 'Color', 'white');


% load data
T = readtable('fig3fg.csv','ReadVariableNames',true);


%
ax = subplot(1,2,1); hold on;

[P,H,STATS] = signtest(T.afb,T.alb,'method','approximate');
disp(['First vs last block. z=' num2str(STATS.zval,2) ', p=' num2str(P,3)])

b1 = bar(.85,sum(T.afb==1),.2,'FaceColor',[.1 .1 .1],'EdgeColor','none'); 
b2 = bar(1.15,sum(T.afb==2),.2,'FaceColor',[.7 .7 .7],'EdgeColor','none');
bar(1.85,sum(T.alb==1),.2,'FaceColor',[.1 .1 .1],'EdgeColor','none');
bar(2.15,sum(T.alb==2),.2,'FaceColor',[.7 .7 .7],'EdgeColor','none');

if H; plot([1 2],[max([sum(T.afb==1) sum(T.alb==2)]) max([sum(T.afb==1) sum(T.alb==2)])]+2,'k-'); 
text(1.46,max([sum(T.afb==1) sum(T.alb==2)])+2.5,'**','FontName','Helvetica','FontSize',16);
end

set(ax,'xtick',[1 2],'xticklabel',{'First block' 'Last block'},'ytick',5:5:25)
ax.YLabel.String = '# participants';
legend([b1 b2],{'FeRL' 'AbRL'},'box','off')

%
ax = subplot(1,2,2); hold on;

[P,H,STATS] = signtest(T.afh,T.alh,'method','approximate');
disp(['Early vs late blocks. z=' num2str(STATS.zval,2) ', p=' num2str(P,3)])

v = violinplot([T.afh T.alh]);
v(1).ViolinColor = [.961 .592 .106];
v(2).ViolinColor = [.161 .722 .732];

if H; plot([1 2],[max([T.afh; T.alh]) max([T.afh; T.alh])]+.05,'k-'); 
text(1.46,max([T.afh; T.alh])+.1,'**','FontName','Helvetica','FontSize',16);
end

set(ax,'xticklabel',{'Early' 'Late'},'ytick',0:.25:1)
ax.YLabel.String = 'Abstraction level';

