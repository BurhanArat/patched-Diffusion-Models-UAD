import torch 

def gen_noise(cfg,shape):   


    if cfg.noisetype == 'gaussian':
        ns=torch.randn(shape)   
    else: 
        raise ValueError('Noise type not recognized')
    return ns
