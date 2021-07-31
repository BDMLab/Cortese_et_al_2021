clear;
clc;
rng(44501)


NumModel = 2;

load('../Mydata_Orderblk.mat')
numsub  = size(Mydata_Orderblk,1);
f       = fieldnames(Mydata_Orderblk{1,1});
maxB    = 20;
ctr     = 1;

v           = 6.25;
parameters  = randn(1,2);
prior_RL    = struct('mean',zeros(2,1),'variance',v); % note dimension of 'mean'

fname_RL_8S_v2 = 'lap_RL_8S_v2.mat';
fname_RL_4S_v2 = 'lap_RL_4S_v2.mat';

fcbm_maps   = {'lap_RL_8S_v2.mat', 'lap_RL_4S_v2.mat'};
models      = {@model_RL_8states_v2, @model_RL_4states_v2};

MF      = zeros(maxB, NumModel);
MFall   = zeros(maxB, numsub, NumModel);
NLL     = zeros(maxB, NumModel, numsub);
Theta   = zeros(maxB, NumModel, numsub, 2);

for tr=1: maxB
    ctr = 1;
    Data= [];
    for j=1:numsub
        subj = Mydata_Orderblk{j,tr};
        if isempty(subj)
        else
            Data{ctr, 1}=subj;
            ctr = ctr+1;
        end
    end
    
    CBM8S = cbm_lap(Data, @model_RL_8states_v2, prior_RL, fname_RL_8S_v2);
    CBM4S = cbm_lap(Data, @model_RL_4states_v2, prior_RL, fname_RL_4S_v2);
    
    fname_hbi_blk = ['hbi_RLv2_8-4S_blk_',num2str(tr),'.mat'];
    
    
    cbm_hbi(Data,models,fcbm_maps,fname_hbi_blk);
    load(fname_hbi_blk);
    
    MF(tr, :)=cbm.output.model_frequency;
    
    % get indices of subjects for which there was data for this block
    subidx = ~cellfun(@isempty, Mydata_Orderblk(:,tr));
    
    MFall(tr, subidx, :)=cbm.output.responsibility;
    
    NLL(tr,1,subidx) = -CBM8S.math.loglik;
    NLL(tr,2,subidx) = -CBM4S.math.loglik;
    
    Theta(tr,1,subidx,:) = [CBM8S.math.theta{:}]';
    Theta(tr,2,subidx,:) = [CBM4S.math.theta{:}]';
    
end
save('Mf.mat', 'MF','MFall')
save('NLL.mat','NLL')
save('Theta.mat','Theta')

delete hbi* lap*

