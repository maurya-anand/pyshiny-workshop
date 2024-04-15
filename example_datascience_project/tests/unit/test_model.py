from example_datascience_project.model import predict
import numpy as np

def test_predict():
    # Given
    X = np.array([1, 2, 3])
    expected_prediction = 2.0

    # When
    prediction = predict(X)

    # Then
    assert prediction == expected_prediction
