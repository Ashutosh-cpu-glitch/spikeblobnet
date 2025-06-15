# SpikeBlobNet

A minimal spiking-inspired neural network trained on synthetic blob data for multi-class classification, mimicking spike behavior through threshold activations.

---

# Overview

This project builds a simple feedforward neural network that draws inspiration from Spiking Neural Networks (SNNs). It uses synthetic 2D blob data (4-class) to demonstrate how threshold-like activations can approximate spiking behavior in traditional deep learning frameworks.

---

# Motivation

While traditional neural networks use continuous activation functions, biological neurons fire only when membrane potentials cross a threshold — a binary spike. This project explores how such "spike-like behavior" can be mimicked using standard tools (e.g., ReLU + thresholding) for educational and experimental purposes.

---

# Project Structure
spikeblobnet/
├── data/
│ └── generate_data.py # Create 4-class synthetic dataset
├── src/
│ ├── model.py # Build spiking-inspired model
│ ├── train.py # Training loop
│ └── utils.py # Helper functions (e.g., accuracy)
├── notebooks/
│ └── 01_explore_data.ipynb # Data visualization & decision boundary
├── outputs/
│ └── decision_boundary.png # Plots and saved outputs
├── README.md
├── requirements.txt
└── .gitignore
