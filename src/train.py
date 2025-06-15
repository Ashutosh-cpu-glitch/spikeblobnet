# src/train.py

import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD
from sklearn.model_selection import train_test_split
from src.model import build_model

# Load data
data = np.load('data/blob_data.npz')
X = data['X']
y = data['y']

# One-hot encode labels
y_cat = to_categorical(y, num_classes=4)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=1)

# Build model
model = build_model()
model.compile(loss='categorical_crossentropy', optimizer=SGD(learning_rate=0.1), metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=30, verbose=2)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {acc*100:.2f}%")
