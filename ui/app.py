import customtkinter as ctk

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

if __name__ == "__main__":
    app = App()
    app.mainloop()