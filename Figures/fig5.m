% -------------------------------------------------------------------------
% This script reproduces fig. 5 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure 5')
disp('    ')
disp('***********')

clear;


%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 5B %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 450 450], 'Color', 'white');

% color 
fc = [.205 .728 .819;
      .176 .192 .401];
  
% load data
T = readtable('fig5b.csv','ReadVariableNames',true);

Nsbj = 33;

Y = [T.fpT_vmpfc; T.apT_vmpfc; T.fpT_hpc; T.apT_hpc];
S = repmat((1:Nsbj)',4,1);
Br = [ones(Nsbj*2,1);2*ones(Nsbj*2,1)];
RL = repmat([ones(Nsbj,1);2*ones(Nsbj,1)],2,1);
FactNames = {'Bregion' 'RL'};
stats = rm_anova2(Y,S,Br,RL,FactNames);
t = table(Y,Br,RL,S);
f = 'Y ~ Br*RL + (1|S)';
disp('** ----------------- **')
disp('Mixed effect model (all)')
disp(' ')
lm = fitglme(t,f)
f = 'Y ~ RL + (1|S)';
disp('** ----------------- **')
disp('Mixed effect model (vmPFC)')
disp(' ')
lm1 = fitglme(t(t.Br==1,:),f)
disp('** ----------------- **')
disp('Mixed effect model (HPC)')
disp(' ')
lm2 = fitglme(t(t.Br==2,:),f)

al = .6; 
y  = [mean(T.fpT_vmpfc) mean(T.apT_vmpfc) mean(T.fpT_hpc) mean(T.apT_hpc)];
yerr = [std(T.fpT_vmpfc) std(T.apT_vmpfc) std(T.fpT_hpc) std(T.apT_hpc)]./sqrt(Nsbj);
b = bar([1 4],y([1 3]),.3,'FaceColor',fc(1,:),'EdgeColor','none'); alpha(b,al);
b = bar([2 5],y([2 4]),.3,'FaceColor',fc(2,:),'EdgeColor','none'); alpha(b,al);
e = errorbar([1 2 4 5],y,yerr,'k','LineStyle','none','LineWidth',2,'CapSize',0);


% plot interaction between areas activity and learning models (if
% significant)
if lm.Coefficients.pValue(4)<.05
    plot([1 1],[max(y(1:2)+yerr(1:2))+.2 max(y(1:2)+yerr(1:2))+.25],'k-'); plot([2 2],[max(y(1:2)+yerr(1:2))+.2 max(y(1:2)+yerr(1:2))+.25],'k-')
    plot([1 2],[max(y(1:2)+yerr(1:2))+.25 max(y(1:2)+yerr(1:2))+.25],'k-')
    plot([4 4],[max(y(3:4)+yerr(3:4))+.2 max(y(3:4)+yerr(3:4))+.25],'k-'); plot([5 5],[max(y(3:4)+yerr(3:4))+.2 max(y(3:4)+yerr(3:4))+.25],'k-')
    plot([4 5],[max(y(3:4)+yerr(3:4))+.25 max(y(3:4)+yerr(3:4))+.25],'k-')
    plot([1.5 1.5],[max(y(1:2)+yerr(1:2))+.25 max(y+yerr)+.35],'k-'); plot([4.5 4.5],[max(y(3:4)+yerr(3:4))+.25 max(y+yerr)+.35],'k-')
    plot([1.5 4.5],[max(y+yerr)+.35 max(y+yerr)+.35],'k-')
    text(2.925,max(y+yerr)+.4,'*','FontName','Helvetica', 'FontSize', 16);
end
ax = gca; set(ax,'FontName','Helvetica', 'FontSize', 12, 'ylim', [2 3.75], 'ytick', 2:.5:4,...
    'xlim', [0 6], 'xtick', [1.5 4.5], 'xticklabel', {'vmPFC ' 'HPC'});
ax.YLabel.String = 'ROI activity [a.u.]';




%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 5C %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 750 450], 'Color', 'white');

% color 
fc = [.205 .728 .819;
      .176 .192 .401];
  
Nsbj = 33;

% load data
T = readtable('fig5c.csv','ReadVariableNames',true);

