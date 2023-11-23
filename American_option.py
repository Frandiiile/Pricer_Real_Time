import numpy as np

def american_call_option_pricing(S, K, T, r, sigma, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialize option values at maturity
    call_values = np.maximum(0, S * (u ** np.arange(n, -1, -1)) * (d ** np.arange(0, n+1)) - K)

    # Calculate option values at each node
    for j in range(n-1, -1, -1):
        call_values = np.maximum(S * (u ** np.arange(j, -1, -1)) * (d ** np.arange(0, j+1)) - K,
                                 np.exp(-r * dt) * (p * call_values[:-1] + (1 - p) * call_values[1:]))

    return call_values[0]
def american_put_option_pricing(S, K, T, r, sigma, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialize option values at maturity
    put_values = np.maximum(0, K - S * (u ** np.arange(n, -1, -1)) * (d ** np.arange(0, n+1)))

    # Calculate option values at each node
    for j in range(n-1, -1, -1):
        put_values = np.maximum(K - S * (u ** np.arange(j, -1, -1)) * (d ** np.arange(0, j+1)),
                                np.exp(-r * dt) * (p * put_values[:-1] + (1 - p) * put_values[1:]))

    return put_values[0]

