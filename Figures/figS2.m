% -------------------------------------------------------------------------
% This script reproduces fig. 3 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Supp Figure S2')
disp('    ')
disp('***********')


%%
% ----------------------------------------------------------------------- %

%%%%%%% LOAD DATA %%%%%%%%
% load data
nsub = 33;
nblk = 20; 
nmod = 3;
T = reshape(table2array(readtable('figS2.csv','ReadVariableNames',true)), nblk, nsub, nmod); % n: 20 blocks max, 33 subj, 3 models


%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S2A %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 400 450], 'Color', 'white');

% set data for plot
[~, ix] = max(T, [], 3); % take model ID based on max likelihood
ix_real = nan(nblk, nsub);
for i = 1:nsub
    t = table2array(readtable(['sub-' num2str(i) '.csv']));
    ix_real(1:length(t), i) = ix(t, i);
end
for j = 1:20 % plot until block = 11
    b(1,j) = sum(ix_real(j,:)==1)/sum(~isnan(ix_real(j,:)));
    b(2,j) = sum(ix_real(j,:)==2)/sum(~isnan(ix_real(j,:)));
    b(3,j) = sum(ix_real(j,:)==3)/sum(~isnan(ix_real(j,:)));
end
% bar(1, sum(ix_real(:)==1)/sum(~isnan(ix_real(:)))*100,.6,'FaceColor',[.16 .65 .22],'EdgeColor','none','FaceAlpha',.4);
% bar(2, sum(ix_real(:)==2)/sum(~isnan(ix_real(:)))*100,.6,'FaceColor',[.16 .41 .83],'EdgeColor','none','FaceAlpha',.4);
% bar(3, sum(ix_real(:)==3)/sum(~isnan(ix_real(:)))*100,.6,'FaceColor',[.28 .76 .84],'EdgeColor','none','FaceAlpha',.4);
bar(1, mean(b(1,:))*100,.6,'FaceColor',[.16 .65 .22],'EdgeColor','none','FaceAlpha',.4);
bar(2, mean(b(2,:))*100,.6,'FaceColor',[.16 .41 .83],'EdgeColor','none','FaceAlpha',.4);
bar(3, mean(b(3,:))*100,.6,'FaceColor',[.28 .76 .84],'EdgeColor','none','FaceAlpha',.4);
errorbar(1, mean(b(1,:))*100,std(b(1,:))./sqrt(length(b))*100,'CapSize',0,'LineStyle','none','Color','k');
errorbar(2, mean(b(2,:))*100,std(b(2,:))./sqrt(length(b))*100,'CapSize',0,'LineStyle','none','Color','k');
errorbar(3, mean(b(3,:))*100,std(b(3,:))./sqrt(length(b))*100,'CapSize',0,'LineStyle','none','Color','k');

set(gca,'xlim',[0 4],'xtick',1:3,'xticklabel',{'MoE-RL' 'FeRL' 'AbRL'},'ylim',[0 60]);
ylabel('Model best fit [% participants]')


%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S2B %%%%%%%%
% open figure
fh = figure; box off; hold on
set(fh, 'Position', [0 1200 400 450], 'Color', 'white');

% set data for plot
[~, ix] = max(T, [], 3); % take model ID based on max likelihood
ix_real = nan(nblk, nsub);
for i = 1:nsub
    t = table2array(readtable(['sub-' num2str(i) '.csv']));
    ix_real(1:length(t), i) = ix(t, i);
end
for j = 1:20 % plot until block = 11
    b(1,j) = sum(ix_real(j,:)==1)/sum(~isnan(ix_real(j,:)));
    b(2,j) = sum(ix_real(j,:)==2)/sum(~isnan(ix_real(j,:)));
    b(3,j) = sum(ix_real(j,:)==3)/sum(~isnan(ix_real(j,:)));
end
bar(1, sum(ix_real(:)==1)/sum(~isnan(ix_real(:)))*100,.6,'FaceColor',[.16 .65 .22],'EdgeColor','none','FaceAlpha',.4);
bar(2, sum(ix_real(:)==2)/sum(~isnan(ix_real(:)))*100,.6,'FaceColor',[.16 .41 .83],'EdgeColor','none','FaceAlpha',.4);
bar(3, sum(ix_real(:)==3)/sum(~isnan(ix_real(:)))*100,.6,'FaceColor',[.28 .76 .84],'EdgeColor','none','FaceAlpha',.4);

set(gca,'xlim',[0 4],'xtick',1:3,'xticklabel',{'MoE-RL' 'FeRL' 'AbRL'},'ylim',[0 60]);
ylabel('Model best fit [% blocks]')
clear b


%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S2C %%%%%%%%
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
for j = 1:20 % plot until block = 11
    b(1) = bar(-.25+j, sum(ix_real(j,:)==1),.23,'FaceColor',[.16 .65 .22],'EdgeColor','none','FaceAlpha',.4);
    b(2) = bar(j, sum(ix_real(j,:)==2),.23,'FaceColor',[.16 .41 .83],'EdgeColor','none','FaceAlpha',.4);
    b(3) = bar(.25+j, sum(ix_real(j,:)==3),.23,'FaceColor',[.28 .76 .84],'EdgeColor','none','FaceAlpha',.4);
end

set(gca,'xlim',[0 21],'xtick',1:3:22,'ylim',[0 25]);
xlabel('time [# blocks]'); ylabel('mean nfb score (block)')
legend(b, {'MoE-RL' 'FeRL' 'AbRL'}, 'location', 'best', 'box', 'off')






%%
% ----------------------------------------------------------------------- %

%%%%%%% LOAD DATA %%%%%%%%
% load data
nsub = 44;
nblk = 20; 
nmod = 3;
T = reshape(table2array(readtable('figS2-1.csv','ReadVariableNames',true)), nblk, nsub, nmod); % n: 20 blocks max, 33 subj, 3 models
%%
% ----------------------------------------------------------------------- %

%%%%%%% FIGURE S12 %%%%%%%%
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
