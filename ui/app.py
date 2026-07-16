import customtkinter as ctk
import numpy as np
from network import NeuralNetwork
from ui.canvas import NetworkCanvas



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Neural Network Playground")
        self.geometry("1200x700")

        self.left = ctk.CTkFrame(self, width=220, corner_radius = 0)
        self.left.pack(side = "left", fill = "y")
        self.left.pack_propagate(False)

        self.center = ctk.CTkFrame(self, corner_radius = 0, fg_color = "#1a1a2e")
        self.center.pack(side = "left", fill = "both", expand = True)

        self.network = NeuralNetwork([2, 4, 1])
        self.network_canvas = NetworkCanvas(self.center, self.network)
        self.network_canvas.pack(fill="both", expand=True)
        self.network_canvas.draw()


        self.right = ctk.CTkFrame(self, width = 280, corner_radius = 0)
        self.right.pack(side = "right", fill = "y")
        self.right.pack_propagate(False)

        self.loss_label = ctk.CTkLabel(self.right, text = "Loss: -", font=("Arial", 14))
        self.loss_label.pack(pady = 20)

        ctk.CTkLabel(self.left, text="Neural Playground", font=("Arial", 16, "bold")).pack(pady=(20, 10))
        self.train_btn = ctk.CTkButton(self.left, text = "Train", fg_color= "#2ecc71", hover_color = "#27ae60", command=self._on_train_click)
        self.train_btn.pack(pady = 20, padx = 12, fill = "x")

        self.reset_btn = ctk.CTkButton(self.left, text = "Reset", fg_color = "#e74c3c", hover_color= "#c0392b", command=self._on_reset_click)
        self.reset_btn.pack(pady = (0, 20), padx = 12, fill = "x")

    def _on_train_click(self):
        X = np.array([[0, 0], [0, 1], [1, 0],[1, 1]], dtype=float)
        y = np.array([[0], [1], [1], [0]], dtype=float)

        loss = 0
        for epoch in range(3000):
            loss = self.network.train_step(X, y, learning_rate = 0.1)

        self.loss_label.configure(text = f"Final loss: {loss:.4f}")
        self.network_canvas.draw()

    def _on_reset_click(self):
        self.network = NeuralNetwork([2, 4, 1])
        self.network_canvas.set_network(self.network)
        self.loss_label.configure(text = "Loss: -")



if __name__ == "__main__":
    app = App()
    app.mainloop()