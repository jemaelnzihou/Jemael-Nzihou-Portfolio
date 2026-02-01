
import os
import numpy as np
import torch
from tqdm import trange
import matplotlib.pyplot as plt

from pinn import HeatPINN
from utils import set_seed, analytical_solution_sin, make_grid, to_tensor

def sample_collocation(n_f, L, T_end, device):
    x = np.random.rand(n_f, 1) * L
    t = np.random.rand(n_f, 1) * T_end
    return to_tensor(x, device), to_tensor(t, device)

def sample_boundary(n_b, L, T_end, device):
    t = np.random.rand(n_b, 1) * T_end
    x0 = np.zeros((n_b, 1))
    xL = np.ones((n_b, 1)) * L
    return (to_tensor(x0, device), to_tensor(t, device),
            to_tensor(xL, device), to_tensor(t.copy(), device))

def sample_initial(n_i, L, device):
    x = np.random.rand(n_i, 1) * L
    t0 = np.zeros((n_i, 1))
    return to_tensor(x, device), to_tensor(t0, device)

def main():
    set_seed(42)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Device:", device)

    # Domain and physics
    L = 1.0
    T_end = 1.0
    alpha = 0.1

    # Training sizes
    n_f = 20000
    n_b = 2000
    n_i = 2000

    # Training hyperparams
    epochs = 5000
    lr = 1e-3

    # Loss weights
    w_pde = 1.0
    w_bc  = 10.0
    w_ic  = 10.0

    pinn = HeatPINN(alpha=alpha, hidden=64, depth=5).to(device)
    opt = torch.optim.Adam(pinn.parameters(), lr=lr)

    # fixed training points
    x_f, t_f = sample_collocation(n_f, L, T_end, device)
    x0, tb, xL, tb2 = sample_boundary(n_b, L, T_end, device)
    x_i, t_i = sample_initial(n_i, L, device)

    # Targets
    T_bc0 = torch.zeros_like(tb)
    T_bcL = torch.zeros_like(tb2)
    T_ic = torch.sin(np.pi * x_i)

    history = {"loss": [], "pde": [], "bc": [], "ic": []}

    pbar = trange(epochs, desc="Training", leave=True)
    for ep in pbar:
        opt.zero_grad()

        r = pinn.pde_residual(x_f, t_f)
        loss_pde = torch.mean(r**2)

        T0 = pinn.T(x0, tb)
        TL = pinn.T(xL, tb2)
        loss_bc = torch.mean((T0 - T_bc0)**2) + torch.mean((TL - T_bcL)**2)

        Ti = pinn.T(x_i, t_i)
        loss_ic = torch.mean((Ti - T_ic)**2)

        loss = w_pde*loss_pde + w_bc*loss_bc + w_ic*loss_ic
        loss.backward()
        opt.step()

        history["loss"].append(loss.item())
        history["pde"].append(loss_pde.item())
        history["bc"].append(loss_bc.item())
        history["ic"].append(loss_ic.item())

        if ep % 100 == 0 or ep == epochs-1:
            pbar.set_postfix({
                "loss": f"{loss.item():.3e}",
                "pde": f"{loss_pde.item():.3e}",
                "bc": f"{loss_bc.item():.3e}",
                "ic": f"{loss_ic.item():.3e}",
            })

    # Evaluation
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    n_x, n_t = 101, 101
    xs, ts, X, TT = make_grid(n_x=n_x, n_t=n_t, L=L, T_end=T_end)
    XT = np.stack([X.reshape(-1), TT.reshape(-1)], axis=1)

    with torch.no_grad():
        xt = torch.tensor(XT, dtype=torch.float32, device=device)
        pred = pinn.model(xt).cpu().numpy().reshape(n_t, n_x)

    true = analytical_solution_sin(alpha, X, TT)
    err = np.abs(pred - true)

    # Plots
    plt.figure()
    plt.plot(history["loss"], label="total")
    plt.plot(history["pde"], label="pde")
    plt.plot(history["bc"], label="bc")
    plt.plot(history["ic"], label="ic")
    plt.yscale("log")
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.legend()
    plt.title("Training Loss")
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, "loss_curves.png"), dpi=200)

    plt.figure()
    for t_pick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        idx = int(t_pick*(n_t-1))
        plt.plot(xs, pred[idx, :], label=f"PINN t={t_pick:.2f}")
        plt.plot(xs, true[idx, :], "--", label=f"True t={t_pick:.2f}")
    plt.xlabel("x")
    plt.ylabel("T")
    plt.title("PINN vs Analytical (time slices)")
    plt.legend(ncol=2, fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, "time_slices.png"), dpi=200)

    plt.figure()
    plt.imshow(err, aspect="auto", origin="lower", extent=[0, L, 0, T_end])
    plt.xlabel("x")
    plt.ylabel("t")
    plt.title("Absolute Error |T_PINN - T_true|")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, "error_heatmap.png"), dpi=200)

    metrics = {
        "alpha": alpha,
        "L": L,
        "T_end": T_end,
        "max_abs_error": float(np.max(err)),
        "mean_abs_error": float(np.mean(err)),
        "rmse": float(np.sqrt(np.mean((pred-true)**2))),
        "epochs": epochs,
        "n_f": n_f,
        "n_b": n_b,
        "n_i": n_i
    }
    import json
    with open(os.path.join(results_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    print("Saved results to:", results_dir)
    print("Metrics:", metrics)

if __name__ == "__main__":
    main()
