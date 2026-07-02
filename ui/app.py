import customtkinter as ctk
from network import NeuralNetwork
from customtkinter.windows.widgets import font

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

        self.right = ctk.CTkFrame(self, width = 280, corner_radius = 0)
        self.right.pack(side = "right", fill = "y")
        self.right.pack_propagate(False)

        ctk.CTkLabel(self.left, text="Neural Playground", font=("Arial", 16, "bold")).pack(pady=(20, 10))
        self.train_btn = ctk.CTkButton(self.left, text = "Train", fg_color= "#2ecc71", hover_color = "#27ae60")
        self.train_btn.pack(pady = 20, padx = 12, fill = "x")



if __name__ == "__main__":
    app = App()
    app.mainloop()