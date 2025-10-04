import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt


data = pd.read_csv('dava_sonuclari.csv')
data.head()


np.random.seed(42)
data["Outcome"] = np.random.choice([0, 1], size=len(data))

data_encoded = pd.get_dummies(data, columns=["Case Type"], drop_first=True)

X = data_encoded.drop("Outcome", axis=1)
y = data_encoded["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

clf = DecisionTreeClassifier(random_state=42, max_depth=4)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-Score:", f1_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(18,8))
plot_tree(clf, feature_names=X.columns, class_names=["0", "1"], filled=True)
plt.show()