import numpy as np
import numpy.typing as npt

def predict(X: npt.NDArray[np.float64]) -> np.float64:
    return X.mean()
