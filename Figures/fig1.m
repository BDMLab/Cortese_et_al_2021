% -------------------------------------------------------------------------
% This script reproduces fig. 1 from the paper Cortese et al 2021
%
% -------------------------------------------------------------------------
% last modified: 2020/04/06 Aurelio Cortese

disp('***********')
disp('    ')
disp('Running script for Figure 1')
disp('    ')
disp('***********')


%%
% load data
T = readtable('fig1c.csv','ReadVariableNames',true);

%%%%%%% FIGURE 1C %%%%%%%%
% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

% plot mean and SEM
scatter(T.x, T.mean, 40, [.3 .3 .3], 'filled')
errorbar(T.x, T.mean, T.SEM, 'LineStyle', 'none', 'CapSize', 0, 'Color', [.3 .3 .3])

% calculate exponential fit
x1 = linspace(1,T.x(end),500);
x = T.x; y = T.mean;
fcn = @(b,x) b(1) * exp(-b(2) * x) + b(3);
[B,~] = fminsearch(@(b) norm(y - fcn(b,x)), ones(3,1));

% plot line fit 
plot(x1, fcn(B,x1), 'Color', [0 0 0], 'LineWidth', 2)

% calculate coordinates for SEM drawing around the curve
xfill = [x1'; flipud(x1')];
y1 = T.CI95l;
[B1,~] = fminsearch(@(b) norm(y1 - fcn(b,x)), ones(3,1));
y2 = T.CI95u;
[B2,~] = fminsearch(@(b) norm(y2 - fcn(b,x)), ones(3,1));
yfill = [fcn(B1,x1)'; flipud(fcn(B2,x1)')];

% draw 95CI
f = fill(xfill, yfill, [.2 .2 .2], 'LineStyle', 'none'); alpha(f,.1);


% set axis labels, limits etc
set(gca, 'xlim', [0 51], 'ylim', [.45 1.0], 'xtick', [1 10 20 30 40 50], 'fontname', 'helvetica')
ylabel('Ratio correct'); xlabel('Trials')



%%
% ----------------------------------------------------------------------- %
% load data
T = readtable('fig1d.csv','ReadVariableNames',true);
nsbj = 33;

%%%%%%% FIGURE 1D %%%%%%%%
% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

% plot individual subject lines
for i = 1:nsbj
    p = polyfit(T.x, eval(['T.x' num2str(i)]), 1);
    yfit = p(1)*T.x + p(2);
    plot(T.x, yfit, 'Color', [.8 .8 .8 .5], 'LineWidth', 1)
end

% plot main line 
p = polyfit(T.x, T.mean, 1);
yfit = p(1)*T.x + p(2);
plot(T.x, yfit, 'Color', [.2 .2 .2], 'LineWidth', 2)

% plot mean data points
s = scatter(T.x,T.mean,75,[.3 .45 .65], 'filled', 'MarkerFaceAlpha', .4)
% errorbars
err = std(table2array(T(:,4:end)),0,2)./sqrt(nsbj);
errorbar(T.x, T.mean, err, 'CapSize', 0, 'LineStyle', 'none', 'Color', 'k')

% set axis labels, limits etc
set(gca, 'xlim', [0.8 11.2], 'ylim', [.25 1.0], 'xtick', [1 4 7 10], 'ytick', .3:.2:.9, 'fontname', 'helvetica')
ylabel('Learning speed'); xlabel('Time [n blocks]')

% statistics: correlation
[r,p] = corr(T.x, T.mean);
disp(['Pearson''s r = ' sprintf('%.2f',r) ', p = ' sprintf('%.3f',p)])



%% 
% ----------------------------------------------------------------------- %
% load data
T = readtable('fig1e.csv','ReadVariableNames',true);

%%%%%%% FIGURE 1E %%%%%%%%
% open figure
fh = figure; box off; hold on;
set(fh, 'Position', [0 1200 550 450], 'Color', 'white');

% plot data points and linear fit
scatter(T.confidence, T.learningspeed, 40, [.2 .2 .2], 'filled')
l = lsline;
set(l,'LineWidth',1,'Color',[0 0 0]);


% set axis labels, limits etc
set(gca, 'xlim', [3.5 8.5], 'ylim', [.50 0.80], 'xtick', 4:8, 'ytick', .55:.05:.75, 'fontname', 'helvetica')
ylabel('Learning speed'); xlabel('Confidence')


% statistics: robust regression
[a,b] = robustfit(T.confidence, T.learningspeed);
disp(['y = ' sprintf('%.3f', a(1)) ' + ' sprintf('%.3f', a(2)) 'x'])
disp(['t = ' sprintf('%.2f', b.t(2))])
disp(['p = ' sprintf('%.3f', b.p(2))])
disp(['df = ' num2str(b.dfe)])

% statistics & controls: correlation
[r1, p1] = corr(T.confidence, T.learningspeed);
[r2, p2] = corr(T.confidence, T.totaltrials);
[r3, p3] = corr(T.confidence, T.propcorr);
n        = length(T.confidence); 
disp(['Confidence vs learning speed. Pearson''s r = '  sprintf('%.2f',r1) ', p = ' sprintf('%.3f',p1)])
disp(['Confidence vs total N trials. Pearson''s r = '  sprintf('%.2f',r2) ', p = ' sprintf('%.3f',p2)])
disp(['Confidence vs prod proportion correct. Pearson''s r = '  sprintf('%.2f',r3) ', p = ' sprintf('%.3f',p3)])

% [z1, p1] = comp_corr_coeff(r1,r2,n,n);
% [z2, p2] = comp_corr_coeff(r1,r3,n,n);
[p1, z1] = corr_rtest(r1,r2,n,n);
[p2, z2] = corr_rtest(r1,r3,n,n);
disp('z-test comparing correlation coefficients')
disp(['Learning speed vs total N trials. z = '  sprintf('%.2f',z1) ', p = ' sprintf('%.3f',p1(2))])
disp(['learning speed vs prod proportion correct. z = '  sprintf('%.2f',z2) ', p = ' sprintf('%.3f',p2(2))])

