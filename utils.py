
import numpy as np
import torch

def set_seed(seed=42):
    import random
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def analytical_solution_sin(alpha, x, t):
    """
    For BC: T(0,t)=0, T(1,t)=0, IC: sin(pi x)
    Solution: exp(-alpha*pi^2 t) * sin(pi x)
    x,t can be numpy arrays (same shape).
    """
    return np.exp(-alpha*(np.pi**2)*t) * np.sin(np.pi*x)

def make_grid(n_x=101, n_t=101, L=1.0, T_end=1.0):
    xs = np.linspace(0.0, L, n_x)
    ts = np.linspace(0.0, T_end, n_t)
    X, TT = np.meshgrid(xs, ts, indexing='xy')
    return xs, ts, X, TT

def to_tensor(arr, device):
    return torch.tensor(arr, dtype=torch.float32, device=device)
