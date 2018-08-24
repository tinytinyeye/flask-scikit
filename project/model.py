from sklearn.datasets import load_boston


def get_data():
    boston = load_boston()
    boston_data = boston.data
    return boston_data
