# -----------------------------
# 1️⃣ Import Libraries
# -----------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# -----------------------------
# 2️⃣ Read the Dataset
# -----------------------------
data = pd.read_csv("Churn_Modelling.csv")
print("Dataset loaded successfully ✅")
print(data.head())

# -----------------------------
# 3️⃣ Feature and Target Separation
# -----------------------------
X = data.drop(columns=["RowNumber", "CustomerId", "Surname", "Exited"])  # Features
y = data["Exited"]  # Target

# Encode categorical variables
le_gender = LabelEncoder()
le_geo = LabelEncoder()

X["Gender"] = le_gender.fit_transform(X["Gender"])
X["Geography"] = le_geo.fit_transform(X["Geography"])

# -----------------------------
# 4️⃣ Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# -----------------------------
# 5️⃣ Data Normalization
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# 6️⃣ Build Neural Network Model
# -----------------------------
model = Sequential()

# Input layer + Hidden Layer 1
model.add(Dense(16, activation="relu", input_dim=X_train_scaled.shape[1]))

# Hidden Layer 2 with dropout
model.add(Dense(8, activation="relu"))
model.add(Dropout(0.2))

# Output layer
model.add(Dense(1, activation="sigmoid"))

# Compile model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# -----------------------------
# 7️⃣ Train the Model
# -----------------------------
history = model.fit(
    X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1
)

# -----------------------------
# 8️⃣ Evaluate the Model
# -----------------------------
y_pred = (model.predict(X_test_scaled) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\n✅ Model Evaluation Results:")
print("Accuracy Score:", round(accuracy * 100, 2), "%")
print("Confusion Matrix:\n", cm)
