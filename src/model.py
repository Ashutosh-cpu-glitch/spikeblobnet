# src/model.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf

def build_model():
    tf.random.set_seed(1234)  # for reproducibility
    model = Sequential([
        Dense(2, activation='relu',   name='Hidden_Layer'),
        Dense(4, activation='linear', name='Output_Layer')
    ])
    return model
