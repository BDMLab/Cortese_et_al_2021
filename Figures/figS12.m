% -------------------------------------------------------------------------
% This script reproduces fig. 3 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/06/15 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Supp Figure S12')
disp('    ')
disp('***********')



%%
% ----------------------------------------------------------------------- %

%%%%%%% LOAD DATA %%%%%%%%
% load data
nsub = 44;
nblk = 20; 
nmod = 3;
T = reshape(table2array(readtable('figS12.csv','ReadVariableNames',true)), nblk, nsub, nmod); % n: 20 blocks max, 44 subj, 3 models
%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S12B %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 850 450], 'Color', 'white');

% set data for plot
[~, ix] = max(T, [], 3); % take model ID based on max likelihood
ix_real = nan(nblk, nsub);
for i = 1:nsub
    t = table2array(readtable(['sub-' num2str(i) '.csv']));
    ix_real(1:length(t), i) = ix(t, i);
end

six = 1:33;
b(1,:) = bar(1, [nansum(reshape(ix_real(:,six)==1,33*20,1))./sum(~isnan(reshape(ix_real(:,six),33*20,1)))...
    nansum(reshape(ix_real(:,six)==2,33*20,1))./sum(~isnan(reshape(ix_real(:,six),33*20,1)))...
    nansum(reshape(ix_real(:,six)==3,33*20,1))./sum(~isnan(reshape(ix_real(:,six),33*20,1)))], 'stacked');
six = 34:44;
b(2,:) = bar(2, [nansum(reshape(ix_real(:,six)==1,11*20,1))./sum(~isnan(reshape(ix_real(:,six),11*20,1)))...
    nansum(reshape(ix_real(:,six)==2,11*20,1))./sum(~isnan(reshape(ix_real(:,six),11*20,1)))...
    nansum(reshape(ix_real(:,six)==3,11*20,1))./sum(~isnan(reshape(ix_real(:,six),11*20,1)))], 'stacked');

for i = 1:3
    set(b(1,i), 'FaceColor', [.1 .1 .1].*i^2);
    set(b(2,i), 'FaceColor', [.1 .1 .1].*i^2);
end

set(gca,'xlim',[0 3], 'xtick', [1 2], 'xticklabel', {'Main participants' 'Excluded participants'}, 'ylim',[0 1.1]);
ylabel('Proportion best model \newline [MoE-RL, FeRL, AbRL]')

% probability of seeing FeRL proportion in excluded given proportion in
% main subjects

p = nansum(reshape(ix_real(:,1:33)==2,33*20,1))./sum(~isnan(reshape(ix_real(:,1:33),33*20,1)));
n = nansum(reshape(ix_real(:,six)==2,11*20,1)); N = sum(~isnan(reshape(ix_real(:,six),11*20,1)));
pout = myBinomTest(n, N, p);
disp(['P(FeRL-exc | FeRL-main) = ' num2str(p,2) ', pval = ' num2str(pout,2)])
disp(['Nb FeRL: ' num2str(n) ', given Nb: ' num2str(N)])

p = nansum(reshape(ix_real(:,1:33)==3,33*20,1))./sum(~isnan(reshape(ix_real(:,1:33),33*20,1)));
n = nansum(reshape(ix_real(:,six)==3,11*20,1)); N = sum(~isnan(reshape(ix_real(:,six),11*20,1)));
pout = myBinomTest(n, N, p);
disp(['P(AbRL-exc | AbRL-main) = ' num2str(p,2) ', pval = ' num2str(pout,2)])
disp(['Nb FeRL: ' num2str(n) ', given Nb: ' num2str(N)])
