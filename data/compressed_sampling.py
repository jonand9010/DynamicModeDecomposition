import numpy as np

class Compression:
    def __init__(self, X, num_samples = 100):
        self.X = X
        self.N = len(X)
        self.num_samples = num_samples
    
    def get_compressed_sample(self):
        self.sample_idx = np.floow(np.random.rand(self.num_samples) * self.N).astype(int)
        self.compressed_signal = self.X[self.sample_idx]



