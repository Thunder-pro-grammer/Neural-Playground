import customtkinter as ctk
import numpy as np

class NetworkCanvas(ctk.CTkCanvas):
    def __init__(self, parent, network):
        super().__init__(parent, bg="#1a1a2e", highlightthickness=0)
        self.network = network
        self.bind("<Configure>", self._on_resise)

    def set_network(self, network):
        self.network = network
        self.draw()

    def _on_resise(self, event):
        self.draw()

    def draw(self):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w < 10 or h < 10:
            return

        sizes = self.network.layer_sizes
        n_layers = len(sizes)
        padding = 60
        layer_x = [padding + i * (w - 2 * padding)/(n_layers - 1) for  i in range(n_layers)]

        positions = []
        for i, size in enumerate(sizes):
            col = []
            for j in range(size):
                y = h/2 + (j -(size - 1)/2) * 60
                col.append((layer_x[i], y))
            positions.append(col)

        for layer_idx, weight_matrix in enumerate(self.network.weights):
            max_w = np.max(np.abs(weight_matrix) + 1e-8)
            for i, (x1, y1) in enumerate(positions[layer_idx]):
                for j, (x2, y2) in enumerate(positions[layer_idx+1]):
                    val = weight_matrix[i][j]
                    strength = min(1.0, abs(val)/max_w) ** 0.5
                    thickness = max(1, int(strength*5))

                    if val > 0:
                        r, g, b = 231, 76, 60
                    else:
                        r, g, b = 52, 152, 219

                    grey = 30
                    r = int(grey + (r - grey) * strength)
                    g = int(grey + (g - grey) * strength)
                    b = int(grey + (b - grey) * strength)
                    color = f"#{r:02x}{g:02x}{b:02x}"

                    self.create_line(x1, y1, x2, y2, fill=color, width=thickness)

        for col in positions:
            for x, y in col:
                self.create_oval(x - 15, y-15, x+15, y+15, fill="#2c3e50", outline="#00d4ff", width=2)