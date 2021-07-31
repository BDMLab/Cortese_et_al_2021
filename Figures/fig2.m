% -------------------------------------------------------------------------
% This script reproduces fig. 2 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure 2')
disp('    ')
disp('***********')

clear;


%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE 2D %%%%%%%%

% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 850 850], 'Color', 'white');

% color 
clr         = [44 49 102; 52 185 208; 241 82 55; 219 172 83]./255;
filepaths   = {'valuemodel.csv' 'valuesubs.csv' 'lambdamodel.csv' 'lambdasubs.csv'};
nsbj        = [33 45];
yl          = [.49 .74; .49 .74; 0.1 0.61; 0 0.85];
yt          = {[.5:.05:.7] [.5:.05:.7] [.1:.1:.6] [.1:.1:.8]};
ylab        = {'\lambda (responsibility)' 'Mean expected value'};

for i = 1:4
    % create subplot for model values
    ax = subplot(2,2,i);
    
    % load data
    T = readtable(filepaths{i});
    numsub = nsbj(mod(i,2)+1); maxB = 20;
    
    for j=1:4
        b = bar(j, nanmean(nanmean(T{:,1+maxB*(j-1):maxB*j},2)), 'FaceColor', clr(j,:), 'EdgeColor', 'none'); alpha(b, .5); hold on;
        scatter(j+randn(numsub,1)*.1, nanmean(T{:,1+maxB*(j-1):maxB*j},2), 30, clr(j,:));
        errorbar(j, nanmean(nanmean(T{:,1+maxB*(j-1):maxB*j},2)), nanstd(nanmean(T{:,1+maxB*(j-1):maxB*j},2))/sqrt(numsub), 'k', 'LineWidth', 2, 'CapSize', 0)
    end
    ax.YLabel.String = ylab{(i<3)+1};
    set(ax,'ylim',yl(i,:),'ytick',yt{i},'xtick',1:4,'xticklabel',{'AbRL' 'FeRL' 'AbRL-w1' 'AbRL-w2'}, 'xticklabelrotation', 45);
    
    if mod(i,2); title('Model'); else; title('Subjects'); end
    
    [P(1),~,STATS(1)] = signrank(nanmean(T{:,1:20},2),nanmean(T{:,21:40},2));
    [P(2),~,STATS(2)] = signrank(nanmean(T{:,1:20},2),nanmean(T{:,41:60},2));
    [P(3),~,STATS(3)] = signrank(nanmean(T{:,1:20},2),nanmean(T{:,61:80},2));
    [P(4),~,STATS(4)] = signrank(nanmean(T{:,21:40},2),nanmean(T{:,41:60},2));
    [P(5),~,STATS(5)] = signrank(nanmean(T{:,21:40},2),nanmean(T{:,61:80},2));
    [P(6),~,STATS(6)] = signrank(nanmean(T{:,41:60},2),nanmean(T{:,61:80},2));
    disp('z-val from signed rank tests:'); disp([STATS.zval])
    [h, crit_p, adj_ci_cvrg, adj_p]=fdr_bh(P);
    disp('p-val, adjusted for multiple comparisons (FDR):'); for i=1:6; disp(adj_p(i)); end
end




%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S2E %%%%%%%%

% load data
T = readtable('fig2e.csv','ReadVariableNames',true);

% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

% compute regression
[a,b]=robustfit(T.vv,T.ls);
disp(['y = ' sprintf('%.3f', a(1)) ' + ' sprintf('%.3f', a(2)) 'x'])
disp(['t = ' sprintf('%.2f', b.t(2))])
disp(['p = ' sprintf('%.3f', b.p(2))])
disp(['df = ' num2str(b.dfe)])

% line fit (robust regression)
x = 0.02:.001:0.14;
y = a(1) + a(2)*x;
plot(x,y,'k-','LineWidth',2)

% scatter plot
scatter(T.vv,T.ls,50,[.3 .3 .3],'filled')

% set axes etc
ax = gca; set(ax,'xtick',.02:.03:.15,'xlim',[.01 .15],'ytick',.5:.05:.9,'FontName','Helvetica','FontSize',12)
ax.XLabel.String = '\nu'; ax.YLabel.String = 'Learning speed';


