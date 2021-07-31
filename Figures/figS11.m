% -------------------------------------------------------------------------
% This script reproduces fig. S11 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/06/15 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Supp Figure S11')
disp('    ')
disp('***********')


%%
% ----------------------------------------------------------------------- %

%%%%%%% LOAD DATA %%%%%%%%
% load data
Te = readtable('fig3fg.csv','ReadVariableNames',true);
T = readtable('fig6c.csv','ReadVariableNames',true);
Tnfb = readtable('nfb_score.csv','ReadVariableNames',true);
Tnfball = readtable('nfb_score_all.csv','ReadVariableNames',true);



%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S11A %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

N = 14;
M = 9;
for j = 1:2
    Y = table2array(Tnfball(:,(j-1)*N+1:j*N));
    for i = 1:length(Y)
        x = (j-1)*(N+1)+1:(j-1)*(N+1)+sum(~isnan(Y(i,1:M)));
        y = Y(i,~isnan(Y(i,1:M)));
        scatter(x, y, 25, [.2 .2 .2].^2, 'filled')
        X = [ones(length(x),1) x'];
        b = X\y'; 
        slope(i,j) = b(2);
    end
    y = nanmean(Y(:,1:M));
    yerr = nanstd(Y(:,1:M))./sqrt(sum(~isnan(Y(:,1:M))));
    x = (j-1)*(N+1)+1:(j-1)*(N+1)+sum(~isnan(y));
    scatter(x, y, 100, [.2 .78 .65], 'filled')
    errorbar(x, y, yerr, 'LineStyle', 'none', 'Color', [.2 .78 .65], 'LineWidth', 2, 'CapSize', 0)
    X = [ones(length(x),1) x'];
    b = X\y';
    yhat = X*b;
    plot(x, yhat, 'Color', [.82 .17 .21], 'LineWidth', 2)
    [a,b] = robustfit(x,y);
    disp(['Robust fit, slope: t=' sprintf('%.2f',b.t(2)) ', p=' sprintf('%.3f',b.p(2))])
end

set(gca,'xlim',[0 26],'xtick',[1:3:9 16:3:24],'xticklabel',{'1' '4' '7' '1' '4' '7'},'ylim',[0 300]);
xlabel('nfb blocks'); ylabel('nfb score')



%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S11B %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

y = [Tnfb.nfb_score_nrm_s1 Tnfb.nfb_score_nrm_s2];
x = randn(length(y),2)*.1;
bar(1, mean(y(:,1)), .6, 'FaceColor', [.2 .2 .2], 'EdgeColor', 'none', 'FaceAlpha', .25)
bar(2, mean(y(:,2)), .6, 'FaceColor', [.2 .2 .2], 'EdgeColor', 'none', 'FaceAlpha', .25)
errorbar(1, mean(y(:,1)), std(y(:,1))./sqrt(length(y)), 'LineStyle', 'none', 'Color', [.2 .2 .2], 'LineWidth', 2, 'CapSize', 0)
errorbar(2, mean(y(:,2)), std(y(:,2))./sqrt(length(y)), 'LineStyle', 'none', 'Color', [.2 .2 .2], 'LineWidth', 2, 'CapSize', 0)
scatter(1+x(:,1), y(:,1), 100, [.82 .17 .21], 'filled', 'MarkerFaceAlpha', .75)
scatter(2+x(:,2), y(:,2), 100, [.82 .17 .21], 'filled', 'MarkerFaceAlpha', .75)

set(gca,'xlim',[.25 2.75],'xtick',[1 2],'xticklabel',{'Session 1' 'Session 2'},'ylim',[20 270]);
xlabel('nfb sessions'); ylabel('mean nfb score (block)')




%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S11C %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 650 450], 'Color', 'white');

sub = [1 2 3 4 5 6 7 9 10 11 12 13 14 15 16 18 19 21 22 24 27 28];
x = Tnfb.nfb_score_nrm_s1 + Tnfb.nfb_score_nrm_s2;
y = (T.pmsr - Te.afh(sub));

scatter(x,y,100,'filled','k')
l = lsline;
set(l, 'LineWidth', 2, 'Color', [0 0 0])

set(gca,'ylim',[-.05 .75],'ytick',.0:.1:.8,'xlim',[100 500]);
xlabel('nfb score'); ylabel('increase in abstraction')

[r p] = corr(x,y,'type','Spearman','tail','right');
disp(['NFB score vs abstraction. Spearman correlation (right-tailed), rho=' sprintf('%.2f',r) ', p=' sprintf('%.3f',p)])

% save figure
% saveas('../results/figS6.png')