% reformat data
d1 = [T.vc_1 T.hpc_1 T.vmpfc_1];
d2 = [T.vc_2 T.hpc_2 T.vmpfc_2];

ROI = {'VC' 'HPC' 'vmPFC'};

for i = 1:3
    % group average
    y1 = nanmean(d1(:,i))*100; y2 =  nanmean(d2(:,i))*100;
    e1 = nanstd(d1(:,i))/sqrt(Nsbj)*100; e2 = nanstd(d2(:,i))/sqrt(Nsbj)*100;
    x1 = .8 + 3*(i-1); x2 = 2.2 + 3*(i-1);
    bar(x1, y1, .8, 'Facecolor', fc(1,:),'Edgecolor','none','Facealpha',.4);
    bar(x2,y2, .8, 'Facecolor', fc(2,:),'Edgecolor','none','Facealpha',.4);
    errorbar(x1, y1, e1, 'k', 'CapSize', 0);
    errorbar(x2, y2, e2, 'k', 'CapSize', 0);
    
    % individual data points
    y1 = d1(:,i)*100; y2 =  d2(:,i)*100;
    x1n = .8*ones(Nsbj,1)+randn(Nsbj,1)*0.15 + 3*(i-1);
    x2n = 2.2*ones(Nsbj,1)+randn(Nsbj,1)*0.15 + 3*(i-1);
    plot([x1n x2n]',[y1 y2]','-','Color',[.9 .9 .9 .5],'LineWidth',0.25)
    s1 = scatter(x1n, y1, 35, [.2 .2 .2],'filled'); alpha(s1, .2);
    s2 = scatter(x2n, y2, 35, [.2 .2 .2],'filled'); alpha(s2, .2);
    
    clear Psr STATS;
    [~, Psr(i),~,STATS(i)] = ttest(y1,y2);
    disp([ROI{i} ', Abstract RL vs Feature RL: t=' num2str(STATS(i).tstat) ', p=' num2str(Psr(i))]);
    
    disp('-------')
    
    % if significantdiff, plot on figure
    if Psr(i)<.1 && Psr(i)>.05; text(1.45+3*(i-1),max([y1;y2])+4,'$\dagger$','interpreter','latex','FontSize',16); plot([.8 2.2]+3*(i-1),[max([y1;y2])+2 max([y1;y2])+2],'k-','LineWidth',.5)
    elseif Psr(i)<.05 && Psr(i)>.01; text(1.45+3*(i-1),max([y1;y2])+4,'\ast','FontSize',16); plot([.8 2.2]+3*(i-1),[max([y1;y2])+2 max([y1;y2])+2],'k-','LineWidth',.5)
    elseif Psr(i)<=.01 && Psr(i)>.005; text(1.325+3*(i-1),max([y1;y2])+4,'\ast\ast','FontSize',16); plot([.8 2.2]+3*(i-1),[max([y1;y2])+2 max([y1;y2])+2],'k-','LineWidth',.5)
    elseif Psr(i)<=.005; t=text(1.2+3*(i-1),max([y1;y2])+4,'\ast\ast\ast','FontSize',16); plot([.8 2.2]+3*(i-1),[max([y1;y2])+2 max([y1;y2])+2],'k-','LineWidth',.5)
    end
    
end


plot([0.2 2.8], [100/2 100/2], 'k:'); 
plot([3.2 5.8], [100/2 100/2], 'k:'); 
plot([6.2 8.8], [100/2 100/2], 'k:');
ylabel('Classification acc. [%]');
xlim([0 9]);
ylim([45 82]);
set(gca,'FontName','Helvetica', 'FontSize', 12,'xtick',[1.5 4.5 7.5],'xticklabel', {'VC' 'HPC' 'vmPFC'}, 'ytick', 50:10:80);


% compute statistical test: linear mixed effect model
y = d1(:)-d2(:); % response: difference in decoding accuracy 
br = [zeros(Nsbj,1); ones(Nsbj*2,1)]; % brain region: 0 for VC, 1 for HPC and vmPFC
sub = repmat((1:Nsbj)',3,1); % random effect: subjects
T = table(y,br,sub);
f = 'y ~ br + (1|sub)';
glme = fitglme(T,f);
disp(glme)

