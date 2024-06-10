import torch

class AutoEncoder(torch.nn.Module):
    def __init__(self):
        super().__init__()
        """
        Create a simple AutoEncoder
        """
        # Use an AutoEncoder and try to reconstruct both signals (the 20 samples back)
        self.encoder = torch.nn.Sequential(
            torch.nn.Linear(20, 10),
            torch.nn.ReLU(),
            torch.nn.Linear(10, 5),
        )

        self.decoder = torch.nn.Sequential(
            torch.nn.Linear(5, 10),
            torch.nn.ReLU(),
            torch.nn.Linear(10, 20),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded