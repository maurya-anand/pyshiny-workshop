from example_datascience_project.model import predict
from example_datascience_project.serialization import serialize_prediction
import numpy as np


def main():
    """
    Note that we don't implement any logic in the script itself.
    We call functions from the package.
    """
    # Mocking loading data
    X = np.loadtxt("data/large_data.txt", delimiter=",")

    prediction = predict(X)

    # Serializing prediction
    serialize_prediction(prediction, path="prediction.txt")

if __name__ == "__main__":
    main()
