import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib


df = pd.read_csv("quantum_channel_data.csv")
print("✅ Dataset loaded successfully!")
print(df.head())


X = df.drop("NoiseLabel", axis=1)
y = df["NoiseLabel"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(
    n_estimators=100,       # number of trees
    max_depth=8,            # how deep each tree can go
    random_state=42
)
model.fit(X_train, y_train)
print("\n🌲 Random Forest training completed!")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy: {accuracy*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


joblib.dump(model, "ml_model/noise_predictor.pkl")
print("\n💾 Model saved as 'noise_predictor.pkl' inside ml_model folder.")
