clear;

rng(44501)

load('../Mydata_Orderblk.mat')
numSub  = size(Mydata_Orderblk,1);
f       = fieldnames(Mydata_Orderblk{1,1});
maxB    = 20;
Nmod    = 3;
nparm   = [3 2 2];

MF          = nan(maxB, numSub, Nmod);
NLL         = nan(maxB, numSub, Nmod);

for i = 1:Nmod
    m = zeros(nparm(i),1);
    v = 6.25;
    prior_RL(i) = struct('mean',m,'variance',v);
    Theta{i}    = nan(maxB, numSub, nparm(i));
end

fname_MoERL = 'lap_MoERL.mat';
fname_FeRL  = 'lap_FeRL.mat';
fname_AbRL  = 'lap_AbRL.mat';

fcbm_maps   = {fname_MoERL fname_FeRL fname_AbRL};
models      = {@model_mixRL_PEw_2b, @model_RL_8states_v2, @model_RL_4states_v2};


for tr=1: maxB
    ctr = 1;
    Data= [];
    for j=1:numSub
        subj = Mydata_Orderblk{j,tr};
        if isempty(subj)
        else
            Data{ctr, 1}=subj;
            ctr = ctr+1;
        end
    end
    
    CBMmrl = cbm_lap(Data, @model_mixRL_PEw_2b, prior_RL(1), fname_MoERL);
    CBMfrl = cbm_lap(Data, @model_RL_8states_v2, prior_RL(2), fname_FeRL);
    CBMarl = cbm_lap(Data, @model_RL_4states_v2, prior_RL(3), fname_AbRL);
    
    fname_hbi_blk = ['hbi_RL_blk_',num2str(tr),'.mat'];
    
    
    cbm_hbi(Data,models,fcbm_maps,fname_hbi_blk);
    load(fname_hbi_blk);
        
    
    % get indices of subjects for which there was data for this block
    subidx = ~cellfun(@isempty, Mydata_Orderblk(:,tr));
    
    MF(tr, subidx, :)       = cbm.output.responsibility;
    
    NLL(tr, subidx, 1)      = -CBMmrl.math.loglik;
    Theta{1}(tr, subidx, :) = [CBMmrl.math.theta{:}]';
    
    NLL(tr, subidx, 2)      = -CBMfrl.math.loglik;
    Theta{2}(tr, subidx, :) = [CBMfrl.math.theta{:}]';
    
    NLL(tr, subidx, 3)      = -CBMarl.math.loglik;
    Theta{3}(tr, subidx, :) = [CBMarl.math.theta{:}]';
    
    
    
    
end

save('MF.mat','MF')
save('NLL.mat','NLL')
save('Theta.mat','Theta')
delete hbi* lap*
    
    