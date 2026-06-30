import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Neural Network Playground")
        self.geometry("1200x700")

if __name__ == "__main__":
    app = App()
    app.mainloop()