import numpy as np


class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []

        for i in range(len(layer_sizes) - 1):
            # Create a matrix of random weights
            w = np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * 0.5
            # Create biases for each layer
            b = np.zeros((1, layer_sizes[i + 1]))

            self.weights.append(w)
            self.biases.append(b)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        self.activations = [X]
        current = X
        for w, b in zip(self.weights, self.biases):
            z = current @ w + b
            current = self.sigmoid(z)
            self.activations.append(current)
        return current

    def backward(self, X, y, learning_rate=0.1):
        m = X.shape[0]
        output = self.activations[-1]
        delta = output - y

        for i in range(len(self.weights) - 1, -1, -1):
            dW = self.activations[i].T @ delta / m
            dB = np.sum(delta, axis=0, keepdims=True)
            if i > 0:
                delta = (delta @ self.weights[i].T) * self.sigmoid_derivative(self.activations[i])
            self.weights[i] -= learning_rate * dW
            self.biases[i] -= learning_rate * dB

    def train_step(self, X, y, learning_rate=0.1):
        output = self.forward(X)
        loss = float(np.mean((output - y) ** 2))
        self.backward(X, y, learning_rate)
        return loss
