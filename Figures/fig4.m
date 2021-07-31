% -------------------------------------------------------------------------
% This script reproduces fig. 4 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure 4')
disp('    ')
disp('***********')

clear;

%%
% ----------------------------------------------------------------------- %
%%%%%%% FIGURE 4C %%%%%%%%
% open figure
fh = figure; box off;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

% load data
T = readtable('fig4c.csv','ReadVariableNames',true);

scatter(T.ppi, T.lsp, 50,[.3 .3 .3],'filled')
l = lsline;
set(l,'LineWidth',1,'Color',[0 0 0]);
ylabel('Learning speed'); xlabel('vmPFC - VC, PPI strength [a.u.]')
set(gca,'FontName','Helvetica', 'FontSize', 12, 'xlim', [1 8], 'xtick', 2:2:8, 'ylim', [.5 .77], 'ytick', .55:.05:.75);
[a,b] = robustfit(T.ppi, T.lsp);
disp('Robust regression PPI (vmpfc - vc) vs learning speed')
disp(['y = ' sprintf('%.3f', a(1)) ' + ' sprintf('%.3f', a(2)) 'x'])
disp(['t = ' sprintf('%.2f', b.t(2))])
disp(['p = ' num2str(b.p(2),2)])
disp(['df = ' num2str(b.dfe)])

