% -------------------------------------------------------------------------
% This script reproduces fig. 3 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2021/06/01 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure S3-1')
disp('    ')
disp('***********')


%%
% -------------------------------------------------------------------- %
%%%%%%% FIGURE SXA %%%%%%%%

% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');


% load data
T2 = readtable('fig3d.csv','ReadVariableNames',true);
T1 = readtable('fig3b-1.csv','ReadVariableNames',true);

% color data and other plotting variables
s   = 15;
clr = [[52 185 208]./255
    [44 49 102]./255];

ix = T1.MF_m1 > T1.MF_m2;

y1 = T2.LR_m1(ix==0);
y2 = T2.LR_m2(ix==1);
y1err = std(y1)/sqrt(length(y1));
y2err = std(y2)/sqrt(length(y2));


b(1) = bar(1, mean(y1), .7, 'FaceColor', clr(1,:), 'EdgeColor', 'none', 'FaceAlpha', .4);
x = 1 + randn(1,length(y1))*.1;
scatter(x, y1, s, clr(1,:), 'filled', 'markerFaceAlpha', .4);
errorbar(1, mean(y1), y1err, 'CapSize', 0, 'LineStyle', 'none', 'Color', [0 0 0], 'LineWidth', 2)
b(2) = bar(2, mean(y2), .7, 'FaceColor', clr(2,:), 'EdgeColor', 'none', 'FaceAlpha', .4);
x = 2 + randn(1,length(y2))*.1;
scatter(x, y2, s, clr(2,:), 'filled', 'markerFaceAlpha', .4);
errorbar(2, mean(y2), y2err, 'CapSize', 0, 'LineStyle', 'none', 'Color', [0 0 0], 'LineWidth', 2)

ax = gca; 
set(ax,'xlim',[0 3],'ylim',[0 1],'xtick',[],'ytick',0:.2:1)
ylabel('Learning rate \alpha')
% 

[P,~,STATS] = ranksum(y1, y2);
disp(['Ranksum Z = ' sprintf('%.2f', STATS.zval) ', p = ' num2str(P,2)])
if P<.001; t = '***'; elseif P<.01; t = '**'; elseif P<.05; t = '*'; else; t = ''; end

plot([1 2],[max([y1;y2]) max([y1;y2])]+.075, 'k-');
text(1.5,max([y1; y2])+.1,t,'fontsize',14, 'fontweight','bold', 'HorizontalAlignment', 'center');


% save figure
% saveas('../results/fig3d.png')


%%
% -------------------------------------------------------------------- %
%%%%%%% FIGURE SXB %%%%%%%%

% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');


% load data
T2 = readtable('fig3e.csv','ReadVariableNames',true);
T1 = readtable('fig3b-1.csv','ReadVariableNames',true);

% color data and other plotting variables
s   = 15;
clr = [[52 185 208]./255
    [44 49 102]./255];

ix = T1.MF_m1 > T1.MF_m2;

y1 = T2.St_m1(ix==0);
y2 = T2.St_m2(ix==1);
y1err = std(y1)/sqrt(length(y1));
y2err = std(y2)/sqrt(length(y2));


b(1) = bar(1, mean(y1), .7, 'FaceColor', clr(1,:), 'EdgeColor', 'none', 'FaceAlpha', .4);
x = 1 + randn(1,length(y1))*.1;
scatter(x, y1, s, clr(1,:), 'filled', 'markerFaceAlpha', .4);
errorbar(1, mean(y1), y1err, 'CapSize', 0, 'LineStyle', 'none', 'Color', [0 0 0], 'LineWidth', 2)
b(2) = bar(2, mean(y2), .7, 'FaceColor', clr(2,:), 'EdgeColor', 'none', 'FaceAlpha', .4);
x = 2 + randn(1,length(y2))*.1;
scatter(x, y2, s, clr(2,:), 'filled', 'markerFaceAlpha', .4);
errorbar(2, mean(y2), y2err, 'CapSize', 0, 'LineStyle', 'none', 'Color', [0 0 0], 'LineWidth', 2)

ax = gca; 
set(ax,'xlim',[0 3],'ylim',[0 8.4],'xtick',[],'ytick',0:8)
ylabel('Greediness \beta')
% 

[P,~,STATS] = ranksum(y1, y2);
disp(['Ranksum Z = ' sprintf('%.2f', STATS.zval) ', p = ' num2str(P,2)])
if P<.001; t = '***'; elseif P<.01; t = '**'; elseif P<.05; t = '*'; else; t = ''; end

plot([1 2],[max([y1;y2]) max([y1;y2])]+.5, 'k-');
text(1.5,max([y1; y2])+.71,t,'fontsize',14, 'fontweight','bold', 'HorizontalAlignment', 'center');


% save figure
% saveas('../results/fig3d.png')

