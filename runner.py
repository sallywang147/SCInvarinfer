import click
import pandas as pd
from xgboost import XGBClassifier
from sklearn.external import joblib

@click.command()
@click.aragument("--model-file", type=str, default="model.pkl")
@click.argument("training_data", type=str)
@click.option("--prediction-file", type=str, default="predictions.txt")
@click.option("--n-estimators", type=int, default=500)
@click.option("--max-depth", type=int, default=3)
@click.option("--learning-rate", type=float, default=0.15)
def main(
    training_data,
    model_file,
    prediction_file,
    n_estimators,
    max_depth,
    learning_rate
):
    training_df = pd.read_csv(training_data)
    X = training_df.drop(columns="target")
    y = training_df[["target"]]
    model = XGBClassifier(
        max_depth=max_depth,
        n_estimators=n_estimators,
        learning_rate=learning_rate
    )
    model.fit(X, y)
    predictions = model.predict(X)
    training_df.loc[:, "predictions"] = predictions
    training_df.to_csv(prediction_file, index=False)
    joblib.dump(model, model_file)

if __name__ == "__main__":
   # A little disconcerting, but click injects the arguments for you.
    main()