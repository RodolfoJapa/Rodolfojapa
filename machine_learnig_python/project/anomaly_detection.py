from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import joblib


class DecisionTreeAnomalyDetector:
    """
    Decision Tree based anomaly detector.
    """

    def __init__(self, random_state: int = 42):
        self.model = DecisionTreeClassifier(
            max_depth=8,
            min_samples_split=20,
            min_samples_leaf=10,
            class_weight="balanced",
            random_state=random_state
        )

    def train(self, X, y):
        self.model.fit(X, y)

    def evaluate(self, X, y):
        predictions = self.model.predict(X)
        return classification_report(y, predictions)

    def save(self, path: str):
        joblib.dump(self.model, path)
