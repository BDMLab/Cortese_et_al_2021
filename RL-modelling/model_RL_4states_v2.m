
function [loglik] = model_RL_4states_v2(parameters,subj)

num_state   = 4;
num_action  = 2;

nd_alpha    = parameters(1); % normally-distributed alpha
alpha       = 1/(1+exp(-nd_alpha)); % alpha (transformed to be between zero and one)

nd_beta     = parameters(2);
beta        = exp(nd_beta);

% unpack data
actions     = subj.actions+1; % adding 1 such thact actions are {1, 2}
outcome     = subj.Outcome; 
color       = subj.Color ;
orientation = subj.Orientation ;
mouth_dir   = subj.Mouth_dir ;

% counter over all trials
ctr         = 1;
% calculating numTrails
U           = unique(subj.block());
numTrails   = zeros(1, length(U));
for i=1:length(U)
    ind=find(subj.block()==U(i));
    numTrails(i)=length(ind);
end

for t1=1:size(numTrails, 2)
    % number of trials
    T       = numTrails(t1);

    % Q-value for each action
    q       = .5 * ones(num_state, num_action); % Q-value for both actions initialized at 0

    % to save probability of choice. Currently NaNs, will be filled below
    p       = [];  
    
    for t=1:T   
        
        if num_state==8
            state= mouth_dir(ctr)*2*2 + orientation(ctr)*2 + color(ctr)+1 ;
        elseif num_state==4
            state= subj.States4(ctr)+1 ;
        elseif num_state==2
            state= subj.States2(ctr)+1 ;
        end
        
        % probability of action 1
        % this is equivalant to the softmax function, but overcomes the problem
        % of overflow when q-values or beta are large.        
        p1   = 1./(1+exp(-beta*(q(state, 1)-q(state, 2))));

        % probability of action 2
        p2   = 1-p1;

        % read info for the current trial
        a    = actions(ctr); % action on this trial
        o    = outcome(ctr); % outcome on this trial

        % store probability of the chosen action
        if a==1
            p(ctr) = p1;
        elseif a==2
            p(ctr) = p2;
        end

        delta1    = o - q(state, a); % prediction error
        q(state, a)     = q(state, a) + (alpha*delta1);  
        
        a2 = mod(a, 2)+1 ;
        delta2    = 1 - o - q(state, a2); % prediction error
        q(state, a2)     = q(state, a2) + (alpha*delta2);  
        
        ctr = ctr+1;
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