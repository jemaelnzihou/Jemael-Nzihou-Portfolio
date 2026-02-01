
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, in_dim=2, out_dim=1, hidden=64, depth=5, activation=nn.Tanh):
        super().__init__()
        layers = [nn.Linear(in_dim, hidden), activation()]
        for _ in range(depth - 1):
            layers += [nn.Linear(hidden, hidden), activation()]
        layers += [nn.Linear(hidden, out_dim)]
        self.net = nn.Sequential(*layers)

        # Xavier init helps stability
        for m in self.net:
            if isinstance(m, nn.Linear):
                nn.init.xavier_normal_(m.weight)
                nn.init.zeros_(m.bias)

    def forward(self, x):
        return self.net(x)

class HeatPINN(nn.Module):
    """
    PINN for 1D heat equation: T_t = alpha * T_xx
    """
    def __init__(self, alpha: float, hidden=64, depth=5):
        super().__init__()
        self.alpha = float(alpha)
        self.model = MLP(in_dim=2, out_dim=1, hidden=hidden, depth=depth, activation=nn.Tanh)

    def T(self, x, t):
        xt = torch.cat([x, t], dim=1)
        return self.model(xt)

    def pde_residual(self, x, t):
        """
        Residual r(x,t) = T_t - alpha * T_xx using autograd.
        """
        x.requires_grad_(True)
        t.requires_grad_(True)

        T = self.T(x, t)

        dT_dt = torch.autograd.grad(
            T, t, grad_outputs=torch.ones_like(T), create_graph=True, retain_graph=True
        )[0]

        dT_dx = torch.autograd.grad(
            T, x, grad_outputs=torch.ones_like(T), create_graph=True, retain_graph=True
        )[0]

        d2T_dx2 = torch.autograd.grad(
            dT_dx, x, grad_outputs=torch.ones_like(dT_dx), create_graph=True, retain_graph=True
        )[0]

        return dT_dt - self.alpha * d2T_dx2
