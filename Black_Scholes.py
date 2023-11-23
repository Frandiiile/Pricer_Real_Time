def BS_CALL(S, K, T, r, sigma):
    import numpy as np
    from scipy.stats import norm
    N = norm.cdf
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    import numpy as np
    from scipy.stats import norm
    N = norm.cdf
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)
print(BS_CALL(100, 100, 1, 0.05, 0.25))
print(BS_PUT(100, 100, 1, 0.05, 0.25))

