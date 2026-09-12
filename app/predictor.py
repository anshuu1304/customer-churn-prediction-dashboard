import mlflow


def load_model():
    model = mlflow.pyfunc.load_model(
        "models/champion_model"
    )
    return model