function [loglik] = model_mixRL_PEw_2b(parameters,subj,~)


nd_alpha    = parameters(1); % normally-distributed alpha
alpha       = 1/(1+exp(-nd_alpha)); % alpha (transformed to be between zero and one)

nd_gamma    = parameters(2);
gamma       = 1/(1+exp(-nd_gamma));

nd_mvar     = parameters(3);
mvar        = exp(nd_mvar);

p           = [];


% unpack data
color       = subj.Color;
orientation = subj.Orientation ;
mouth_dir   = subj.Mouth_dir;
actions     = subj.actions+1; % adding 1 such thact actions are {1, 2}
outcome     = subj.Outcome;

T = length(color);


% Q-value for each model and state
q0 = .5;
q8S      = q0 * ones(8, 2);
qDO      = q0 * ones(4, 2);
qDC      = q0 * ones(4, 2);
qOC      = q0 * ones(4, 2);

q       = zeros(4,2);

rpe0 = .5;
rpe8s = rpe0;
rpeDO = rpe0;
rpeDC = rpe0;
rpeOC = rpe0;

gdualRL = 1;

for t=1:T
    
    % read info for the current trial
    a    = actions(t); % action on this trial
    o    = outcome(t); % outcome on this trial
    
    % extract states (3 abstract RL representations, 1 feature RL
    stateDO = mouth_dir(t)*2 + orientation(t)+1 ;
    stateDC = mouth_dir(t)*2 + color(t)+1 ;
    stateOC = orientation(t)*2 + color(t)+1 ;
    
    state8 = mouth_dir(t)*2*2 + orientation(t)*2 + color(t)+1;
    
    q(1,:)= q8S(state8,:);
    q(2,:)= qDO(stateDO,:);
    q(3,:)= qDC(stateDC,:);
    q(4,:)= qOC(stateOC,:);
    
    
    N = t; tmp = [];
    if N==1
        tmp(1,1) = (1 - gamma) * rpe8s(1)^2;
        tmp(1,2) = (1 - gamma) * rpeDO(1)^2;
        tmp(1,3) = (1 - gamma) * rpeDC(1)^2;
        tmp(1,4) = (1 - gamma) * rpeOC(1)^2;
    else
        tmp(1,1) = gamma * rpeb(N-1,1) + (1 - gamma) * rpe8s(end)^2;
        tmp(1,2) = gamma * rpeb(N-1,2) + (1 - gamma) * rpeDO(end)^2;
        tmp(1,3) = gamma * rpeb(N-1,3) + (1 - gamma) * rpeDC(end)^2;
        tmp(1,4) = gamma * rpeb(N-1,4) + (1 - gamma) * rpeOC(end)^2;
    end
    rpeb(t,:) = tmp;
    
    lambda = exp( - rpeb(t,:)/mvar)./sum(exp( - rpeb(t,:)/mvar));
    
    
    % probability of action 1
    % this is equivalant to the softmax function, but overcomes the problem
    % of overflow when q-values or beta are large.
    ptmp   = 1./(1+exp(-(q(:, 1)-q(:, 2))));
    
    % store probability of the chosen action
    p1     = sum(lambda .* ptmp');
    
    % probability of action 2
    p2   = 1-p1;
    
    % store probability of the chosen action
    if a==1
        p(end+1) = p1;
    elseif a==2
        p(end+1) = p2;
    end
    
    
    % update 8S
    delta1              = o - q8S(state8, a); % prediction error
    q8S(state8, a)      = q8S(state8, a) + (lambda(1)*alpha*delta1);
    rpe8s(end+1)        = delta1;
    
    % update state DO
    delta1              = o - qDO(stateDO, a); % prediction error
    qDO(stateDO, a)     = qDO(stateDO, a) + (lambda(2)*alpha*delta1);
    rpeDO(end+1)        = delta1;
    
    
    % update state DC
    delta1              = o - qDC(stateDC, a); % prediction error
    qDC(stateDC, a)     = qDC(stateDC, a) + (lambda(3)*alpha*delta1);
    rpeDC(end+1)        = delta1;
    
    
    % update state OC
    delta1              = o - qOC(stateOC, a); % prediction error
    qOC(stateOC, a)     = qOC(stateOC, a) + (lambda(4)*alpha*delta1);
    rpeOC(end+1)        = delta1;
    
    if gdualRL
        a2                  = mod(a, 2)+1 ;
        
        delta2              = 1 - o - q8S(state8, a2); % prediction error
        q8S(state8, a2)     = q8S(state8, a2) + (lambda(1)*alpha*delta2);
        
        delta2              = 1 - o - qDO(stateDO, a2); % prediction error
        qDO(stateDO, a2)    = qDO(stateDO, a2) + (lambda(2)*alpha*delta2);
        
        delta2              = 1 - o - qDC(stateDC, a2); % prediction error
        qDC(stateDC, a2)    = qDC(stateDC, a2) + (lambda(3)*alpha*delta2);
        
        delta2              = 1 - o - qOC(stateOC, a2); % prediction error
        qOC(stateOC, a2)    = qOC(stateOC, a2) + (lambda(4)*alpha*delta2);
    end
end

% log-likelihood is defined as the sum of log-probability of choice data
% (given the parameters).
loglik = sum(log(p+eps));
% Note that eps is a very small number in matlab (type eps in the command
% window to see how small it is), which does not have any effect in practice,
% but it overcomes the problem of underflow when p is very very small
% (effectively 0).
end






