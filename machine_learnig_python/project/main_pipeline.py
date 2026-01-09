from sklearn.model_selection import train_test_split

from data_generation import generate_synthetic_data
from feature_engineering import add_kurtosis_features
from anomaly_detection import DecisionTreeAnomalyDetector


RANDOM_STATE = 42


def run_pipeline():
    # 1. Generate data
    df = generate_synthetic_data()

    # 2. Feature engineering
    df = add_kurtosis_features(df)

    X = df.drop(columns=["target"])
    y = df["target"]

    # 3. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=RANDOM_STATE
    )

    # 4. Train model
    detector = DecisionTreeAnomalyDetector(random_state=RANDOM_STATE)
    detector.train(X_train, y_train)

    # 5. Evaluate
    report = detector.evaluate(X_test, y_test)
    print("Model Evaluation:\n")
    print(report)

    # 6. Save model
    detector.save("/content/project/decision_tree_model.joblib")
    print("Model saved at /content/project/decision_tree_model.joblib")


if __name__ == "__main__":
    run_pipeline()
